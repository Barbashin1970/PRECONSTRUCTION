# Стенд слушателя · Student setup

Пошаговая инструкция для слушателя курса «ИИ в строительстве»: как за десять минут
подключить ИИ-агента, обученного навыку пресейл-исследования, и начать с ним диалог.

> **Репозиторий проекта:** https://github.com/Barbashin1970/PRECONSTRUCTION
>
> Отсканируй QR-код телефоном — он ведёт на репозиторий:
>
> ![QR на репозиторий](https://api.qrserver.com/v1/create-qr-code/?size=240x240&data=https://github.com/Barbashin1970/PRECONSTRUCTION)

Есть **три пути**. Выбери один:

| Путь | Что нужно | Как идёт исследование |
|---|---|---|
| **A. VS Code + Claude Code** | платный план Claude (Pro, Max) или курсовой/командный аккаунт | полноценно: несколько потоков-исследователей работают параллельно |
| **B. claude.ai — сайт или приложение Claude** | аккаунт Claude; по справке Anthropic навыки есть и на бесплатном тарифе | те же этапы, но потоки идут по очереди |
| **C. Perplexity — бесплатно** | любой аккаунт Perplexity | те же этапы по очереди, с веб-поиском Perplexity |

На всех путях навык один и тот же; отличается только среда.

---

## 🇷🇺 Путь A — VS Code + Claude Code

### Что установить заранее
1. **VS Code** — [code.visualstudio.com](https://code.visualstudio.com/).
2. **Git** — [git-scm.com/downloads](https://git-scm.com/downloads): Claude Code забирает
   плагин с GitHub клонированием. На macOS и Linux Git обычно уже есть.
3. Интернет. Скачивать проект вручную **не нужно**: навык ставится плагином прямо из GitHub.

### Шаги
1. **Зарегистрируйся в Claude:** [claude.ai](https://claude.ai).
   > ⚠️ Claude Code работает с **платным планом** (Pro или Max) либо с курсовым/командным
   > аккаунтом. Нет платного плана — выбирай путь B или C. Актуальные тарифы — на [claude.ai](https://claude.ai).
2. **Установи расширение Claude Code:** в VS Code открой панель расширений
   (`Ctrl+Shift+X` / `Cmd+Shift+X`), найди **«Claude Code»**, нажми **Install**.
   Документация: [code.claude.com/docs/en/vs-code](https://code.claude.com/docs/en/vs-code).
3. **Войди в аккаунт:** при первом запуске расширение откроет вход через браузер.
4. **Поставь навык.** В окне Claude Code набери:
   ```
   /plugin install preconstruction --marketplace Barbashin1970/PRECONSTRUCTION
   ```
   и выбери **«Install for you»** (для себя). Если команда не сработала — версия старая;
   тогда набери `/plugins`, на вкладке **Marketplaces** добавь `Barbashin1970/PRECONSTRUCTION`,
   на вкладке **Plugins** нажми **Install** у `preconstruction`.
   > Одинаково на Windows, macOS и Linux: ничего не копируешь руками.
5. **Начни работу:** открой любую папку (File → Open Folder…), в чате Claude Code напиши
   «проработай идею: …» — или вызови навык явно: `/preconstruction:preconstruction-ru`
   (отчёт на русском) или `/preconstruction:preconstruction-en` (на английском).
   Агент проведёт интервью, запустит потоки-исследователи, проверит их и сохранит
   отчёт в папку `research/` открытой папки.

---

## 🇷🇺 Путь B — claude.ai (сайт или приложение Claude)

1. **Скачай архив навыка** — не распаковывай его:
   [preconstruction-ru.zip](https://github.com/Barbashin1970/PRECONSTRUCTION/raw/main/zip/claude/preconstruction-ru.zip)
   (для отчёта на английском — [preconstruction-en.zip](https://github.com/Barbashin1970/PRECONSTRUCTION/raw/main/zip/claude/preconstruction-en.zip)).
2. **Войди** на [claude.ai](https://claude.ai) или открой приложение Claude на компьютере.
3. **Включи выполнение кода:** **Settings → Capabilities → Code execution and file creation**
   (в новом меню настроек пункт называется **Create and edit files**).
4. **Загрузи навык:** **Customize → Skills → «+» → Create skill → Upload a skill** → выбери архив.
5. **Начни работу:** в новом чате напиши «проработай идею: …». Отчёт придёт файлом для скачивания.

> На бесплатном тарифе лимиты сообщений ниже — для учебного прогона выбирай глубину «быстрая».
> С телефона архив не загрузить; работает ли загруженный навык в мобильном приложении,
> справка Anthropic не говорит — проверь сам.

---

## 🇷🇺 Путь C — Perplexity (бесплатно)

1. **Зарегистрируйся** на [perplexity.ai](https://www.perplexity.ai).
2. **Скачай архив для Perplexity:**
   [preconstruction-ru.zip](https://github.com/Barbashin1970/PRECONSTRUCTION/raw/main/zip/perplexity/preconstruction-ru.zip)
   (английский — [preconstruction-en.zip](https://github.com/Barbashin1970/PRECONSTRUCTION/raw/main/zip/perplexity/preconstruction-en.zip)).
   Это **другой** архив, чем на пути B: бери именно из папки `perplexity`.
3. **Загрузи навык:** **Настройка → Навыки → Создать навык → Загрузить навык** → выбери архив.
4. **Начни работу:** в новом треде напиши «проработай идею: …».

> Если раздела «Навыки» нет: создай **Space**, загрузи в него файлы из распакованного архива
> и задай в Custom Instructions: «Следуй инструкции из файла SKILL.md; остальные файлы —
> справочники к ней».

---
---

# 🇬🇧 Student setup — step by step

A step-by-step guide for a student of the "AI in construction" course: connect an AI agent
trained in the pre-sales research skill in ten minutes and start a dialogue with it.

> **Project repository:** https://github.com/Barbashin1970/PRECONSTRUCTION
>
> Scan the QR code with your phone — it points to the repository:
>
> ![Repository QR](https://api.qrserver.com/v1/create-qr-code/?size=240x240&data=https://github.com/Barbashin1970/PRECONSTRUCTION)

There are **three paths**. Pick one:

| Path | What you need | How the study runs |
|---|---|---|
| **A. VS Code + Claude Code** | a paid Claude plan (Pro, Max) or a course/team account | in full: several research streams run in parallel |
| **B. claude.ai — website or Claude app** | a Claude account; per Anthropic's help, skills are available on the free plan too | the same stages, streams run one by one |
| **C. Perplexity — free** | any Perplexity account | the same stages one by one, with Perplexity's web search |

## 🇬🇧 Path A — VS Code + Claude Code

1. **Install VS Code** — [code.visualstudio.com](https://code.visualstudio.com/) and **Git** —
   [git-scm.com/downloads](https://git-scm.com/downloads) (Claude Code fetches the plugin from
   GitHub by cloning; macOS and Linux usually have Git already). No manual project download
   needed: the skill installs as a plugin straight from GitHub.
2. **Register at [claude.ai](https://claude.ai).** Claude Code requires a **paid plan** (Pro or Max)
   or a course/team account; otherwise use path B or C.
3. **Install the Claude Code extension:** Extensions (`Ctrl+Shift+X` / `Cmd+Shift+X`) → **"Claude Code"** → **Install**,
   then sign in through the browser.
4. **Install the skill.** In the Claude Code panel type
   ```
   /plugin install preconstruction --marketplace Barbashin1970/PRECONSTRUCTION
   ```
   and choose **"Install for you"**. On an older version: type `/plugins`, add
   `Barbashin1970/PRECONSTRUCTION` on the **Marketplaces** tab, then **Install** `preconstruction`
   on the **Plugins** tab. Same on Windows, macOS and Linux.
5. **Start:** open any folder, write "research this idea: …" — or call
   `/preconstruction:preconstruction-en` (English report) or `/preconstruction:preconstruction-ru`
   (Russian). The report is saved to the `research/` folder.

## 🇬🇧 Path B — claude.ai (website or Claude app)

1. **Download the skill archive** — don't unzip it:
   [preconstruction-en.zip](https://github.com/Barbashin1970/PRECONSTRUCTION/raw/main/zip/claude/preconstruction-en.zip).
2. **Sign in** at [claude.ai](https://claude.ai) or open the Claude desktop app.
3. **Enable code execution:** **Settings → Capabilities → Code execution and file creation**
   (called **Create and edit files** in the updated settings).
4. **Upload:** **Customize → Skills → "+" → Create skill → Upload a skill** → pick the archive.
5. **Start:** in a new chat write "research this idea: …". The report arrives as a downloadable file.

> Free-plan message limits are lower — pick the "quick" depth for a practice run. Archives
> can't be uploaded from a phone, and Anthropic's help doesn't say whether uploaded skills
> work in the mobile app — check for yourself.

## 🇬🇧 Path C — Perplexity (free)

1. **Register** at [perplexity.ai](https://www.perplexity.ai).
2. **Download the Perplexity archive:**
   [preconstruction-en.zip](https://github.com/Barbashin1970/PRECONSTRUCTION/raw/main/zip/perplexity/preconstruction-en.zip).
   It is a **different** archive from path B: take it from the `perplexity` folder.
3. **Upload:** **Settings → Skills → Create skill → Upload skill** → pick the archive.
4. **Start:** in a new thread write "research this idea: …".

> No Skills section? Create a **Space**, upload the files from the unzipped archive and set
> Custom Instructions to: "Follow the instructions in SKILL.md; the other files are its references."
