# SKILL-Preconstruction — навыки пресейл-исследования (RU/EN)

Видимая **публикуемая** папка с двумя зеркальными Claude Code навыками для качественного
пресейл-исследования (preconstruction) строительных и ИТ-для-стройки идей:

| Навык | Язык | Точка входа |
|-------|------|-------------|
| [`preconstruction-ru/`](preconstruction-ru/SKILL.md) | 🇷🇺 русский | `/preconstruction-ru` |
| [`preconstruction-en/`](preconstruction-en/SKILL.md) | 🇬🇧 английский | `/preconstruction-en` |

Каждый навык самодостаточен: `SKILL.md` + `references/` из 4 файлов
(`interview-protocol`, `research-roles`, `audit-checklist`, `report-template`).

**Механика:** диалог-скоупинг → несколько параллельных потоков-агентов (бизнес-анализ,
маркетинг, техэкспертиза, применимость ИИ) → адверсариальный аудит их отчётов → единый
пресейл-отчёт с питчем и вердиктом «нужен ли ИИ ВНУТРИ продукта».

## Как установить в любой проект

Скопируйте нужную папку навыка в `.claude/skills/` вашего проекта (или в
`~/.claude/skills/` для глобального доступа), затем вызовите `/preconstruction-ru`
(или `/preconstruction-en`) в Claude Code. База знаний (`knowledge-base/` и
`knowledge-base-en/`) — опциональный учебник, навык работает и без неё.

## Связь с этим проектом

Это **канонические реальные файлы**. В `.claude/skills/` этого проекта лежат **симлинки**
на эти папки — чтобы Claude Code находил навыки (`/preconstruction-*`), а вы публиковали
видимую `skills/`. Правьте здесь — изменения сразу видны и в `.claude/skills/`.

---

# SKILL-Preconstruction — pre-sales research skills (RU/EN) — EN

Visible, **publishable** folder with two mirrored Claude Code skills for high-quality
preconstruction (pre-sales) research of construction and construction-IT ideas.

| Skill | Language | Entry point |
|-------|----------|-------------|
| [`preconstruction-ru/`](preconstruction-ru/SKILL.md) | 🇷🇺 Russian | `/preconstruction-ru` |
| [`preconstruction-en/`](preconstruction-en/SKILL.md) | 🇬🇧 English | `/preconstruction-en` |

**Mechanics:** scoping dialogue → several parallel research-agent streams (business analysis,
marketing, technical feasibility, AI-necessity) → adversarial audit → one consolidated
pre-sales report with a pitch and an "is AI needed INSIDE the product" verdict.

**Install:** copy a skill folder into your project's `.claude/skills/` (or `~/.claude/skills/`
for global access), then invoke `/preconstruction-en` in Claude Code. These are the canonical
real files; this project's `.claude/skills/` contains symlinks to them.
