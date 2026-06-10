---
title: Criteria for Whether AI Is Needed in the Product
description: A key stage of the methodology — an honest assessment of whether AI is needed INSIDE the product. "Built with AI" vs "AI inside".
tags: [preconstruction, ai-necessity, critical-thinking]
---

# Is AI Needed IN the Product? Criteria

This is the **key and most underestimated stage** of presale (stage 4 of the
[5 stages](02-presale-5-stages.md)). The goal is to **honestly** answer whether AI is needed inside the
final product, rather than "how to insert AI in a prettier way".

> **Main principle.** Not all projects must contain AI. Many excellent IT solutions in
> construction **are CREATED WITH AI**, but run on classical technologies.

## The Difference: "Built with AI" vs "AI inside"

| | Created **WITH** AI | Contains AI **INSIDE** |
|---|---|---|
| What it is | You used ChatGPT/Copilot/Cursor to write the code (vibe coding) | ML models, LLM APIs, and embeddings search run in production |
| Final product | A classical application | AI is part of the runtime |
| Example | A cost-estimate calculator written with AI, but computing via formulas | Intelligent search across regulations via embeddings |

Confusing these two things is the root error. At the pitch, the mandatory "AI Applicability" slide
is responsible for this (see [05](05-pitch-packaging.md)).

## When AI Is REALLY Needed in the Product

- Unstructured data: texts, images, video.
- Training on large datasets.
- Recognizing patterns that are hard to formalize with rules.
- Generative tasks (creating content, floor plans).
- Personalization based on user behavior.
- Predictive analytics.

## When CLASSICAL Methods Are Enough

- Clear rules and logic.
- Deterministic computations.
- CRUD operations with a database.
- Simple filtering and sorting.
- Formula-based calculators.
- Aggregation of structured data.

## Honest Assessment Protocol (5 questions)

1. Can the task be solved with **classical** methods (database, rules, algorithms)?
2. If yes — what is the advantage of the AI approach? Is the added complexity justified?
3. If no — which **specific** tasks REQUIRE AI/ML?
4. Distinguish: what to **create** with AI, and what should **contain** AI in the final product?
5. Recommendation: is AI needed in the final product, and in which components?

## Examples of Decisions

| Task | Verdict |
|---|---|
| Parsing documents | WITH AI once → then an ordinary database ✓ |
| Intelligent search across regulations | YES, embedding search with AI is needed ✓ |
| Cost calculator based on parameters | NO, formulas and rules are enough ✓ |
| Generating floor plans | YES, generative AI is needed ✓ |
| Recognizing dimensions on drawings | NO for LLMs → specialized computer vision (see [07](07-case-llm-limits.md)) ✓ |

> At a hackathon, the **honesty** of this assessment is valued most highly, not the "coolness of the AI".
> Admitting that the classical approach is better is a strong move, not a weak one.
