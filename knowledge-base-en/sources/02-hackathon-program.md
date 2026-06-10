---
title: NGUADI Mini-Hackathon Program — AI-Assisted Presale Methodology
description: Complete methodology "Product Management (Presale) of Construction Projects with AI Assistants". 5 stages, 4 agent roles, prompts, criteria.
tags: [preconstruction, methodology, hackathon, source]
source: "Программа очного мини-хакатона для студентов НГАУДИ.docx.pdf"
---

# In-Person Mini-Hackathon Program for NGUADI Students

**Concept:** "Product Management (Presale) of Construction Projects with AI Assistants".

## Key Idea

The event is **not about embedding AI into the final product**, but about how to use AI
**at the research stage (presale)** for elaborating, analyzing, and packaging project ideas.
Many modern IT solutions in construction **are created with the help of AI** (for example,
through vibe coding), but **do not themselves use AI** in the code of the final version.

> **Core message.** AI is a powerful tool for the research and presale stage, not a
> mandatory component of every project.

## Double Presale in IT Projects for Construction

When it comes to IT projects FOR construction (a digital master plan, a GIS platform, a
regulation-analysis system), a **double presale** takes place:

- **Level 1 — presale of the construction solution:** what construction problem are we solving?
  Who is the target audience (urban planners, developers, municipalities)? How does it fit into the construction cycle?
- **Level 2 — presale of the IT solution:** what technical architecture? What technologies?
  **Is AI needed in the product?**

> **Conclusion.** Presale in IT and pre-construction in construction are one and the same
> lifecycle phase under different names. Both include research, design, estimation, and planning
> BEFORE implementation begins.

### Analogy Table: IT Presale ↔ Construction Pre-Construction

| Aspect | IT Project (Pre-Sales) | Construction Project (Pre-Construction) |
|---|---|---|
| Phase name | Pre-Sales / Presale | Pre-Construction / Preconstruction |
| Main goal | Understand the client's requirements, propose a technical solution | Understand the client's needs, create a construction plan |
| Feasibility analysis | Feasibility Assessment (technical feasibility) | Feasibility Study (the expediency of construction) |
| Context research | Analysis of the client's IT infrastructure | Site inspection: territory, soils, ecology |
| Solution design | Solution Architecture: technologies, stack | Design Development: drawings, engineering systems |
| Regulation | Compliance (GDPR, data security) | SP/GOST/FZ (Russian building codes & federal laws), permits |
| Cost/timeline estimation | Estimation: labor effort, timeline | Cost Estimation: budget estimate, schedule |
| Team selection | Composition of the development team | Contractors, engineers |
| Risk analysis | Technical risks, integration risks | Construction risks, natural factors |
| Concept demonstration | POC, product demo | Visualization, mock-ups, 3D models |
| Proposal creation | Commercial proposal, roadmap, budget | Tender documentation: design, estimate, schedule |
| Phase outcome | Development contract → Delivery | Contract with a contractor → Construction |

---

## Event Structure (4–5 hours)

### Block 1. Introduction to AI-Assisted Presale Methodology (60 min)

- **1.1 Opening and context (15 min).** Icebreaker, teams of 5–6 people (8–10 teams).
  Key thesis: "Today we are NOT learning how to embed AI into projects. We are learning how to use AI
  as a product manager's tool at the presale stage — for researching, analyzing, and packaging ideas".
- **1.2 Presentation "The Project Presale Cycle with AI Assistants" (45 min).** The 5 presale stages
  (see below), demonstration on the case "Digital Platform for Analyzing Urban-Planning
  Regulations", an overview of free AI tools, an introduction to Perplexity Spaces.

### Block 2. Self-Assessment of Projects through AI Agents (150 min)

- **2.1 Formulating ideas (20 min).** Each team chooses an idea from
  architecture/construction (2–3 sentences, the level of elaboration does not matter).
- **2.2 Creating a Perplexity Space and loading instructions (15 min).** Loading 4 PDF instructions,
  configuring Custom Instructions for the role-based AI agents, inviting the team into the Space.
- **2.3 Presale analysis through AI agents (90 min).** Teams go through the 5 stages, with a separate
  thread per stage (prompts — see below).
- **2.4 Creating the presentation (25 min).** Gamma.app / Canva / Google Slides + ChatGPT / GigaChat.

### Block 3. Pitches and Feedback (60 min)

- **3.1 Team pitches (40 min).** 5 minutes per team: 4 min presentation + 1 min
  mandatory slide "AI Applicability".
