---
title: "Lecture 6. AI in Construction — from Preconstruction to Intelligent Project Delivery"
lecturer: Oleg Barbashin
course: InteRussia 2026 — Smart Cities & AI in Medicine
date: 2026-06-01
support: Gorchakov Fund
lang: en
source: InteRussia Handbook, Chapter 6 (original English lecture; the Russian version is the mirror translation)
---

# Chapter 6. AI for Construction — from Preconstruction to Intelligent Project Delivery

**A lecture by Oleg Barbashin**
*Preconstruction and AI specialist; lecturer at NSU*
*InteRussia fellowship "Smart Cities and AI in Medicine", 1–27 June 2026. Supported by the Gorchakov Fund.*

> Edited and structured version of the sixth chapter of the InteRussia handbook, prepared from Oleg Barbashin's
> lecture on AI in construction. Sections, tables, quotes, and "Further reading" blocks are preserved.

---

## 6.1 Introduction: why AI in construction?

Construction is one of the largest sectors of the global economy, yet it has been depressingly slow to
digitize. That is now changing fast. The market for AI in construction is growing exponentially:
from **$2.28 billion in 2025 to $3.02 billion in 2026** at a compound annual growth rate (CAGR) of **32.8%**,
and it is expected to reach **$9.48 billion by 2030** at a CAGR of 33.1%. Other estimates put the 2026 market
as high as **$12.94 billion**, growing to **$27.92 billion by 2031**.

> *Note: estimates from different agencies differ by several times — this is normal for a young market;
> use them as an order of magnitude, not as precise figures.*

**What is driving this growth:**

- the expansion of large-scale infrastructure projects;
- the adoption of construction management software;
- growing attention to occupational safety;
- increasing project complexity;
- early adoption of BIM (Building Information Modeling);
- smart city initiatives;
- demand for optimizing construction costs.

The lecturer, Oleg Barbashin, brings a unique perspective: he spent **35 years working in construction** — not
building entire cities, but doing **reconstruction** of existing buildings, including more than
**1,000 banks** across Siberia and Moscow. When the construction market changed, he retrained in AI and now
works as a prompt engineer and AI specialist at Novosibirsk State University (NSU), where he teaches courses
on AI. His path from hands-on construction to AI mirrors the very transformation the industry itself is going
through.

**Further reading:**

- *AI in Construction Market Report 2026* — Research and Markets: a full market analysis (250 pp.).
- *AI in Construction Market Trends 2026–2031* — Mordor Intelligence: a breakdown of segments (predictive
  scheduling, AI safety, ROI challenges).
- *Nemetschek AI assistant* (January 2025) — an AI assistant embedded into AEC/O workflows for
  documentation and design coordination.
- *Turner Construction acquires Dornan Engineering* (August 2024) — an acquisition to expand
  AI capabilities in planning, safety, and cost estimation.

---

## 6.2 AI vs. IoT: brain and body

Before talking about AI applications, it is important to distinguish AI from the Internet of Things (IoT):

> "Cameras, sensors, triggers — they're in every corner. That is not artificial intelligence. That is IoT.
> Artificial intelligence is like the brain. IoT is like the hands, the eyes, the ears. They talk to each other."

| Component | Role |
|---|---|
| IoT (sensors, cameras) | Collect data from the physical world (eyes, ears, hands) |
| AI (machine learning models) | Analyze data, recognize patterns, make decisions (the brain) |
| Actuators / transmitters | Carry out actions based on AI's decisions |

Voice assistants like Alexa (or the Russian "Alice") are a clear example: AI recognizes speech,
queries a language model, and returns the answer by voice.

**Further reading:**

- *AI and IoT integration* — a systematic literature review of AI in construction projects (2025).
- *Digital transformation in construction* — how IoT and AI together make the construction site smart.

---

## 6.3 Types of AI: narrow, general, and superintelligence

AI can be pictured in three layers:

| Layer | Description |
|---|---|
| **Weak / narrow AI** | Specialized in a single task (image recognition, text generation, speech recognition). This is exactly what we use in construction today. |
| **General AI (AGI)** | Multi-purpose AI capable of solving any intellectual task a human can. Hypothetical (but actively being worked on). |
| **Super AI** | AI that surpasses humans in all domains. Purely hypothetical. |

This entire lecture is about **weak (narrow) AI** — the only type that is practical and available today.

**Further reading:**

- *Narrow AI in construction* — an analysis of AI use cases in construction by McKinsey (2025).
- *AGI development timelines* — expert surveys and forecasts (2025–2026).

---

## 6.4 How AI learns: levels of learning

Engineers train AI models using several approaches:

| Level | Method | Description |
|---|---|---|
| 1. Supervised learning | Human-labeled data | The model learns from examples with correct answers. |
| 2. Unsupervised learning | Pattern discovery | The model finds hidden structures in unlabeled data. |
| 3. Reinforcement learning | Trial and error | An agent learns from rewards and penalties for its actions. |
| 4. Deep learning | Neural networks | Multilayer networks that learn hierarchical representations. "The king of all learning types." |
| 5. Transformers | Attention architecture | A revolutionary architecture (2017) enabling fast parallel processing. |
| 6. Large language models (LLMs) | Pretrained transformers | Models like GPT, Gemini, DeepSeek — they understand and generate human text. |
| 7. Generative AI | Content creation | Produces new content (text, images, music, designs) from learned patterns. |

**Practical applications in construction:**

- **Computer vision** — safety monitoring and progress tracking on the site;
- **Natural language processing (NLP)** — document analysis and compliance checking;
- **Recommendation systems** — material selection and supplier evaluation;
- **Robots (embodied AI)** — physical tasks on the construction site.

**Further reading:**

- *Transformers in construction* — how attention mechanisms are applied to scheduling and resource allocation.
- *Generative AI for construction design* — a review of text-to-design and image-to-BIM tools.
- *Reinforcement learning for construction robotics* — case studies of RL in automated bricklaying and material handling.

---

## 6.5 Preconstruction: the most important phase

> "70–80% of a project's success is determined at the preconstruction level."

The lecturer illustrated this with a personal story. Having decided to build a wooden house (a dacha), he spent
a whole year studying everything — timber construction, water supply, roofing, pumps. He read books,
studied the codes, and built a 100 m² house out of wood — all through his own research and labor. A neighbor gave
him a key piece of advice:

> "Whatever sum you budget — multiply it by two."

That is the essence of preconstruction: **catch problems before they become expensive mistakes**.

**What is preconstruction?**
In IT, "pre-sales" means understanding what the client needs from an AI system. In construction, "preconstruction"
means understanding what the client wants to build (a school, a stadium, housing) and preparing the entire
analysis, budget, and code compliance check **before construction begins**.

**The five steps of AI-assisted preconstruction:**

| Step | Action |
|---|---|
| 1. Problem research | Understand what is needed. Analyze existing roads, railways, infrastructure. An AI agent finds ideas and materials for you. |
| 2. Competitive analysis | Find out how competitors solved similar problems. Learn from their successes and mistakes. |
| 3. Technical review and code compliance | Check the draft plan against regulations. AI compares the plan with thousands of regulatory documents and produces a checklist of potential violations. |
| 4. AI adoption decision | Decide whether AI is needed inside the building itself (smart systems, IoT, automated controls). |
| 5. Stakeholder pitch | Package the entire study into a clear proposal. Present the plan, risks, and recommendations — sometimes the best decision is **not to build**. |

> "Not every idea becomes a building. Many ideas stay only on paper. You can help your boss save money by
> advising not to build a stadium or a school, because it is too big a risk. Preconstruction helps the
> business save money."

**Further reading:**

