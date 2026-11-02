#!/usr/bin/env python3
"""Сборка архивов навыков для загрузки в чужие среды.

    python3 tools/build_zips.py

Два вида архива на каждый навык из skills/:

    zip/claude/<навык>.zip      папка навыка в корне архива — так требует claude.ai:
                                «The ZIP should contain the skill folder as its root».
    zip/perplexity/<навык>.zip  SKILL.md в корне архива — формат, который Perplexity
                                принял при проверке автором 19.09.2026 (~/NSU-AI-SKILLS).

Архивы лежат в репозитории: слушатель скачивает их со страницы GitHub, ничего не собирая.
После правки навыка — пересобрать и прогнать tools/check.py.

В архив идёт только перечисленное: каталоги skills/*/ с SKILL.md и в них всё, кроме
скрытых файлов, служебных файлов ОС и двойников Finder (урок vault
finder-zip-ships-ignored-files). Найдя PDF, ключ или .env, сборщик отказывается собирать
навык: в исходных PDF бывают необезличенные данные, и один такой файл в архиве дороже
всего остального.

Дата внутри архива постоянная, поэтому сборка без правок навыка даёт те же файлы
и не шумит в git. Сторож сравнивает содержимое, а не байты архива: сжатие у разных
версий zlib может отличаться.
"""

import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
OUT = ROOT / "zip"
LAYOUTS = ("claude", "perplexity")

JUNK = {".DS_Store", "Thumbs.db", "desktop.ini", "__MACOSX"}
FORBIDDEN_SUFFIXES = (".pdf", ".env", ".pem", ".key", ".p12")
FORBIDDEN_NAMES = {"id_rsa", "id_ed25519"}
# Любая постоянная дата годится; 1980-01-01 — нижняя граница формата zip,
# но у получателя выглядит как сбой часов.
FIXED_DATE = (2026, 1, 1, 0, 0, 0)
# Perplexity: до 100 файлов в архиве (замер автора 19.09.2026).
MAX_FILES = 100


class PackError(Exception):
    pass


def skill_dirs():
    return sorted(d for d in SKILLS.iterdir() if (d / "SKILL.md").is_file())


def skip(name):
    return name in JUNK or name.startswith(".") or name.startswith("._")


def skill_files(skill_dir, strict=True):
    """Файлы навыка, которые идут в архив, — пути относительно папки навыка.

    strict=False — для сторожа: запрещённый файл попадает в список, а не роняет разбор,
    чтобы остальные проверки навыка всё равно прошли.
    """
    files = []
    for path in sorted(skill_dir.rglob("*")):
        rel = path.relative_to(skill_dir)
        if any(skip(part) for part in rel.parts) or not path.is_file():
            continue
        if strict and (path.suffix.lower() in FORBIDDEN_SUFFIXES or path.name in FORBIDDEN_NAMES):
            raise PackError(f"{skill_dir.name}: в навыке лежит {rel.as_posix()} — "
                            f"такие файлы в поставку не идут; архив не собран")
        files.append(rel)
    if len(files) > MAX_FILES:
        raise PackError(f"{skill_dir.name}: {len(files)} файлов при пределе {MAX_FILES}")
    return files


def arcname(skill_dir, rel, layout):
    posix = rel.as_posix()
    return f"{skill_dir.name}/{posix}" if layout == "claude" else posix


def zip_path(skill_dir, layout):
    return OUT / layout / f"{skill_dir.name}.zip"


def build(skill_dir, layout):
    files = skill_files(skill_dir)
    target = zip_path(skill_dir, layout)
    target.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED) as z:
        for rel in files:
            info = zipfile.ZipInfo(arcname(skill_dir, rel, layout), FIXED_DATE)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            z.writestr(info, (skill_dir / rel).read_bytes())
    return target, len(files)


def main():
    problems = 0
    for skill_dir in skill_dirs():
        for layout in LAYOUTS:
            try:
                target, count = build(skill_dir, layout)
            except PackError as e:
                print(f"   {e}")
                problems += 1
                continue
            size = target.stat().st_size / 1024
            print(f"{target.relative_to(ROOT).as_posix():<36}{count:>4} файлов{size:>7.0f} КБ")
    if problems:
        print(f"Замечаний: {problems}. Архивы с замечаниями не собраны.")
        return 1
    print("Готово. Дальше: python3 tools/check.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())
