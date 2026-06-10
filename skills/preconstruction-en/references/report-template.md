# Final document template (Phase 3)

Merge audit-confirmed results into one file `research/<slug>-YYYY-MM-DD.md`. Every claim has a
source or an explicit confidence tag (primary / vendor-claim / hypothesis). To chat, surface
Executive summary + Pitch + AI verdict.

```markdown
---
title: Pre-sales study — [idea name]
date: YYYY-MM-DD
type: preconstruction-research
depth: quick | full
---

# Pre-sales study: [idea name]

## Executive summary
- Problem (correct framing): ...
- Solution: ...
- Market: TAM/SAM/SOM ... (range if sources diverge)
- Payable demand (bottom-up: clients × ARPU) proven? yes / no — the main go/no-go
- Verdict on AI inside the product: YES/NO/PARTIAL — why
- Recommendation: build / don't build / build with caveats

## 1. Problem and beneficiaries
[who suffers (incl. the financing side), scale, losses — with sources]

## 2. Business analysis
### Analogues, competitors and incumbents
[direct analogues + incumbents with free/bundled alternatives]
### SWOT
### Market: TAM / SAM / SOM
[top-down + bottom-up; if sources diverge — a range, not one number]
### Monetization / financing models

## 3. Technical feasibility
[stack, ready solutions/platforms, regulations/standards, potential blockers
(privacy, data localization, land/permits), complexity, risks]

## 4. AI applicability (mandatory section)
| Component | Classic possible? | AI inside: YES/NO/PARTIAL | Rationale |
|---|---|---|---|
| ... | ... | ... | ... |
"Built WITH AI" (vibe-coding) vs "contains AI INSIDE" (ML in prod): ...
Product layers: no-AI MVP (classic) → AI modules in phase 2 (under what condition they mature): ...
Final verdict: ...

## 5. Pitch
**Elevator pitch (30s):** ...

[PROBLEM] Who / Suffers from / Scale
[SOLUTION] Essence / How it works / Advantage
[TECH] Stack / AI in product — YES/NO + rationale
[MARKET] TAM-SAM / Monetization / Differentiator
[ROADMAP] Step 1 → Step 2 → Step 3

## Blocking questions (go/no-go)
[blocker facts to close BEFORE committing resources, even if unresolved now:
payable demand (bottom-up), land/ownership, financing, regulation/privacy.
Each — exactly what to verify and where]

## Risks and caveats
[ranked list; vendor-claims tagged]

## Open questions / contradictions
[what didn't reconcile across streams, what to verify next]

## Audit log
- Confirmed: ...
- Rejected / confidence lowered / vendor-claim: ...
- Added after audit (forgotten players/instruments): ...

## Sources
[list; mark primary anchors separately]
```

> Quality criteria (self-check before delivery): correct problem framing; depth across all 5
> stages; grounding in sources (vendor-claims discounted); **bottom-up demand check**;
> **honesty of the AI verdict**; explicit go/no-go blockers; persuasiveness of the pitch.