- *LeanCon* — an AI team of preconstruction engineers. Cuts planning from months to **seven minutes**
  at 90% accuracy and −20% to timelines. Deployed across development projects worth over $650 million.
  Raised $6 million in seed funding.
- *MeltPlan* — an AI "planning engine" for preconstruction solutions (codes, cost, schedule, value).
  Raised $10 million (round led by Bessemer Venture Partners). Scores 95%+ on building inspector exams.
- *AI agents for pre-construction planning* — an MDPI study (June 2026): accelerating the preconstruction phase
  by **96%**, reducing Work Breakdown Structure creation time from 480 to ~20 minutes.
- *Preconstruction software market 2026–2031* — the market is shaped by rapid consolidation and aggressive AI integration.

---

## 6.6 AI agents and skills: a new paradigm

### What are Skills?

In 2026, the AI landscape has shifted. **Prompt engineering is fading.** The new paradigm is **Skills**:
folders of instructions, scripts, and resources that AI agents discover and apply to solve tasks more
accurately and efficiently.

> "Prompt engineering is the old technique. Skills are the new one. Skills can be assembled for free, and they
> can be improved iteratively — like a snowball that keeps getting bigger."

**Key differences:**

| Prompt engineering (2023–2025) | Skills (from 2026) |
|---|---|
| Improves a single query | Creates reusable packages of capabilities for many tasks |
| Local and tied to the moment | Systematic, scalable, reusable |
| Requires careful phrasing every time | Agents discover and apply skills on their own |
| Human in the loop at every step | Agents execute multi-step scenarios independently |

**The five-step process for creating a skill (per the lecturer):**

1. **Create a base skill** — using Claude Code, turn your knowledge into a skill file.
2. **Run the skill** — task an agent with carrying out research using the skill.
3. **Evaluate quality** — ask the agent to assess the quality of its own result.
4. **Iterate** — repeat 2–3 times; each iteration makes the skill smarter.
5. **Scale** — a manager agent coordinates sub-agents, each with its own specialized skill.

> "You can have one manager skill and five skills beneath it. The manager gathers all the answers,
> audits them, fixes them together, and produces the final report. Every step is inside a single prompt,
> not 100 separate prompts."

### Types of skills (Anthropic's classification)

Anthropic (the creator of Claude) cataloged hundreds of internal skills into nine categories.
The most relevant for builders:

| Skill type | Application in construction |
|---|---|
| Library and API reference | Understanding building codes, regulations, material specifications |
| Data retrieval and analysis | Connecting to project management databases, cost estimation tools |
| Automation scripts | Generating documentation, checking compliance, producing reports |
| Product verification | Verifying that design deliverables meet regulatory requirements |

> "You can take my skill as a base core and keep training your own skill with your own research. In the
> 'weak' field of construction, the quality of the result will grow every time."

**Further reading:**

- *Claude Code Skills* — Anthropic's official documentation and lessons from building hundreds of internal skills.
- *Prompt Engineering Is Fading* — a Hugging Face community article on the shift to skills and frameworks (February 2026).
- *From Prompt Engineering to Skill Engineering* — a Turing Post analysis (SkillOpt, SkillOps, SkillMOO; June 2026).
- *Agent Skills for Claude Code* — a GitHub repository of reusable agent skills.
- *Orchestrator agents* — a PyPI package for coordinating multiple AI agents in parallel.

---

## 6.7 Hallucinations: a critical problem

One of the main problems with AI in construction is **hallucinations**: the model produces a confident but
factually incorrect result.

> "If you read drawings through ChatGPT, it can misread the numbers. The red marks on the image are
> errors, hallucinations. If you use narrow models for documentation, you can get a hallucination.
> ChatGPT is a tool for text, not for image recognition. If you use a smartphone as a hammer — it will break."

**Why hallucinations occur:**

- Early LLMs (2022–2024) had short training and limited reasoning abilities.
- Models confidently "fill in the gaps" when they lack information.
- In agentic systems, early errors cascade and amplify across subsequent steps.

