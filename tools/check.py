#!/usr/bin/env python3
"""Сторож пакета: навыки, манифесты, архивы и документы не разошлись между собой и с диском.

    python3 tools/check.py

«Расхождений нет.» — всё сходится, код возврата 0. Иначе — список расхождений и код 1.

Что проверяется (разрывы — по docs/PAKET-RAZBOR.md):
  1. Шапка SKILL.md: только поля спецификации (claude.ai и Skills API отвергают остальные),
     name по правилам и равно имени папки, description не длиннее 1024 знаков и 1024 БАЙТ
     (Perplexity меряет байтами), без < и >, версия равна версии плагина.
  2. Тело SKILL.md короче 500 строк; справочник длиннее 100 строк имеет «Содержание».
  3. Навык самодостаточен: каждая ссылка ведёт на существующий файл внутри папки навыка,
     абсолютных путей нет.
  4. Зеркальность: у preconstruction-ru и preconstruction-en один и тот же набор файлов.
  5. Манифесты плагина и маркетплейса читаются, имена и источник сходятся.
  6. Архивы zip/ собраны из текущих исходников, раскладка верна, лишнего внутри нет.
  7. Ссылки в документах репозитория ведут на существующие файлы.
  8. install.ps1 — только ASCII; в git нет служебных файлов ОС.
  9. Проверки поведения evals/: у каждого случая есть промпт и оценщик.

Шапка разбирается намеренно строгим подмножеством YAML: значение — одной строкой
в двойных кавычках, metadata — один уровень вложенности. Так длина описания в байтах
считается однозначно, а любая другая запись — замечание, а не догадка.
"""

import json
import re
import subprocess
import sys
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_zips as bz  # noqa: E402  — одни и те же правила отбора файлов

ROOT = bz.ROOT
ALLOWED_KEYS = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
RESERVED = ("anthropic", "claude")
DESCRIPTION_MAX = 1024           # знаков у Anthropic и agentskills.io, байт у Perplexity
BODY_MAX_LINES = 500             # лучшие практики Anthropic
TOC_FROM_LINES = 100             # справочник длиннее — с оглавлением в начале
TOC_RE = re.compile(r"^## (Содержание|Contents)\s*$", re.M)
LINK_RE = re.compile(r"\]\(([^)\s]+)\)")
ABS_PATH_RE = re.compile(r"~/[A-Za-z]|/Users/|[A-Z]:\\")
MIRROR = ("preconstruction-ru", "preconstruction-en")

problems = []


def problem(text):
    problems.append(text)


def rel(path):
    return path.relative_to(ROOT).as_posix()


# --- 1. шапка -----------------------------------------------------------------

def scalar(value, where, key):
    if value[:1] in (">", "|"):
        problem(f"{where}: {key} — многострочное значение; пишите одной строкой в двойных кавычках")
        return None
    if value.startswith('"'):
        inner = value[1:-1] if len(value) > 1 and value.endswith('"') else None
        if inner is None or re.search(r'(?<!\\)"', inner):
            problem(f"{where}: {key} — кавычки не закрыты или стоят внутри значения; внутри — «»")
            return value
        return inner.replace('\\"', '"').replace("\\\\", "\\")
    return value


def frontmatter(text, where):
    lines = text.split("\n")
    if lines[0] != "---":
        problem(f"{where}: первая строка не «---» — шапку не прочтёт ни одна среда")
        return {}, text
    try:
        end = lines.index("---", 1)
    except ValueError:
        problem(f"{where}: шапка не закрыта строкой «---»")
        return {}, text
    fields, block = {}, None
    for line in lines[1:end]:
        if not line.strip():
            continue
        top = re.match(r"^([A-Za-z][\w-]*):\s*(.*)$", line)
        nested = re.match(r"^  ([A-Za-z][\w-]*):\s*(.+)$", line)
        if top:
            key, value = top.groups()
            if value:
                fields[key], block = scalar(value, where, key), None
            else:
                fields[key] = block = {}
        elif nested and block is not None:
            block[nested.group(1)] = scalar(nested.group(2), where, nested.group(1))
        else:
            problem(f"{where}: строка шапки не разобрана: {line!r}")
    return fields, "\n".join(lines[end + 1:])


