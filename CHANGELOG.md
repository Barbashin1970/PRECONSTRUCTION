# CHANGELOG

Версия одна на плагин и оба навыка: `.claude-plugin/plugin.json` и `metadata.version`
в `SKILL.md` (сверяет `tools/check.py`). Пользователи плагина получают правку только
с новой версией.

## 1.1.0 — 2026-11-02

Пакет приведён к требованиям Anthropic и ставится в шесть сред. Разбор —
[docs/PAKET-RAZBOR.md](docs/PAKET-RAZBOR.md).

- Плагин и маркетплейс `.claude-plugin/`: установка одной командой в Claude Code
  на macOS, Windows и Linux.
- Архивы `zip/claude/` (claude.ai, приложение Claude) и `zip/perplexity/`; сборщик
  `tools/build_zips.py`.
- Установщики `install.sh` и `install.ps1`: `~/.claude/skills` и `~/.agents/skills`.
- Навыки: шапка только из полей спецификации, описание `preconstruction-ru` уложено
  в 1024 байта (было 1036); чек-лист фаз; работа в средах без `Agent`
  и `AskUserQuestion`; новый справочник `ai-necessity-criteria.md` вместо ссылки
  на базу знаний; ограничения работы потоков и пометки провенанса; дата отчёта — из среды.
- Сторож `tools/check.py`, три проверки поведения в `evals/`.
- Лицензия: тексты и навыки — CC BY 4.0, код — MIT (`LICENSE-CONTENT.md`, `LICENSE`).

## 1.0.0 — 2026-06-10

Первая версия: навыки `preconstruction-ru` и `preconstruction-en`, база знаний RU/EN,
три эталонных отчёта.