- **3.2 Expert feedback (15 min).** Constructive criticism. Particularly valued are cases
  where a team honestly admitted that the classical approach is better than AI.
- **3.3 Closing (5 min).**

---

## The 5 Presale Stages

**Stage 1. Identifying the problem and opportunity.** What problem does the project solve? Who
are the beneficiaries? AI: market analysis, search for analogs, trends.

**Stage 2. Business analysis.** Analysis of the market and competitors, viability assessment. AI:
parsing of market data, SWOT, financial modeling.

**Stage 3. Technical expertise.** Technical feasibility, regulatory requirements,
tech stack. AI: analysis of regulations, tool selection, feasibility.

**Stage 4. Systematic analysis of AI applicability (KEY).** Is AI needed IN THE PRODUCT ITSELF?
The distinction "created WITH THE HELP OF AI" vs "a product WITH AI INSIDE". When AI is genuinely needed and when it is not.

**Stage 5. Packaging and pitching.** Presentation for stakeholders, value proposition,
visualization. AI: generation of presentations, visualizations, texts.

### Demonstration Case: "Digital Platform for Analyzing Urban-Planning Regulations"

1. **Identification (Perplexity):** "Analyze the problems urban planners face when working with
   regulations in Russia. Find statistics on errors and time costs".
2. **Business analysis (Perplexity):** "Find analogs on the market. Do a SWOT. Estimate the size of the market
   for urban-planning services in the Russian Federation".
3. **Technical expertise (DeepSeek):** "What technologies are used for parsing PDFs with
   regulations? What domestic GIS platforms exist? Analyze FZ-218".
4. **AI applicability (DeepSeek + critique):** "Is AI needed IN THE platform itself, or is a
   classical database with search enough?" → Conclusion: "Parsing can be done WITH THE HELP OF AI
   once, but the platform runs on an ordinary database. AI in the product is needed only for
   intelligent search — optional".
5. **Packaging (GigaChat):** presentation structure, visualizations, elevator pitch.

---

## Prompts by Stage (threads in the Space)

**Thread 1 "Problem Analysis"** (Role: Business Analyst):
> 1. Describe who faces this problem (target audience). 2. Estimate the scale (how many
> people/organizations). 3. Find statistics on time/financial losses. 4. Identify the
> root causes. 5. Provide real cases. Use the file "Инструкция_Бизнес-аналитик.pdf".

**Thread 2 "Market and Competitor Analysis"** (Business Analyst + Marketer):
> 1. Find existing solutions (analogs, competitors). 2. Do a SWOT of our idea against the
> competitors. 3. Estimate the size of the Russian market (TAM, SAM, SOM). 4. Identify potential
> clients. 5. Propose monetization models.

**Thread 3 "Technology Analysis"** (AI Systems Analyst):
> 1. What technologies are needed (languages, frameworks, databases)? 2. What ready-made libraries/APIs exist?
> 3. Regulatory constraints, standards? 4. Development complexity (simple/medium/high).
> 5. Risks of technical implementation.

**Thread 4 "Is AI Needed IN the Product?"** (AI Systems Analyst, critical thinking) — HONESTLY:
> 1. Can the task be solved with CLASSICAL methods (databases, rules, algorithms)? 2. If yes — what
> is the advantage of AI? Is the complexity justified? 3. If no — which tasks REQUIRE AI/ML?
> 4. Distinguish: what should be CREATED with the help of AI, and what should CONTAIN AI in the final product. 5. Recommendation:
> is AI needed in the final solution, and in which components?

Examples of conclusions: "Document parsing — with the help of AI once, then an ordinary database" ✓;
"Intelligent search across regulations — YES, embedding search is needed" ✓; "Cost
calculator — NO, formulas are enough" ✓; "Floor-plan generation — YES, generative AI" ✓.

**Thread 5 "Creating the Presentation"** (Pitch Packager) based on threads 1–4:
> 1. Elevator pitch (30 sec). 2. Structure of a 5-minute presentation: Problem / Solution /
> Why Us / Technology (IS AI NEEDED INSIDE) / Market and Monetization / Roadmap. 3. Key
> slides. 4. Key figures.

---

## Free AI Tools

- **DeepSeek** (free) — technical accuracy, reasoning (DeepSeek-R1), code, mathematics.
  Cons: no voice, no images, basic interface. `deepseek.com`.
- **GigaChat** (free for individuals) — Russian language, construction terminology, context
  of Russian regulations, image generation (Kandinsky) and 12-slide presentations. `giga.chat`.