**How to reduce hallucinations (the lecturer's techniques):**

| Technique | Description |
|---|---|
| Reasoning models | Show step-by-step reasoning (for example, DeepSeek R1) |
| Web search with sources | AI searches the web and cites verifiable sources for each claim |
| Reversible dialogue | Ask the model: "How did you find this answer? Describe the steps" |
| Cross-checking with multiple models | Feed one model's answer to another — to find errors |
| RAG (Retrieval-Augmented Generation) | Force AI to ground itself in authoritative databases before answering |

**Recent research (2026):**

| Method | Description |
|---|---|
| CHARM framework | Detects and interrupts the propagation of errors in multi-step pipelines. 89.4% cascade detection, −82.1% error propagation. |
| Hyper-RAG | RAG on hypergraphs: +12.3% accuracy over direct LLM, beats GraphRAG by 6.3%. |
| Graph-based RAG | Halves the number of hallucinations with superior fine-grained fidelity. |
| Binghamton University protocol | Several open-source models are forced to use RAG with authoritative terminology databases. |

**Further reading:**

- *CHARM Framework* (June 2026) — arXiv 2606.04435: detecting and suppressing cascading hallucinations in agentic RAG.
- *Hyper-RAG* (April 2026) — Nature Communications: RAG on hypergraphs for high-stakes applications.
- *Graph-based RAG* (June 2026) — reducing hallucinations in complex questions through graph retrieval.
- *MARCH framework* (March 2026) — multi-agent self-verification with reinforcement against hallucinations.

---

## 6.8 Practical applications in Russian construction

### Document verification (KS-2 acts)

The Russian developer **APRI** (together with Napoleon IT) deployed an LLM-based system for the semantic
comparison of construction documents:

| Metric | Before AI | After AI |
|---|---|---|
| Processing a single KS-2 act | 40–60 minutes | 5–10 minutes |
| Contractor consolidating the final statement | A working day | A few minutes |
| Error detection | Discrepancies were missed | Catches discrepancies not found manually |

In pilot operation, the system uncovered discrepancies in volumes **not detected during manual checking** and
not reducible to typical errors.

> "Construction is one of the largest sectors of the Russian economy, but it lags in document workflow
> automation. This solution is an important step forward."

### Taganrog: the first AI housing construction project

In Taganrog, for the first time in the region, a residential district is being built with AI integration. The
budget is **2 billion rubles over five years**; it uses enterprise AI solutions on the **GigaChat Business**
platform.

- **Two key tasks for the AI agents:** analyzing as-built documentation for errors and defects;
  monitoring the performance of subcontractors' work.
- **Results:** increased labor productivity, minimized time for document checking and quality control.
- **Parameters:** 3 ha, mid-rise development, density up to 12,500 m²/ha, children's and sports areas,
  landscaping. Completion — May 2028.

> "AI gives the technical-inspection engineers and the lawyers the chance to work on real tasks rather than
> routine. The synergy of reliable financing and digital technologies will let us deliver a truly high-quality,
> modern district."

### Nornickel: Russia's first AI system for full industrial design

Nornickel developed and deployed the country's first industry AI system capable of designing entire
industrial buildings — from foundation to roof, including structural solutions and complete sets of documentation.

**System architecture:**

- A base model trained on Nornickel's knowledge base (construction codes, GOST, state standards);
- digital agents process the client's requirements, formulate the technical specification, create the design
  documentation, and populate digital information models;
- sub-agents are launched depending on the building type, checking results against regulatory databases,
  permits, and internal standards at every stage.

**Pilot results:**

| Metric | Improvement |
|---|---|
| Preparing design assignments | −83% time |
| Developing the digital model | −80% time |
| Documentation release timelines | −50% |
| Design team size | From 15–25 down to 5–7 specialists |
| Comments on text documentation | Reduced to zero |

**Further reading:**

- *APRI, LLM document verification* — CNews (April 2026).
- *Taganrog, AI construction* — Mail.ru (May 2026): 2 billion rubles, the GigaChat Business platform.
- *Nornickel, generative AI for industrial design* — press release (May 2026).
- *Nornickel details* — ComNews (May 2026): architecture and pilot results.
- *Glavgosexpertiza AI service* (planned for 2026) — preliminary AI review of design documentation.
- *AI requirements tracing* — Delft University (January 2026).

---

## 6.9 Security and privacy when working with AI agents

A pointed question from a listener: *"Is it safe to enter personal data into AI — document numbers, date
of birth, banking details?"*

The lecturer's answer was categorical: **do not enter sensitive data directly into an AI chat.** His story:

> "I needed to connect two systems via an API. The API required a code of 20–32 characters. I gave that code
> to Claude Code, and it answered me: 'Attention, master. You have given me your code. It is now in the open
> information field. Please, once you close the task, change the code on the server — it is no longer secret.'"

**Security recommendations:**

| Practice | Description |
|---|---|
| Separate sensitive operations | Use AI for the steps and instructions; perform security-critical parts yourself. |
| Use environment variables | Store API keys in server environment variables, not in the chat. |
| Rotate keys | Change codes and passwords after sharing them with AI. |
| Use trustworthy platforms | Claude Code is notable for having dedicated skills for handling client confidentiality. |
| Hybrid approach | Use AI for reasoning and planning; perform sensitive actions in an isolated, secure environment. |

> "Make sure you do not perform security-critical steps inside the chat. The question of security is a
> very interesting and very important one for this session."

**Further reading:**

- *Anthropic security practices* — Anthropic as a leader in AI safety and confidentiality skills.
- *Secure deployment of AI agents* — emerging best practices for enterprise AI security (2025–2026).

---

## 6.10 The human factor: adoption challenges

> "Research shows: about 5–7% of people are always open to new technology. About 50% are mature and ready
> to adopt it with proper support. Some people resist."

**Adoption strategies:**

| Approach | Example |
|---|---|
| Free trial period | Give the system for free for two months. When you announce you'll switch it off — people protest and agree to pay. |
| Training and support | Offer to train the specialists. After training, companies see the need. |
| Focus on pain points | Find a concrete problem (for example, garbage trucks waking residents at 3 a.m.) and solve it with AI. |

**The AI adoption paradox.** The lecturer admitted he is "a very lazy person" who looked to AI in order to work
less. The result is that he now works **12 hours a day**, because the field is incredibly interesting and friends
keep tossing him tasks. *"Be careful. Your working day may become longer, not shorter."*

**Further reading:**

- *Barriers to AI adoption in construction* — high upfront investment and unclear ROI: comprehensive
  deployments often exceed $100,000 before delivering returns, cutting out many subcontractors.
- *Digital-first project delivery* — predictive scheduling is becoming the market baseline.
- *AI safety as a board-level mandate* — CV gates reduce accident rates by 67.5% and insurance payouts by 36.8%.

---

## 6.11 A personal journey: from construction to AI

> "I worked in construction for 35 years, I reconstructed more than 1,000 banks. Then I lost my company and
> spent six months in depression. I found another field — life insurance, and I worked for three years at an
> American company in Novosibirsk. Then I discovered IT, studied, got a diploma, and started working at the university."

His message: **it is never too late to learn.** The AI field is open to people from all walks of life, and
hands-on construction experience provides invaluable domain knowledge that pure AI engineers do not have.

**Career opportunities.** The lecturer noted that countries like Saudi Arabia are actively "hunting" for
qualified AI consultants. His son works in Dubai and has received offers from Saudi Arabia with a substantial
salary increase. At the same time, he warned that the lifestyle (including restrictions and extreme heat) is
not for everyone.

**Further reading:**

- *The AI talent shortage in construction* — the lack of AI-literate specialists as a key constraint.
- *Consultants and systems integrators* — competitiveness increasingly depends on the depth of expertise, not just on "algorithmic power."

---

## 6.12 Conclusion: AI is a tool, not a magic wand

The lecturer's overarching message:

> "AI is a very powerful tool in construction, but it is not magic. ChatGPT is a tool for text.
> If you use it as a hammer — it will break. You need to know a long list of tools in your field
> and apply the right tool to each task."

**The main principle:** even with the most advanced AI systems, the final decision stays with the engineer.
As the Nornickel deployment shows:

> "The final decision still rests with the engineer. The system automates routine, augments expertise, and
> reduces the risk of formal errors, but it does not remove professional responsibility."

**Further reading:**

- *AI workflow automation* — the Nemetschek AI assistant in AEC/O software.
- *Predictive analytics* — halves cost overruns by modeling thousands of schedule variants.
- *AI safety* — CV gates detect missing PPE, dangerous proximity, and equipment failures in real time.
- *Planning and design segment* — led with a 34.92% share in 2025 (generative design −50% to timelines).
- *CIC AI Award* (January 2026); *Daewoo "Hyper Safety & AI"* (May 2026); *Ironsite Hackathon* (May 2026, University of Maryland team, $10,000).

---

## Discussion questions

1. The lecturer claims preconstruction determines 70–80% of a project's success. In your field (smart cities
   or medical AI), what would be the analog of "preconstruction"? How would you improve it with AI?
