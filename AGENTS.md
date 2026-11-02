# AGENTS.md

Instructions for AI coding agents (Codex, Cursor, GitHub Copilot, GigaCode and others)
that open this repository.

- When the user asks to research, validate or package a project idea, size its market,
  check feasibility, or decide whether a product needs AI, follow
  `skills/preconstruction-ru/SKILL.md` (report in Russian) or
  `skills/preconstruction-en/SKILL.md` (report in English). Their `references/` and
  `examples/` folders are the reference files those instructions name.
- Save new reports to `research/<idea-slug>-YYYY-MM-DD.md`.
- `skills/` is the single source. After editing it, run `python3 tools/build_zips.py`
  and `python3 tools/check.py`; the check must print «Расхождений нет.».

Инструкция для ИИ-агентов, открывших репозиторий: исследование идеи ведётся по
`skills/preconstruction-ru/SKILL.md` (отчёт на русском) или `skills/preconstruction-en/SKILL.md`
(на английском); отчёты — в `research/`; после правки `skills/` — сборка архивов и сторож.
