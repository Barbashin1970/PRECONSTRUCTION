# Criteria: is AI needed INSIDE the product (stage 4)

The basis for stream D and for auditing the AI verdict. The goal is to **honestly** answer
whether AI is needed in the running product, not "how to insert AI more prettily". Not every
project must contain AI: many good construction IT solutions are **built WITH** AI but run
on classic technologies.

## "Built with AI" and "AI inside"

| | Built **WITH** AI | Contains AI **INSIDE** |
|---|---|---|
| What it is | code written with ChatGPT, Copilot, Cursor (vibe-coding) | ML models, LLM calls, embedding search run in production |
| Final product | a classic application | AI is part of the runtime |
| Example | a cost calculator written with AI but computing by formulas | search across regulations via embeddings |

Confusing the two is the root error. In the pitch, the mandatory "AI applicability"
section is responsible for it.

## When AI inside is really needed

- unstructured data: texts, images, video;
- training on large datasets;
- recognizing patterns that are hard to write down as rules;
- generation: content, floor plans;
- personalization based on user behavior;
- predictive analytics.

## When classic methods are enough

- clear rules and logic;
- deterministic computations, formula-based calculators;
- CRUD operations on a database;
- filtering, sorting, aggregating structured data.

## Honest-assessment protocol

1. Can the task be solved with **classic** methods (database, rules, algorithms)?
2. If yes — what is the measurable advantage of AI? Is the extra complexity and cost justified?
3. If no — which **specific** subtasks require AI/ML?
4. What to **build** with AI, and what must **contain** AI in the final product?
5. A verdict per component: YES / NO / PARTIAL, and layers — no-AI MVP → AI phase 2 with
   the condition under which the layer "matures" (data, labelling, budget appear).

## Sample verdicts

| Task | Verdict |
|---|---|
| parsing documents into a database | WITH AI once, then an ordinary database |
| meaning-based search across regulations | YES: embedding search |
| cost calculator from parameters | NO: formulas and rules are enough |
| generating floor plans | YES: a generative model |
| dimensions from drawings | NO for LLMs: specialized computer vision |

## LLM limits: the facade drawings case

A construction company wanted bills of quantities from PDF facade drawings. The LLM
"invented" dimensions: numbers merged (`670` and `450` → `670450`), some were lost, and the
facade area could not be computed. The reason: an LLM works with tokens, not with the
geometry of an image, and does no spatial analysis.

| LLMs fit | LLMs don't fit |
|---|---|
| reviews, comparison tables, solution-maturity assessment | exact recognition of dimensions on drawings |
| researching tools and reviews, market research | spatial analysis of geometry |
| subscription payback, scenarios | direct automation of complex technical work |

The right move: the LLM researches and compares specialized platforms (KREO, Togal.AI,
Bluebeam Revu — tag their accuracy figures `[vendor-claim]`), and they are adopted **after
a test on real drawings** — or rejected if not worth it.

> The honesty of this assessment is valued above "AI coolness". Admitting that the classic
> approach is better is a strong move, not a weak one.