- **Perplexity** (limited free tier) — search with sources, up-to-date data.
  Free: 5 queries / 4 hours. Available in the Russian Federation. Pro $20/month (GPT-4, Claude). `perplexity.ai`.

### Perplexity Spaces as a Team Collaboration Tool

- Create a Space for the project; load the PDF instructions; set **Custom Instructions** for the
  AI agents (business analyst, marketer, systems analyst); collaborative teamwork.

Example of Custom Instructions:
> "You work in the role specified at the beginning of each query (Business Analyst / Marketer /
> AI Systems Analyst / Pitch Packager). Use the files loaded into the Space as
> reference materials with the methodology. Always: rely on real data (search for sources),
> structure your answers, give concrete recommendations, cite sources".

---

## The 4 PDF Instructions (agent roles)

### 1. Инструкция_Бизнес-аналитик.pdf

- The **BANT** methodology (Budget, Authority, Need, Timing) for qualifying ideas.
- The problem-analysis framework **4Ws** (Who, What, Where, Why).
- Market-analysis prompts, **SWOT** templates, **TAM/SAM/SOM** market-sizing methods.

### 2. Инструкция_Маркетолог.pdf

- Defining the target audience, competitive intelligence, **Customer Journey Mapping**.
- Prompts for finding cases and reviews, SaaS/B2B monetization strategies.

### 3. Инструкция_Системный_аналитик_ИИ.pdf

**Part A — technical expertise:** feasibility assessment, analysis of SP/GOST/FZ, stack selection, risks.

**Part B — criteria for the necessity of AI (CRITICALLY IMPORTANT):**

*When AI is GENUINELY NEEDED in the product:* unstructured data (texts, images,
video); training on large datasets; recognition of patterns that are hard to formalize;
generative tasks; personalization based on behavior; predictive analytics.

*When CLASSICAL methods are enough:* clear rules and logic; deterministic
computations; CRUD; simple filtering/sorting; formula-based calculators; aggregation
of structured data.

*The distinction "With the help of AI" vs "With AI inside":* "With the help of AI" — you used
ChatGPT/Copilot/Cursor to write the code, but the final product is a classical application; "With AI inside" —
ML models, API calls to an LLM, and embeddings search run in production.

### 4. Инструкция_Упаковка_питча.pdf

Structure (Problem-Solution-Market-Tech-Team), elevator pitch (30 sec), storytelling,
visualization, handling objections.

**Pitch template:**
```
[PROBLEM] Who: [target audience]. Suffers from: [problem]. Scale: [figures].
[SOLUTION] We offer: [the essence in 1 sentence]. How it works: [briefly]. Advantage: [vs alternatives].
[TECHNOLOGY] Stack: [technologies]. CRITICALLY: AI in the product — [YES/NO + justification].
  If YES: where exactly and why it is necessary. If NO: how it is solved without AI and why that is optimal.
[MARKET] Size of TAM/SAM. Monetization: [model]. Competitors: [difference].
[ROADMAP] Step 1 → Step 2 → Step 3.
```

---

## Pitch Evaluation Criteria

1. Depth of elaboration (25%) — how all presale stages were covered.
2. Quality of AI-tool usage (20%) — effectiveness of working with Perplexity Spaces.
3. **Critical thinking (20%)** — honesty in assessing the necessity of AI in the product.
4. Presentation and delivery (20%).
5. Practical value of the idea (15%).

> **Important.** What is evaluated is NOT "how cool the AI in the project is", but how
> **well-justified** the decision about the necessity/absence of AI is.

---

## Key Takeaways

1. AI is a research tool, not a mandatory component of every project.
2. Vibe coding: many IT solutions ARE CREATED with the help of AI but run without it.
3. The AI-assisted presale methodology speeds up idea elaboration 5–10x.
4. Perplexity Spaces is a powerful team collaboration tool.

**Before → After:** the focus shifted from "how to embed AI into a project" to "how to use AI to
elaborate an idea at the presale stage"; critical thinking was added (AI is not always needed) and
the distinction between "created WITH THE HELP OF AI" (vibe coding) vs "contains AI INSIDE" (ML in production).

---

## Sources (from the original)

47 links in the source PDF. Key ones: arphie.ai (AI tools for presales); Google Cloud /
kdnuggets / codingscape (vibe coding); arpedio (pre-sales strategy); productschool /
chisellabs (AI tools for PM); Perplexity Spaces (airespo, enterprise videos, student guide);
testfit.io; 3dcityplanner.com; archivinci (AI masterplan).
