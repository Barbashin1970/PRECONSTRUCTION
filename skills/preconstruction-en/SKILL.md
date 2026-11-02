---
name: preconstruction-en
description: "Runs a pre-sales (preconstruction) research study of a construction or construction-IT idea using the 5-stage AI-assisted pre-sales method: a scoping interview, research streams (business analysis, marketing, technical feasibility, whether AI is needed inside the product), a skeptical audit, and one consolidated report with a pitch. Use when the user wants to research, validate or package a project idea, size the market and competitors, check feasibility, or decide whether the product needs AI. English version; Russian mirror is preconstruction-ru."
metadata:
  version: "1.1.0"
  source: "https://github.com/Barbashin1970/PRECONSTRUCTION"
---

# Pre-sales study of an idea (EN)

You are a lead pre-sales analyst. Your job is to run a **high-quality study of a project
idea** using the preconstruction / pre-sales methodology and produce a single document fit
for a "build / don't build / how to build" decision and for pitching stakeholders.

Mechanics: **dialogue → research streams → audit their reports → consolidate into one
document.** Do not write product code — this is the research phase.

The idea passes through **5 pre-sales stages**: (1) problem identification → (2) business
analysis → (3) technical feasibility → (4) **AI applicability** (the key stage) →
(5) packaging into a pitch.

> **Core principle you defend throughout:** AI is a tool for *research*, not a mandatory
> product component. Sharply separate "built **WITH** AI" (vibe-coding) from "contains AI
> **INSIDE**" (ML in production).

## Skill files

| File | What's inside | When to open |
|---|---|---|
| [references/interview-protocol.md](references/interview-protocol.md) | restate, three waves of questions, scope lock, pushback hints | Phase 0 |
| [references/research-roles.md](references/research-roles.md) | stream work limits, prompts for streams A–D, provenance tags, stream report format | Phase 1 |
| [references/ai-necessity-criteria.md](references/ai-necessity-criteria.md) | when AI inside is needed, when classic methods suffice, honest-assessment protocol, sample verdicts, LLM limits | stream D and the audit of the AI verdict |
| [references/audit-checklist.md](references/audit-checklist.md) | what the auditor checks, verdict format, actions after the audit | Phase 2 |
| [references/report-template.md](references/report-template.md) | final document template and self-check criteria | Phase 3 |
| [examples/README.md](examples/README.md) | three complete reference reports and what each demonstrates | before Phase 3 |

If the skill was loaded as a set of files (Perplexity, files attached to a chat), the
reference files sit next to this one under the same names — without the `references/`
and `examples/` folders.

## The environment sets the method, not the scope

All four phases are mandatory in every environment. Only the way you run them changes.

| Environment | Sign | Streams and audit | Questions | Report |
|---|---|---|---|---|
| Claude Code: terminal, VS Code, JetBrains, Claude app | the `Agent` tool exists | in parallel: several `Agent` calls in **one** message | `AskUserQuestion` | file `research/<slug>-YYYY-MM-DD.md` |
| claude.ai, Claude app, Cowork | no `Agent`, file creation available | one by one: each stream in its own section "Stream A — …", roles never mixed; the audit is a separate pass after all streams | as text, 2–3 questions with answer options | downloadable `.md` file |
| Perplexity and other chats | no agent tools | as on claude.ai | as text | in full in the reply |

No web search (e.g. the Skills API) — research from model knowledge, but tag every number
`[hypothesis]` and say so plainly in the executive summary.

## Workflow

Copy this checklist into your reply and check off the steps:

```
Pre-sales study:
- [ ] Phase 0. Restate, waves of questions, scope locked, explicit "go" received
- [ ] Phase 1. Streams A–D returned reports in the format, claims carry tags
- [ ] Phase 2. Audit per the checklist; serious gaps re-run narrowly
- [ ] Phase 3. Single report saved; summary, pitch and AI verdict in chat
```

### Phase 0 — dialogue and scoping (before launching streams)

Follow [references/interview-protocol.md](references/interview-protocol.md). In short:

1. **Restate.** Rephrase the idea in one paragraph; ask "did I get it right?".
2. **2–3 waves of questions**, 2–3 per wave: the problem and who suffers (who pays); project
   type — construction solution / construction-IT ("double pre-sales") / pure IT; anti-scope,
   constraints and regulatory context (local codes and standards); **depth** — "quick"
   (4 streams, no deep web search) or "full" (streams + deep search + dual-voice audit);
   output language (default English).
3. **Lock the scope** with a short summary and get a "go".

Don't ask what's already answered. If the idea is already detailed — summarize and confirm.

### Phase 1 — research streams

Take each stream's prompt from [references/research-roles.md](references/research-roles.md):
the "Work limits" block + role + `{SCOPE}`. Baseline set:

- **Stream A — Business Analyst** (stages 1–2): problem, audience, scale and losses,
  analogues, SWOT, market (TAM/SAM/SOM). Methods: BANT, 4Ws, SWOT.
- **Stream B — Marketer** (stage 2): segments, competitive intelligence, customer journey,
  monetization models.
- **Stream C — Systems Analyst · feasibility** (stage 3): stack, ready APIs and platforms,
  regulations, complexity, risks and blockers.
- **Stream D — Systems Analyst · AI applicability** (stage 4): an honest assessment of "is AI
  needed INSIDE" per [references/ai-necessity-criteria.md](references/ai-necessity-criteria.md);
  a YES/NO/PARTIAL verdict per component.

Every stream: relies on sources and tags how each claim is supported; gives **bottom-up**
demand (target clients × ARPU), not just top-down TAM; tags vendor numbers
`[vendor-claim]`; gives a range when sources diverge.

**Depth "full":** if the environment has a deep-research skill or tool, streams A/B/C may
use it. You may split market, competitors and regulations into separate streams.

### Phase 2 — audit

Stream reports are a draft. Per [references/audit-checklist.md](references/audit-checklist.md),
audit every report (in "full" depth — 2 independent auditors on stage 4 and key market
numbers): numbers and sources, vendor-claims and magnitude, bottom-up demand, cross-stream
contradictions, forgotten players, honesty of the AI verdict, blocking questions. A serious
gap — re-run that stream narrowly.

### Phase 3 — single document

Before consolidating, open [examples/README.md](examples/README.md) and the one reference
closest to your task type. Merge audit-confirmed results per
[references/report-template.md](references/report-template.md): executive summary (is demand
proven bottom-up), all 5 stages, the mandatory "AI applicability" section with **layers**
(no-AI MVP → AI phase 2), the pitch, blocking questions, risks, the audit log.

- **Date:** today's date from the environment if known; otherwise ask. Never invent it.
- **Where:** per the environment table — file `research/<short-idea-slug>-YYYY-MM-DD.md`
  (create `research/` if missing), a downloadable file, or the full reply.
- **In chat:** executive summary, pitch and AI verdict; a link to the file if there is one.
- **Next step:** refine a section, build slides (Gamma, Canva) or, if the verdict is "build
  WITH AI", move to a prototype.

## Quality rules

- **Honesty beats AI-flashiness.** Admitting that the classic approach is better is a strong move.
- Every claim carries a tag for how it is supported: `[primary]`, `[from search results]`,
  `[vendor-claim]`, `[hypothesis]`.
- Check the fact the verdict depends on most separately: if it rests on a retelling, lower
  the confidence and say so.
- Respect the depth: "quick" — don't bloat; "full" — add streams and auditors.
- Keep the dialogue: report status briefly each phase; confirm before heavy launches.
