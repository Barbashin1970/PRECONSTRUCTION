# PRECONSTRUCTION — ИИ-пресейл для строителей

Методология и навыки агента для **качественных пресейл-исследований** строительных и
ИТ-для-стройки идей. Собрано из трёх материалов НГУ/НГАУДИ
(см. [knowledge-base/sources/](knowledge-base/sources/README.md)).

> **Главный принцип:** ИИ — инструмент *исследования и упаковки* идеи на стадии
> preconstruction/presale, а **не** обязательный компонент каждого продукта.
> «Создано С ПОМОЩЬЮ ИИ» (вайб-кодинг) ≠ «содержит ИИ ВНУТРИ» (ML в продакшене).

> 🎓 **Слушателям курса / Course students:** пошаговая настройка по шагам, RU + EN —
> [STUDENT-SETUP.md](STUDENT-SETUP.md).

Два зеркальных навыка: [`preconstruction-ru`](skills/preconstruction-ru/SKILL.md) (отчёт
на русском) и [`preconstruction-en`](skills/preconstruction-en/SKILL.md) (на английском).
Навык ведёт интервью, запускает потоки-исследователи (бизнес-анализ, маркетинг,
техэкспертиза, применимость ИИ), проверяет их отчёты скептическим аудитом и сводит всё
в один документ с питчем и вердиктом «нужен ли ИИ внутри продукта».

## Установка — выберите свою среду

