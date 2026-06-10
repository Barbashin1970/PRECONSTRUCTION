---
title: Lesson — the limits of LLMs (the facade-drawings case)
description: A real case where ChatGPT "invents" dimensions on drawings. Where the boundary of LLM applicability lies and how to use AI correctly.
tags: [preconstruction, lesson, llm-limits, case-study]
---

# Lesson: the limits of LLMs as illustrated by facade drawings

A real case that illustrates the [AI necessity criterion](04-ai-necessity-criteria.md):
**LLMs are good for research, but not for the direct automation of complex technical work.**

## The challenge

A construction company wanted to automatically generate a bill of quantities and materials,
and then cost estimates, from PDF facade drawings. The expectation: upload a drawing → get a
ready-made table of dimensions.

## What happened with ChatGPT

- "ChatGPT version 5 does not recognize all the digits and **invents results**."
- Dimensions merge together, and some numbers are lost. Example: `670` and `450` → `670450`.
- With data like this it is **impossible to calculate the facade area**.

## Why LLMs make such mistakes

- An LLM processes **tokens**, without perceiving the image as an object.
- It does not distinguish the visual boundaries of dimensions and markings.
- It is incapable of **spatial analysis**.
- The result: errors, wasted time, manual checks, and a drop in ROI.

## Where the boundary lies

| An LLM/AI agent is suitable | An LLM/AI agent is NOT suitable |
|---|---|
| Analysis, reviews, assessing the maturity of solutions | Accurate recognition of dimensions on drawings |
| Comparison tables, scenarios, "baskets of solutions" | Spatial analysis of geometry |
| Researching tools, analyzing reviews, best-in-class | Direct automation of complex technical work |
| Calculating the payback period of subscriptions, market research | Tasks that require computer vision |

## How to use AI correctly

1. A prompt engineer describes the business task for the AI agent.
2. The agent conducts **market research**, builds a comparison of solutions (accuracy, price,
   automation), proposes specialized platforms, and justifies their applicability.
3. We obtain a list and a ranking of solutions; we can justify in-house development if no
   analogs exist; we calculate the benefit and **can decline** if it is not worthwhile.
4. Specialized software (KREO, Togal.AI, Bluebeam Revu — see
   [06](06-ai-research-tools.md)) is adopted **after testing on real drawings**.

> **The moral.** ChatGPT is useful for analysis and research, but not for direct automation,
> where specialized technologies (computer vision) and a team of ML engineers are needed.
> This is precisely the practical meaning of the "AI applicability" stage.
