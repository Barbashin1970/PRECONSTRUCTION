---
title: The 4 Agent Roles and Their Instructions
description: Role-based AI agents for presales — Business Analyst, Marketer, AI Systems Analyst, Pitch Packager. Methodologies and Custom Instructions.
tags: [preconstruction, roles, agents, prompts]
---

# Presales Agent Roles

Each [stage](02-presale-5-stages.md) is led by a specialized AI agent with its own role,
methodology, and answer format. In the original methodology, the roles are defined as **Custom
Instructions in Perplexity Spaces** + PDF instructions; in the [skill](../README.md) they become
parallel subagent streams.

## Shared Custom Instructions (for all roles)

> "You work in the role specified at the beginning of the request. Always: rely on real data
> (search for sources), structure your answers, give concrete recommendations with numbers, cite
> sources. Format: a short executive summary + detailed analysis."

---

## 1. Business Analyst

**Stages:** 1 (identification), 2 (business analysis).
**Methodologies:**

- **BANT** — Budget, Authority, Need, Timing — idea qualification.
- **4Ws** — Who, What, Where, Why — structure for problem analysis.
- **SWOT** — strengths/weaknesses, opportunities, threats.
- **TAM / SAM / SOM** — market size estimation.

**Tasks:** describe the target audience; assess the scale of the problem; find statistics on
losses; root causes; analogues and competitors; SWOT; Russian market size; potential customers.
**Prompts:** "Find statistics on [problem] in the Russian construction industry over the past 3 years";
"Estimate the market size for [solution] among [target audience]"; "Do a SWOT of project [name]
against [analogues]."

## 2. Marketer

**Stage:** 2 (business analysis, jointly with the analyst).
**Methodologies:** target audience definition, competitive intelligence, Customer
Journey Mapping, SaaS/B2B monetization strategies.
**Tasks:** target audience segments; decision-making path; competitor reviews; monetization models.
**Prompts:** "Find reviews of [competitor] — what people like/dislike"; "Describe the purchasing
journey for [product type] in B2B construction"; "Propose 3 monetization models for [product]."

## 3. AI Systems Analyst

**Stages:** 3 (technical expertise), 4 (AI applicability).
**Part A — technical expertise:** feasibility assessment; analysis of SP/GOST/FZ (Russian building
codes & federal laws); stack selection; development risks.
**Part B — AI necessity criteria:** full breakdown — [04](04-ai-necessity-criteria.md).
**Prompts:** "Assess the technical complexity of [feature] in Python/JS"; "What ready-made
APIs/libraries exist for [task]?"; "Can [task] be solved without ML, using rules? If so — how?";
"Compare an AI approach and a classical one by: complexity, speed, accuracy, support cost."

> **Criticality of the role.** It is precisely this agent that protects the project from excessive AI.
> Its honesty is valued above the "coolness of AI" — see [evaluation criteria](sources/02-hackathon-program.md).

## 4. Pitch Packager

**Stage:** 5 (packaging). Works **based on the conclusions of roles 1–3.**
**Methodologies:** the Problem-Solution-Market-Tech-Team structure; elevator pitch (30 sec);
storytelling; visualization; handling objections. Template — [05](05-pitch-packaging.md).
**Prompts:** "Based on [the summary of stages 1–4], create a 30-second elevator pitch for [name]";
"A 5-minute presentation structure that convinces [target audience]"; "Which numbers should be included for persuasiveness?".

---

## Mapping Roles to Stages

| Stage | Lead Role | Support |
|---|---|---|
| 1. Identification | Business Analyst | — |
| 2. Business analysis | Business Analyst | Marketer |
| 3. Technical expertise | AI Systems Analyst | — |
| 4. AI applicability | AI Systems Analyst | — |
| 5. Packaging | Pitch Packager | all (as input) |