| Где вы работаете | Как поставить | Подробно |
|---|---|---|
| **Claude Code** — терминал, VS Code, JetBrains, вкладка Code приложения Claude; macOS, Windows, Linux | плагин одной командой | [↓](#claude-code-плагин) |
| **claude.ai** и приложение Claude | загрузить архив `zip/claude/…` | [↓](#claudeai-и-приложение-claude) |
| **Perplexity** — бесплатно | загрузить архив `zip/perplexity/…` | [↓](#perplexity) |
| **Codex и другие агенты**, или Claude Code без плагинов | установщик `install.sh` / `install.ps1` | [↓](#установщик-macos-linux-windows) |
| **Любой чат** — GigaChat, DeepSeek, ChatGPT | распаковать архив и приложить файлы | [↓](#любой-чат) |

Где навык уже поставлен, хватает фразы «проработай идею: …» — агент возьмёт навык сам.

### Claude Code: плагин

В окне Claude Code (Claude Code 2.1.275 и новее):

```text
/plugin install preconstruction --marketplace Barbashin1970/PRECONSTRUCTION
```

В более старых версиях — двумя командами:

```text
/plugin marketplace add Barbashin1970/PRECONSTRUCTION
/plugin install preconstruction@preconstruction-skills
```

В VS Code: наберите `/plugins` → вкладка **Marketplaces** → добавьте
`Barbashin1970/PRECONSTRUCTION` → вкладка **Plugins** → **Install**. Выберите
«для себя» (user scope) — навыки будут во всех проектах.

Навыки плагина называются `/preconstruction:preconstruction-ru` и
`/preconstruction:preconstruction-en`. Обновление: `/plugin` → **Marketplaces** →
`preconstruction-skills` → **Update marketplace**.

### claude.ai и приложение Claude

1. Скачайте архив: [preconstruction-ru.zip](https://github.com/Barbashin1970/PRECONSTRUCTION/raw/main/zip/claude/preconstruction-ru.zip)
   или [preconstruction-en.zip](https://github.com/Barbashin1970/PRECONSTRUCTION/raw/main/zip/claude/preconstruction-en.zip)
   (папка [zip/claude/](zip/claude/)). Архив не распаковывайте.
2. Включите выполнение кода: **Settings → Capabilities → Code execution and file
   creation** (в новом меню — **Create and edit files**).
3. **Customize → Skills → «+» → Create skill → Upload a skill** и выберите архив.

По справке Anthropic навыки доступны на тарифах Free, Pro, Max, Ultra, Team, Enterprise.
Загруженный навык привязан к учётной записи: он работает на сайте и в приложении Claude
для компьютера, а в Claude Code 2.1.273 и новее появляется сам. В claude.ai потоки идут
по очереди, а не параллельно, — это предусмотрено в навыке. Работу навыков в мобильных
приложениях справка не описывает (на 2026-11-02).

### Perplexity

Скачайте [zip/perplexity/preconstruction-ru.zip](https://github.com/Barbashin1970/PRECONSTRUCTION/raw/main/zip/perplexity/preconstruction-ru.zip)
(или `preconstruction-en.zip`) → **Настройка → Навыки → Создать навык → Загрузить навык**.
Архивы для Perplexity и для claude.ai устроены по-разному: берите из своей папки.

### Установщик: macOS, Linux, Windows

Скачайте репозиторий (**Code → Download ZIP** или `git clone`) и положите папку туда,
где она останется. Установщик ставит навыки в `~/.claude/skills/` (Claude Code)
и `~/.agents/skills/` (Codex и другие агенты), ничего не затирая.

```bash
# macOS, Linux — в терминале, в папке проекта
./install.sh            # ссылки: обновление потом через git pull
./install.sh --copy     # копии: папку проекта можно удалить
./install.sh --uninstall
```

```powershell
# Windows — в PowerShell, в папке проекта
powershell -ExecutionPolicy Bypass -File .\install.ps1             # junction-ссылки, без прав администратора
powershell -ExecutionPolicy Bypass -File .\install.ps1 -Copy
powershell -ExecutionPolicy Bypass -File .\install.ps1 -Uninstall
```

Перезапустите Claude Code — появятся `/preconstruction-ru` и `/preconstruction-en`.
Плагин и установщик вместе не ставьте: каждый навык окажется в списке дважды.

### Любой чат

Распакуйте любой архив, приложите все файлы к новому чату и напишите первым сообщением:
«Следуй инструкции из файла SKILL.md; остальные файлы — справочники к ней». Если сервис
не принимает `.md`, переименуйте файлы в `.txt`.

## Что внутри

```
PRECONSTRUCTION/
├── skills/                    # 📦 навыки — единственный источник
│   ├── preconstruction-ru/    #   🇷🇺 SKILL.md + references/ + examples/ (эталонные отчёты)
│   └── preconstruction-en/    #   🇬🇧 зеркало
├── .claude-plugin/            # плагин и маркетплейс для /plugin
├── zip/                       # готовые архивы: claude/ и perplexity/
├── install.sh, install.ps1    # установщики для macOS/Linux и Windows
├── tools/                     # build_zips.py — сборка архивов, check.py — сторож
├── evals/                     # проверки поведения для claude plugin eval
├── knowledge-base/            # 🇷🇺 база знаний: 8 заметок + индекс (учебник, навыку не нужна)
├── knowledge-base-en/         # 🇬🇧 зеркало базы знаний
├── lectures/                  # лекция 6 и глоссарий, RU + EN
├── research/                  # сюда навык в Claude Code пишет новые отчёты
├── docs/                      # разбор пакета, сценарии использования, бэклог
└── .claude/skills/            # симлинки → ../../skills: навыки видны, когда папка открыта в Claude Code
```

## Для автора: выпуск новой версии

```bash
python3 tools/build_zips.py     # пересобрать архивы zip/
python3 tools/check.py          # сторож: «Расхождений нет.»
claude plugin validate .        # проверка манифестов официальным валидатором
claude plugin eval . --max-cost-usd 5   # проверки поведения — расходуют лимиты
```

Перед `git push` поднимите версию в `.claude-plugin/plugin.json` и в `metadata.version`
обоих `SKILL.md` (сторож сверяет все три) и допишите [CHANGELOG.md](CHANGELOG.md):
пользователи плагина получают правку только с новой версией. Почему устроено так —
[docs/PAKET-RAZBOR.md](docs/PAKET-RAZBOR.md); отложенное — [docs/BEKLOG.md](docs/BEKLOG.md).

## Лицензия

Тексты и навыки — **CC BY 4.0** (с указанием источника), код — **MIT**. Подробно и что под
другими условиями — [LICENSE-CONTENT.md](LICENSE-CONTENT.md) и [LICENSE](LICENSE).

---

# PRECONSTRUCTION — AI pre-sales for builders (EN)

Methodology and agent skills for **high-quality preconstruction (pre-sales) research** of
construction and construction-IT ideas. Two mirrored skills:
[`preconstruction-en`](skills/preconstruction-en/SKILL.md) (English report) and
[`preconstruction-ru`](skills/preconstruction-ru/SKILL.md) (Russian report). The agent
interviews you, runs research streams (business analysis, marketing, feasibility, AI
applicability), audits them skeptically, and consolidates one report with a pitch and an
honest verdict on whether the product needs AI inside.

> **Core principle:** AI is a tool for *researching and packaging* an idea, **not** a mandatory
> component of every product. "Built WITH AI" ≠ "contains AI INSIDE".

## Install — pick your environment

| Where you work | How |
|---|---|
| **Claude Code** (terminal, VS Code, JetBrains, Claude app Code tab; macOS, Windows, Linux) | `/plugin install preconstruction --marketplace Barbashin1970/PRECONSTRUCTION` (2.1.275+); older: `/plugin marketplace add Barbashin1970/PRECONSTRUCTION`, then `/plugin install preconstruction@preconstruction-skills`. Skills: `/preconstruction:preconstruction-en`, `/preconstruction:preconstruction-ru` |
| **claude.ai** and the Claude app | download [zip/claude/preconstruction-en.zip](https://github.com/Barbashin1970/PRECONSTRUCTION/raw/main/zip/claude/preconstruction-en.zip); enable **Settings → Capabilities → Code execution and file creation**; **Customize → Skills → + → Create skill → Upload a skill** |
| **Perplexity** (free) | [zip/perplexity/preconstruction-en.zip](https://github.com/Barbashin1970/PRECONSTRUCTION/raw/main/zip/perplexity/preconstruction-en.zip) → **Settings → Skills → Create skill → Upload skill** |
| **Codex, other agents**, or Claude Code without plugins | `./install.sh` (macOS, Linux) or `powershell -ExecutionPolicy Bypass -File .\install.ps1` (Windows); `--copy` / `-Copy` for copies, `--uninstall` / `-Uninstall` to remove |
| **Any chat** | unzip either archive, attach all files, first message: "Follow the instructions in SKILL.md; the other files are its references" |

Once installed, just say "research this idea: …". On claude.ai and in other chats the streams
run one by one instead of in parallel — the skill is written for that. Skills in the mobile
apps are not described in Anthropic's help (as of 2026-11-02). Knowledge base (English):
[knowledge-base-en/README.md](knowledge-base-en/README.md).

**License:** texts and skills — CC BY 4.0 (with attribution), code — MIT; see
[LICENSE-CONTENT.md](LICENSE-CONTENT.md) and [LICENSE](LICENSE).
