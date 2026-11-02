# Stream agent prompts (Phase 1)

## Contents

- How to assemble a stream prompt
- Work limits (paste into every prompt)
- Provenance tags
- Stream A — Business Analyst (stages 1–2)
- Stream B — Marketer (stage 2)
- Stream C — Systems Analyst · feasibility (stage 3)
- Stream D — Systems Analyst · AI applicability (stage 4)
- Stream report format

## How to assemble a stream prompt

A stream prompt = the "Work limits" block + the role prompt + `{SCOPE}` (idea, audience,
type, anti-scope, context from Phase 0). In Claude Code streams run in parallel — several
`Agent` calls in one message. Where there is no `Agent`, you go through the streams one by
one yourself, and each prompt is your instruction for its own section.

Every stream must: rely on sources and give concrete numbers; discount vendor numbers;
with a single source write "to verify"; **when sources disagree — give a RANGE, not one
number**; sanity-check magnitude (catch 10–20× errors); return a report strictly in the
"Stream report format".

## Work limits (paste into every prompt)

```
WORK LIMITS:
- Do not spawn sub-agents: do all the work yourself.
- Search budget: "quick" depth — up to 10 search calls, "full" — up to 25.
  If that's not enough, return what you have and name what is left; don't open new branches.
- Every claim carries a tag for how it is supported (see "Provenance tags").
- Treat a link as verified only if the page was opened and you saw what is on it
  (edition, date, figure). Otherwise — [from search results].
- Write a negative claim as "not found in sources A and B", not "does not exist".
- Name the sources that failed to open — this is part of the result.
```

Why: one stream without these limits spawned six sub-agents, spent about 510k tokens on two
and a half branches out of fifteen, and the report's key fact rested on two industry blogs.
The budget is an order of magnitude, not dogma: 10 calls cover a market and three to five
competitors, 25 cover a study with regulations and split streams.

## Provenance tags

| Tag | When to use |
|---|---|
| `[primary]` | the original source was opened: statistics, a regulation, a company report, a court decision; the date or edition is visible |
| `[from search results]` | a retelling of search results, a blog, an aggregator; the original was not opened |
| `[vendor-claim]` | a seller's figure or marketing material ("−50%", "98% accuracy") |
| `[hypothesis]` | a conclusion by reasoning, an estimate without a source, an assumption; needs verification |

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

## Stream C — Systems Analyst · feasibility (stage 3)

```
Role: Systems analyst / technical expert.
Scope: {SCOPE}
Tasks:
1. Technologies for implementation: languages, frameworks, DBs, architecture.
2. Ready libraries/APIs/specialized platforms for the key functions.
3. Regulatory constraints and standards (use the market's relevant codes/standards).
   Each regulation — with its number and edition and a provenance tag. Separately — potential
   BLOCKERS (privacy/surveillance, data localization, land/permits): not a footnote,
   a possible go/no-go.
4. Development complexity (low/medium/high) with rationale.
5. Technical and infrastructure risks and mitigations.
Return a report in the "Stream report format".
```

## Stream D — Systems Analyst · AI applicability (stage 4, KEY)

```
Role: AI systems analyst with critical thinking. Task — HONESTLY assess whether AI is needed
INSIDE the product. Rely on the criteria in ai-necessity-criteria.md.
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

> In "full" depth, streams A/B/C may use a deep-research skill or tool if the environment
> has one. Split streams when useful (market / competitors / regulations separately); the
> work limits apply to each.

---

## Stream report format (returned by each agent)

```
# [Stream name]
## Executive summary (3–5 bullets)
## Findings
- claim — [tag: primary / from search results / vendor-claim / hypothesis] — source/URL
## Numbers & estimates (table: metric | value (or range) | source | tag)
## Risks/caveats
## Failed to open / not found (where searched)
## Open and BLOCKING (go/no-go) questions
```