2. LeanCon cuts planning from months to seven minutes. What are the risks of accelerating decisions so sharply?
   Can it be "too fast"?
3. Hallucinations are especially dangerous in construction (confident but incorrect compliance checks). How would
   you design a verification system for AI-generated construction documentation?
4. Nornickel's AI system cut teams from 15–25 down to 5–7 people. Is this a good thing (efficiency) or a bad one
   (job losses)? How should the industry manage the transition?
5. Skills are displacing prompt engineering in 2026. What skills would you develop in your field?
   How would you "grow the snowball"?
6. The story of the API key leaked into a chat. What security protocols would you put in place before deploying
   AI agents with access to sensitive project data?
7. The high upfront cost of AI (often >$100,000). What is the most economical first step into AI for a
   small construction firm in a developing country?

---

## Key resources summary (Chapter 6)

| Topic | Resource |
|---|---|
| AI in construction market 2026 | Research and Markets / Mordor Intelligence |
| LeanCon (preconstruction) | leancon.ai; $6M, planning in 7 minutes |
| MeltPlan (planning engine) | meltplan.com; $10M, 95% on the inspector exam |
| Claude Code Skills | claude.com/blog/lessons-from-building-claude-code-how-we-use-skills |
| Prompt Engineering Is Fading | huggingface.co/blog/sadpig70/prompting-end |
| Skill engineering (Turing Post) | turingpost.com/p/from-prompt-engineering-to-skill-engineering |
| CHARM Framework (hallucinations) | arXiv:2606.04435 |
| Hyper-RAG (Nature Communications 2026) | nature.com/articles/s41467-026-71411-1 |
| APRI, LLM document verification | tadviser.ru / cnews.ru |
| Taganrog, AI construction | news.mail.ru/society/70959932 |
| Nornickel, AI industrial design | nornickel.com (press release, May 2026) |
| CIC AI Award (Hong Kong) | cic.hk |
| Daewoo Hyper Safety & AI | insightkorea.co.kr (May 2026) |
| AI safety hackathon | cs.umd.edu (May 2026) |

---

*This chapter was prepared from a recording of Oleg Barbashin's lecture during the InteRussia fellowship.
Transcribed, structured, and supplemented with web resources for the fellows. Recording source: "2026-06-09
InteRussia — AI in Smart Cities" (Evgeny Pavlovsky, 2026-06-11). The Russian version is a mirror translation
for the course's Russian-speaking audience.*
