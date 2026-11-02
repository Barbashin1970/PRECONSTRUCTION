# Навыки пресейл-исследования (RU/EN)

Единственный источник двух зеркальных навыков для пресейл-исследования (preconstruction)
строительных и ИТ-для-стройки идей. Формат — открытый стандарт Agent Skills: папка
с `SKILL.md` и справочниками. Отсюда собираются плагин, архивы и установка.

| Навык | Язык отчёта | Вызов в Claude Code |
|-------|-------------|---------------------|
| [`preconstruction-ru/`](preconstruction-ru/SKILL.md) | 🇷🇺 русский | `/preconstruction-ru`, в плагине — `/preconstruction:preconstruction-ru` |
| [`preconstruction-en/`](preconstruction-en/SKILL.md) | 🇬🇧 английский | `/preconstruction-en`, в плагине — `/preconstruction:preconstruction-en` |

В каждом навыке: `SKILL.md`, `references/` (протокол интервью, промпты потоков, критерии
«нужен ли ИИ внутри», чек-лист аудита, шаблон отчёта) и `examples/` (три эталонных отчёта).
Навык самодостаточен: базы знаний и путей вне своей папки не требует.

**Механика:** диалог-скоупинг → потоки-исследователи (бизнес-анализ, маркетинг,
техэкспертиза, применимость ИИ; в Claude Code — параллельно, в чатах — по очереди) →
скептический аудит → единый отчёт с питчем и вердиктом «нужен ли ИИ ВНУТРИ продукта».

**Установка** во все среды — [README в корне](../README.md#установка--выберите-свою-среду).

**Правка.** Правьте здесь: `.claude/skills/` этого проекта — симлинки на эти папки.
После правки — `python3 tools/build_zips.py` и `python3 tools/check.py`; оба навыка
правятся вместе, сторож сверяет их состав. Шапку `SKILL.md` пишите значениями в одну строку
в двойных кавычках и только полями `name`, `description`, `license`, `compatibility`,
`metadata`, `allowed-tools`: другие поля claude.ai и Skills API отвергают.

---

# Pre-sales research skills (RU/EN) — EN

The single source of two mirrored skills in the open Agent Skills format: a folder with
`SKILL.md` and reference files. The plugin, the archives and the installers are built from
here. Each skill is self-contained and needs nothing outside its folder.

**Install** in any environment — see the [root README](../README.md#install--pick-your-environment).
**Edit** here (`.claude/skills/` holds symlinks to these folders), then run
`python3 tools/build_zips.py` and `python3 tools/check.py`.
