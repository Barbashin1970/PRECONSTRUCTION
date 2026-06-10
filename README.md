# PRECONSTRUCTION — ИИ-пресейл для строителей

Методология и инструмент для **качественных пресейл-исследований** строительных и
ИТ-для-стройки идей с ИИ-ассистентами. Собрано из трёх материалов НГУ/НГАУДИ
(см. [knowledge-base/sources/](knowledge-base/sources/README.md)).

> **Главный принцип:** ИИ — инструмент *исследования и упаковки* идеи на стадии
> preconstruction/presale, а **не** обязательный компонент каждого продукта.
> «Создано С ПОМОЩЬЮ ИИ» (вайб-кодинг) ≠ «содержит ИИ ВНУТРИ» (ML в продакшене).

> 🎓 **Слушателям курса / Course students:** пошаговая настройка стенда (2 пути, RU+EN) —
> [STUDENT-SETUP.md](STUDENT-SETUP.md).

## Что внутри

```
PRECONSTRUCTION/
├── knowledge-base/            # 🇷🇺 База знаний: 8 заметок + индекс
│   └── sources/               #   три исходных материала в MD (PDF удалены)
├── knowledge-base-en/         # 🇬🇧 Зеркальная база на английском (для иностранных студентов)
├── research/                  # Отчёты скилла: research/<слаг>-<дата>.md
├── skills/                    # 📦 Навыки (видимая публикуемая папка) — реальные файлы
│   ├── preconstruction-ru/    #   🇷🇺 SKILL.md + references/  → /preconstruction-ru
│   └── preconstruction-en/    #   🇬🇧 SKILL.md + references/  → /preconstruction-en
└── .claude/skills/            # симлинки → ../../skills (чтобы /preconstruction-* находились)
```

- **База знаний** — [knowledge-base/README.md](knowledge-base/README.md) (🇷🇺) и
  [knowledge-base-en/README.md](knowledge-base-en/README.md) (🇬🇧, зеркало для иностранных
  студентов): 5 этапов пресейла, 4 роли-агента, критерии необходимости ИИ, шаблон питча,
  инструменты, уроки, экономика/карьера.
- **Скилл** — диалог с агентом → несколько параллельных потоков-исследователей → аудит их
  отчётов → единый документ с питчем. Две зеркальные версии для разной аудитории (RU/EN).

## Как запустить исследование

В Claude Code из этой папки:

- 🇷🇺 `/preconstruction-ru` — «проработай идею: <короткое описание>»
- 🇬🇧 `/preconstruction-en` — "research this idea: <short description>"

Агент проведёт скоупинг-интервью, запустит потоки (бизнес-анализ, маркетинг, техэкспертиза,
применимость ИИ), проаудирует результаты и соберёт отчёт в `research/<слаг>-<дата>.md`.

---

# PRECONSTRUCTION — AI pre-sales for builders (EN)

Methodology and tooling for **high-quality preconstruction (pre-sales) research** of
construction and construction-IT ideas with AI assistants.

> **Core principle:** AI is a tool for *researching and packaging* an idea at the
> preconstruction/pre-sales stage, **not** a mandatory component of every product.
> "Built WITH AI" (vibe-coding) ≠ "contains AI INSIDE" (ML in production).

**Run a study** from this folder in Claude Code:

- 🇬🇧 `/preconstruction-en` — "research this idea: <short description>"
- 🇷🇺 `/preconstruction-ru` — "проработай идею: <short description>"

The agent runs a scoping interview, launches parallel streams (business analysis, marketing,
feasibility, AI-necessity), audits the results, and consolidates a report into
`research/<slug>-<date>.md`. Knowledge base (English):
[knowledge-base-en/README.md](knowledge-base-en/README.md) — Russian original in
[knowledge-base/](knowledge-base/README.md).

---

> Skill mechanics mirror the **5 pre-sales stages**: identification → business analysis →
> feasibility → **AI applicability** → packaging. Both skills are self-contained
> (own `SKILL.md` + `references/`).
