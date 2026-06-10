# Стенд слушателя · Student setup

Пошаговая инструкция для слушателя курса «ИИ в строительстве»: как развернуть на ноутбуке
рабочее место и начать диалог с ИИ-агентом, обученным навыкам пресейл-исследования.

> **Репозиторий проекта:** https://github.com/Barbashin1970/PRECONSTRUCTION
>
> Отсканируй QR-код телефоном — он ведёт на репозиторий:
>
> ![QR на репозиторий](https://api.qrserver.com/v1/create-qr-code/?size=240x240&data=https://github.com/Barbashin1970/PRECONSTRUCTION)

Есть **два пути**. Выбери один:

| Путь | Что нужно | Кому |
|------|-----------|------|
| **A. VS Code + Claude Code** | Платный план Claude (Pro/Max) или курсовой/командный аккаунт | Хочешь полноценный навык с многопоточным исследованием |
| **B. Perplexity (бесплатно)** | Любой аккаунт Perplexity | Нет платного Claude — проходишь методологию вручную |

---

## 🇷🇺 Путь A — VS Code + Claude Code (полноценный навык)

### Что установить заранее
1. **Git** — [git-scm.com/downloads](https://git-scm.com/downloads) (нужен, чтобы скачать проект; можно и без него — см. шаг 2).
2. **VS Code** (версия 1.98 или новее) — [code.visualstudio.com](https://code.visualstudio.com/).
3. Интернет.

### Шаги
1. **Отсканируй QR-код** телефоном (или открой ссылку) → получишь адрес репозитория `https://github.com/Barbashin1970/PRECONSTRUCTION`.
2. **Скачай проект.** Два варианта:
   - **Проще (без Git):** на странице репозитория нажми зелёную кнопку **Code → Download ZIP**, распакуй папку.
   - **Через Git:** открой терминал и выполни
     ```
     git clone https://github.com/Barbashin1970/PRECONSTRUCTION
     ```
3. **Открой папку проекта в VS Code:** меню **File → Open Folder…** → выбери папку проекта.
4. **Зарегистрируйся в Claude:** зайди на [claude.ai](https://claude.ai) и создай профиль.
   > ⚠️ Claude Code работает только с **платным планом** (Claude **Pro** или **Max**) либо с
   > курсовым/командным аккаунтом. На бесплатном тарифе не запустится — тогда выбирай **Путь B**.
   > Проверь актуальные планы на [claude.ai](https://claude.ai).
5. **Установи расширение Claude Code:** в VS Code открой панель расширений
   (`Ctrl+Shift+X` / `Cmd+Shift+X`), найди **«Claude Code»**, нажми **Install**.
   Отдельно ставить что-либо из командной строки не нужно. Доку: [code.claude.com/docs/en/vs-code](https://code.claude.com/docs/en/vs-code).
6. **Войди в аккаунт:** при первом запуске расширение откроет вход через браузер — авторизуйся своим Claude-профилем.
7. **Активируй навыки (важно, особенно на Windows).** Навыки лежат в папке `skills/` проекта.
   Скопируй обе папки навыков в свою личную папку навыков Claude, чтобы они точно подхватились:
   - **macOS / Linux** (терминал в папке проекта):
     ```
     mkdir -p ~/.claude/skills && cp -R skills/preconstruction-ru skills/preconstruction-en ~/.claude/skills/
     ```
   - **Windows** (PowerShell в папке проекта):
     ```
     New-Item -ItemType Directory -Force $HOME\.claude\skills | Out-Null
     Copy-Item -Recurse -Force skills\preconstruction-ru, skills\preconstruction-en $HOME\.claude\skills\
     ```
   > Почему: в репозитории `.claude/skills/` — это ссылки-симлинки на папку `skills/`. На Windows
   > Git часто клонирует их как обычный текст, и навык не виден. Копирование реальных папок решает это раз и навсегда.
8. **Начни работу:** открой чат Claude Code в VS Code и набери
   ```
   /preconstruction-ru
   ```
   (или `/preconstruction-en` для отчёта на английском), затем опиши идею: «проработай идею: …».
   Агент проведёт интервью, запустит несколько потоков-исследователей, проверит их и соберёт
   единый отчёт в папке `research/`.

---

## 🇷🇺 Путь B — Perplexity (бесплатно, методология вручную)

Это тот же подход, что на хакатоне: ИИ как исследовательский ассистент, а ты ведёшь его по этапам.

1. **Зарегистрируйся** на [perplexity.ai](https://www.perplexity.ai) (бесплатного аккаунта хватит).
2. **Скачай файлы проекта** (Download ZIP, см. Путь A, шаг 2) — понадобятся папки `knowledge-base/`
   (или `knowledge-base-en/` для английского) и `skills/`.
3. **Создай Space** в Perplexity (раздел Spaces → Create).
4. **Загрузи в Space файлы-методичку:** из `skills/preconstruction-ru/` — `SKILL.md`, все 4 файла
   из `references/` и 1 готовый отчёт из `examples/` (образец структуры); по желанию добавь заметки
   из `knowledge-base/`. Они станут справочником.
5. **Задай Custom Instructions** (роль агента), например:
   > «Ты — ведущий пресейл-аналитик. Используй загруженные файлы как методологию. Веди меня по
   > 5 этапам пресейла: 1) проблема → 2) бизнес-анализ → 3) техэкспертиза → 4) нужен ли ИИ ВНУТРИ
   > продукта → 5) питч. Опирайся на источники, указывай их, разделяй "сделано С ПОМОЩЬЮ ИИ" и
   > "ИИ ВНУТРИ", будь честным насчёт необходимости ИИ.»
6. **Работай по тредам:** заводи отдельный тред на каждый этап (как 5 шагов методологии),
   в конце попроси собрать единый отчёт и питч.

> Отличие от Пути A: Perplexity не запускает несколько агентов параллельно — ты сам ведёшь его
> по этапам. Зато бесплатно и без установки.

---
---

# 🇬🇧 Student stand — step by step

Step-by-step guide for a student of the “AI in construction” course: set up a workstation on
your laptop and start a dialogue with an AI agent trained in the pre-sales research skill.

> **Project repository:** https://github.com/Barbashin1970/PRECONSTRUCTION
>
> Scan the QR code with your phone — it points to the repository:
>
> ![Repository QR](https://api.qrserver.com/v1/create-qr-code/?size=240x240&data=https://github.com/Barbashin1970/PRECONSTRUCTION)

There are **two paths**. Pick one:

| Path | What you need | For whom |
|------|---------------|----------|
| **A. VS Code + Claude Code** | A paid Claude plan (Pro/Max) or a course/team account | You want the full skill with multi-stream research |
| **B. Perplexity (free)** | Any Perplexity account | No paid Claude — run the methodology manually |

## 🇬🇧 Path A — VS Code + Claude Code (full skill)

### Install first
1. **Git** — [git-scm.com/downloads](https://git-scm.com/downloads) (to download the project; optional — see step 2).
2. **VS Code** (1.98 or newer) — [code.visualstudio.com](https://code.visualstudio.com/).
3. Internet.

### Steps
1. **Scan the QR code** with your phone (or open the link) → you get the repo address `https://github.com/Barbashin1970/PRECONSTRUCTION`.
2. **Get the project.** Two options:
   - **Easiest (no Git):** on the repo page click the green **Code → Download ZIP**, unzip.
   - **With Git:** in a terminal run
     ```
     git clone https://github.com/Barbashin1970/PRECONSTRUCTION
     ```
3. **Open the project folder in VS Code:** **File → Open Folder…** → select the project folder.
4. **Register at Claude:** go to [claude.ai](https://claude.ai) and create a profile.
   > ⚠️ Claude Code requires a **paid plan** (Claude **Pro** or **Max**) or a course/team account.
   > The free tier will not run it — in that case use **Path B**. Check current plans at [claude.ai](https://claude.ai).
5. **Install the Claude Code extension:** in VS Code open Extensions (`Ctrl+Shift+X` / `Cmd+Shift+X`),
   search **“Claude Code”**, click **Install**. No separate command-line install needed.
   Docs: [code.claude.com/docs/en/vs-code](https://code.claude.com/docs/en/vs-code).
6. **Sign in:** on first launch the extension opens a browser login — sign in with your Claude profile.
7. **Activate the skills (important, especially on Windows).** The skills live in the project’s
   `skills/` folder. Copy both skill folders into your personal Claude skills folder so they are reliably picked up:
   - **macOS / Linux** (terminal in the project folder):
     ```
     mkdir -p ~/.claude/skills && cp -R skills/preconstruction-ru skills/preconstruction-en ~/.claude/skills/
     ```
   - **Windows** (PowerShell in the project folder):
     ```
     New-Item -ItemType Directory -Force $HOME\.claude\skills | Out-Null
     Copy-Item -Recurse -Force skills\preconstruction-ru, skills\preconstruction-en $HOME\.claude\skills\
     ```
   > Why: in the repo `.claude/skills/` are symlinks to the `skills/` folder. On Windows, Git often
   > clones them as plain text, so the skill won’t appear. Copying the real folders fixes it for good.
8. **Start working:** open the Claude Code chat in VS Code and type
   ```
   /preconstruction-en
   ```
   (or `/preconstruction-ru` for a Russian report), then describe your idea: “research this idea: …”.
   The agent runs an interview, launches several research streams, audits them, and consolidates a
   single report into the `research/` folder.

## 🇬🇧 Path B — Perplexity (free, run the methodology manually)

Same approach as the hackathon: AI as a research assistant while you drive it through the stages.

1. **Register** at [perplexity.ai](https://www.perplexity.ai) (a free account is enough).
2. **Download the project files** (Download ZIP, see Path A step 2) — you’ll need `knowledge-base-en/`
   (or `knowledge-base/` for Russian) and `skills/`.
3. **Create a Space** in Perplexity (Spaces → Create).
4. **Upload the methodology files:** from `skills/preconstruction-en/` — `SKILL.md`, all 4 files
   from `references/` and one ready report from `examples/` (a structure sample); optionally add
   notes from `knowledge-base-en/`. They become the reference.
5. **Set Custom Instructions** (the agent’s role), e.g.:
   > “You are a lead pre-sales analyst. Use the uploaded files as the methodology. Walk me through
   > the 5 pre-sales stages: 1) problem → 2) business analysis → 3) feasibility → 4) is AI needed
   > INSIDE the product → 5) pitch. Cite sources, separate ‘built WITH AI’ from ‘AI INSIDE’, and be
   > honest about whether AI is needed.”
6. **Work thread by thread:** one thread per stage (the 5 steps), then ask it to assemble a single
   report and pitch.

> Difference from Path A: Perplexity doesn’t run several agents in parallel — you drive it stage by
> stage. But it’s free and needs no installation.