def check_skill(skill_dir, plugin_version):
    where = rel(skill_dir / "SKILL.md")
    fields, body = frontmatter((skill_dir / "SKILL.md").read_text(encoding="utf-8"), where)

    extra = sorted(set(fields) - ALLOWED_KEYS)
    if extra:
        problem(f"{where}: поля {', '.join(extra)} вне спецификации — claude.ai и Skills API "
                f"отвергнут архив («Unexpected key(s) in SKILL.md frontmatter»)")

    name = fields.get("name", "")
    if not (NAME_RE.match(name) and len(name) <= 64):
        problem(f"{where}: name «{name}» — только a-z, 0-9 и одиночные дефисы, до 64 знаков")
    if name != skill_dir.name:
        problem(f"{where}: name «{name}» не равно имени папки «{skill_dir.name}» — "
                f"claude.ai отвергнет («Skill folder name doesn't match the skill name»)")
    if any(word in name for word in RESERVED):
        problem(f"{where}: в name зарезервированное слово ({', '.join(RESERVED)})")

    # None — многострочное описание: замечание уже есть, мерить нечего
    description = fields.get("description", "")
    size = len(description.encode("utf-8")) if description is not None else 0
    if description == "":
        problem(f"{where}: description пустое")
    if description and len(description) > DESCRIPTION_MAX:
        problem(f"{where}: description {len(description)} знаков при пределе {DESCRIPTION_MAX}")
    if size > DESCRIPTION_MAX:
        problem(f"{where}: description {size} байт при пределе Perplexity {DESCRIPTION_MAX}: "
                f"сократить на {size - DESCRIPTION_MAX} байт (по-русски ≈ {(size - DESCRIPTION_MAX + 1) // 2} знаков)")
    if description and ("<" in description or ">" in description):
        problem(f"{where}: в description есть < или > — claude.ai примет их за теги")
    description = description or ""

    metadata = fields.get("metadata") or {}
    if not isinstance(metadata, dict) or metadata.get("version") != plugin_version:
        version = metadata.get("version") if isinstance(metadata, dict) else metadata
        problem(f"{where}: metadata.version «{version}» не равна версии плагина «{plugin_version}»")

    # --- 2. размер тела и оглавления ---
    body_lines = len(body.strip("\n").splitlines())
    if body_lines > BODY_MAX_LINES:
        problem(f"{where}: тело {body_lines} строк при рекомендуемых {BODY_MAX_LINES}")
    for ref in sorted((skill_dir / "references").glob("*.md")):
        text = ref.read_text(encoding="utf-8")
        if len(text.splitlines()) > TOC_FROM_LINES and not TOC_RE.search(text):
            problem(f"{rel(ref)}: длиннее {TOC_FROM_LINES} строк без раздела «## Содержание» / «## Contents»")
    return description, size


# --- 3. самодостаточность -----------------------------------------------------

def links(path):
    for target in LINK_RE.findall(path.read_text(encoding="utf-8")):
        if re.match(r"^(https?:|mailto:|#)", target) or "<" in target:
            continue
        yield target.split("#", 1)[0]


def check_self_contained(skill_dir):
    for file in bz.skill_files(skill_dir, strict=False):
        path = skill_dir / file
        if path.suffix != ".md":
            continue
        text = path.read_text(encoding="utf-8")
        if ABS_PATH_RE.search(text):
            problem(f"{rel(path)}: абсолютный путь — в архиве и на чужой машине его нет")
        for target in links(path):
            resolved = (path.parent / target).resolve()
            if not resolved.exists():
                problem(f"{rel(path)}: ссылка «{target}» ведёт на несуществующий файл")
            elif skill_dir.resolve() not in resolved.parents and resolved != skill_dir.resolve():
                problem(f"{rel(path)}: ссылка «{target}» уходит за папку навыка — в архив это не попадёт")


# --- 5. манифесты -------------------------------------------------------------

