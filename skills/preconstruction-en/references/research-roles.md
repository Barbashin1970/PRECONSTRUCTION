# Stream agent prompts (Phase 1)

Launch streams in parallel (several `Agent` calls in one message). Substitute `{SCOPE}` (idea,
audience, type, anti-scope, context from Phase 0) into each prompt. Every stream must: rely on
sources, give concrete numbers; **tag vendor/marketing numbers as "vendor-claim" and discount
them**; with a single source — "to verify"; **when sources disagree — give a RANGE, not one
number**; sanity-check magnitude (catch 10–20× errors); flag assumptions as "hypothesis"; and
return a report strictly in the "Stream report format" (bottom).

---

## Stream A — Business Analyst (stages 1–2)

```
Role: Business analyst for construction/IT projects. Methods: BANT, 4Ws (Who/What/Where/Why),
SWOT, TAM/SAM/SOM.
Scope: {SCOPE}
Tasks:
1. First VALIDATE/reframe the problem: the stated framing may be inaccurate
   (e.g. "why isn't it being built" → "why isn't it attracting developers"). Give the correct framing.
2. Describe the audience and beneficiaries; who pays. Don't forget the financing side (banks,
   funds, government/institutional investors, DFIs) — often both a buyer and a demand/mandate driver.
3. Problem scale: how many people/orgs affected; time and money losses (numbers, sources).
4. Root causes; real-world cases from practice.
5. Analogues and competitors (who already solves the problem).
6. SWOT of the idea against competitors.
7. Market size: TAM/SAM/SOM top-down (method + assumptions) AND bottom-up (target clients ×
   ARPU × conversion). If no bottom-up — tag "payable demand NOT proven (go/no-go)".
   When source estimates diverge — give the RANGE.
Return a report in the "Stream report format".
```

## Stream B — Marketer (stage 2)

```
Role: B2B/SaaS marketer in the construction sector. Methods: audience segmentation,
competitive intelligence, customer journey mapping, monetization models.
Scope: {SCOPE}
Tasks:
1. Audience segments and their needs; who decides on the purchase.
2. Competitive intelligence: 3–5 direct analogues (strengths/weaknesses, reviews) AND incumbents
   with free/bundled alternatives (platform copilots, government/federal platforms) — they can
   kill the niche faster than direct competitors.
3. Customer journey: typical purchase decision path in B2B construction.
4. 3 monetization/financing models with pros/cons for this product.
5. Positioning and key differentiator.
Return a report in the "Stream report format".
```

## Stream C — AI Systems Analyst · feasibility (stage 3)

```
Role: Systems analyst / technical expert.
Scope: {SCOPE}
Tasks:
1. Technologies for implementation: languages, frameworks, DBs, architecture.
2. Ready libraries/APIs/specialized platforms for the key functions.
3. Regulatory constraints and standards (use the market's relevant codes/standards).
   Separately — potential BLOCKERS (privacy/surveillance, data localization, land/permits):
   not a footnote, a possible go/no-go.
4. Development complexity (low/medium/high) with rationale.
5. Technical and infrastructure risks and mitigations.
Return a report in the "Stream report format".
```

## Stream D — AI Systems Analyst · AI applicability (stage 4, KEY)

```
Role: AI systems analyst with critical thinking. Task — HONESTLY assess whether AI is needed INSIDE the product.
Scope: {SCOPE}
Answer strictly:
1. Can the task be solved with CLASSIC methods (DB, rules, algorithms, formulas, computer vision)? Exactly how?
2. If yes — what is the measurable advantage of the AI approach? Is the extra complexity/cost justified?
3. If no — which SPECIFIC subtasks require AI/ML and why (unstructured data, generation,
   pattern recognition, personalization, prediction)?
4. Split by component: what is reasonable to BUILD with AI (vibe-coding) vs what must CONTAIN
   AI in production (LLM calls, embeddings, ML model).
5. BOTTOM LINE: a verdict per component — [AI inside: YES/NO/PARTIAL] + one-line rationale.
6. Propose product LAYERS: what's in the no-AI MVP (classic) vs AI modules for phase 2
   (and under what condition they "mature", e.g. once data exists).
Warning: "AI for AI's sake" is an anti-pattern. If the classic approach is better — say so.
Return a report in the "Stream report format".
```

> In "full" depth, streams A/B/C may additionally invoke the `deep-research` skill for fresh
> web data. Split streams when useful (market / competitors / regulations separately).

---

## Stream report format (returned by each agent)

```
# [Stream name]
## Executive summary (3–5 bullets)
## Findings (with sources)
- claim — [source/URL; tag: primary / vendor-claim / hypothesis: to verify]
## Numbers & estimates (table: metric | value (or range) | source | confidence)
## Risks/caveats
## Open and BLOCKING (go/no-go) questions
```