def load_json(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as e:
        problem(f"{rel(path)}: не читается как JSON — {e}")
        return {}


def check_manifests():
    plugin = load_json(ROOT / ".claude-plugin" / "plugin.json")
    market = load_json(ROOT / ".claude-plugin" / "marketplace.json")
    name, version = plugin.get("name"), plugin.get("version")
    if not version:
        problem(".claude-plugin/plugin.json: нет version — пользователи плагина не отличат выпуск")
    entries = [p for p in market.get("plugins", []) if p.get("name") == name]
    if not entries:
        problem(f".claude-plugin/marketplace.json: нет записи с name «{name}» из plugin.json — "
                f"установка по имени из манифеста упадёт")
    elif entries[0].get("source") not in ("./", "."):
        problem(".claude-plugin/marketplace.json: source плагина не «./» — решение Р-1 разбора")
    if not market.get("owner", {}).get("name"):
        problem(".claude-plugin/marketplace.json: нет owner.name — обязательное поле")
    if not plugin.get("license") or not (ROOT / "LICENSE").is_file():
        problem("лицензия: нужны файл LICENSE и поле license в plugin.json — без них каталог "
                "плагинов Anthropic не примет плагин")
    return version


# --- 6. архивы ----------------------------------------------------------------

def check_zips(skill_dir):
    try:
        files = bz.skill_files(skill_dir)
    except bz.PackError as e:
        problem(str(e))
        return
    expected = {bz.arcname(skill_dir, f, layout): f for layout in bz.LAYOUTS for f in files}
    for layout in bz.LAYOUTS:
        archive = bz.zip_path(skill_dir, layout)
        if not archive.is_file():
            problem(f"{rel(archive)}: архива нет — python3 tools/build_zips.py")
            continue
        with zipfile.ZipFile(archive) as z:
            names = z.namelist()
            want = sorted(bz.arcname(skill_dir, f, layout) for f in files)
            if sorted(names) != want:
                extra = sorted(set(names) - set(want))
                missing = sorted(set(want) - set(names))
                problem(f"{rel(archive)}: состав не совпадает с навыком; лишнее {extra}, "
                        f"недостаёт {missing} — пересобрать")
                continue
            stale = [n for n in names if z.read(n) != (skill_dir / expected[n]).read_bytes()]
            if stale:
                problem(f"{rel(archive)}: устарел ({len(stale)} файлов не совпадают с исходником, "
                        f"например {stale[0]}) — python3 tools/build_zips.py")


# --- 7–9. документы, гигиена, проверки поведения --------------------------------

def check_docs():
    for path in sorted(ROOT.rglob("*.md")):
        parts = path.relative_to(ROOT).parts
        if parts[0] in (".git", "skills", ".gigacode") or "results" in parts:
            continue
        for target in links(path):
            if ".claude/skills/" in target:
                problem(f"{rel(path)}: ссылка «{target}» идёт через симлинк .claude/skills — "
                        f"на Windows и на сайте GitHub она не откроется; ссылайтесь на skills/")
            elif not (path.parent / target).exists():
                problem(f"{rel(path)}: ссылка «{target}» ведёт на несуществующий файл")


def check_hygiene():
    ps1 = ROOT / "install.ps1"
    if ps1.exists():
        bad = [n for n, line in enumerate(ps1.read_bytes().splitlines(), 1) if any(b > 127 for b in line)]
        if bad:
            problem(f"install.ps1: не-ASCII в строках {bad[:5]} — PowerShell 5.1 исказит их")
    try:
        tracked = subprocess.run(["git", "ls-files"], cwd=ROOT, capture_output=True,
                                 text=True, check=True).stdout.splitlines()
    except (OSError, subprocess.CalledProcessError):
        return  # нет git или не репозиторий — проверять нечего
    junk = [t for t in tracked if Path(t).name in bz.JUNK or Path(t).name.startswith("._")]
    if junk:
        problem(f"в git служебные файлы ОС: {', '.join(junk)} — git rm --cached")


def check_evals(skill_names):
    evals = ROOT / "evals"
    if not evals.is_dir():
        problem("evals/: нет проверок поведения — лучшие практики Anthropic требуют не меньше трёх")
        return
    cases = sorted(p.parent for p in evals.rglob("prompt.md") if "results" not in p.parts)
    if len(cases) < 3:
        problem(f"evals/: {len(cases)} случаев при минимуме 3")
    for case in cases:
        graders = sorted((case / "graders").glob("*.md"))
        if not graders:
            problem(f"{rel(case)}: нет оценщика в graders/ — случай не загрузится")
        for grader in graders:
            text = grader.read_text(encoding="utf-8")
            for skill in re.findall(r"\)\?(preconstruction-[a-z]+)", text):
                if skill not in skill_names:
                    problem(f"{rel(grader)}: ссылается на навык {skill}, которого нет в skills/")


def main():
    version = check_manifests()
    dirs = bz.skill_dirs()
    names = {d.name for d in dirs}
    print(f"{'Навык':<22}{'описание, знаков':>18}{'байт':>7}")
    for skill_dir in dirs:
        description, size = check_skill(skill_dir, version)
        check_self_contained(skill_dir)
        check_zips(skill_dir)
        print(f"{skill_dir.name:<22}{len(description):>18}{size:>7}")

    if set(MIRROR) <= names:
        sets = [{f.as_posix() for f in bz.skill_files(bz.SKILLS / m, strict=False)} for m in MIRROR]
        if sets[0] != sets[1]:
            problem(f"зеркальность: только в {MIRROR[0]} — {sorted(sets[0] - sets[1])}, "
                    f"только в {MIRROR[1]} — {sorted(sets[1] - sets[0])}")
    else:
        problem(f"нет пары навыков {MIRROR}")

    check_docs()
    check_hygiene()
    check_evals(names)

    print()
    if problems:
        for p in problems:
            print(f"   {p}")
        print(f"Расхождений: {len(problems)}.")
        return 1
    print("Расхождений нет.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
