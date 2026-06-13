---
title: Glossary — AI in Construction (for international students)
purpose: Core English terms to learn and master so you can discuss AI in construction confidently
lang: en
---

# Glossary: AI in Construction (term + definition + how to use it)

Terms are grouped by topic. The "Note" column explains how and where to use the term, and what to emphasize.
⭐ — covered in the lecture (lock in the meaning and usage); ➕ — gap that adds depth to the topic.

## 1. AI / Machine Learning — the core

| Term | Definition | Note |
|---|---|---|
| ⭐ machine learning (ML) | Systems that learn patterns from data instead of being explicitly programmed | The basic umbrella term for the field |
| ⭐ deep learning | ML based on multi-layer neural networks | Phrase it as "multi-layer neural networks" |
| ⭐ neural network | A model of interconnected layers of artificial "neurons" | Pronounced "NOOR-al"; the building block of deep learning |
| ⭐ supervised / unsupervised / reinforcement learning | Learning from labeled data / from unlabeled data / by trial and error with rewards and penalties | Three learning paradigms; reinforcement = "trial and error, rewards/penalties" |
| ⭐ transformer / attention | The neural architecture (2017) whose attention mechanism weighs how tokens relate to each other | "The architecture behind modern LLMs (2017)" |
| ⭐ large language model (LLM) | A large model trained on text that predicts and generates language | Examples: GPT, Gemini, DeepSeek |
| ⭐ generative AI | AI that creates new content (text, images, code, designs) | Emphasize "creates new content" |
| ⭐ reasoning model | A model that works through a problem step by step before answering | "Shows step-by-step reasoning", e.g. DeepSeek R1 |
| ➕ inference | Running a trained model to produce outputs | "Running the model in production" (as opposed to training) |
| ➕ training / fine-tuning | Building a model from data / adapting an existing model to a specific domain | Fine-tuning = "adapting a model to your domain" |
| ➕ foundation model | A large general-purpose model trained on broad data, reused for many tasks | Like Nornickel's model — trained on building codes and standards |
| ➕ embeddings | Numeric vector representations of meaning | The foundation of semantic search |
| ⭐ RAG (retrieval-augmented generation) | Generation grounded in documents retrieved from a trusted source | "Forces the AI to cite authoritative databases" |
| ⭐ hallucination | A confident but factually wrong model output | "Confident but factually wrong output" |
| ➕ grounding | Tying answers to real sources or facts | The opposite of hallucination; "ground the answer in sources" |
| ➕ agentic AI / AI agent | AI that plans and executes multi-step tasks on its own | "Executes multi-step tasks autonomously" |
| ➕ multi-agent orchestration | Coordinating several specialized agents to solve one problem | The "manager skill + sub-agents" pattern |
| ⭐ prompt engineering | Crafting inputs to steer a model's output | "The older technique" (predates agents/skills) |
| ⭐ skill (agent skill) | A reusable, packaged capability an agent can call | "Reusable capability package" |
| ➕ MLOps | The practice of deploying, monitoring, and retraining models in production | "Deploying, monitoring, retraining models" |
| ➕ model drift | Gradual loss of accuracy as real-world data shifts away from training data | "Accuracy degrades as real-world data changes" |
| ➕ human-in-the-loop | A workflow where a person reviews or approves AI output | "The final decision stays with the engineer" — the key thesis |

## 2. Construction / AEC + AI

| Term | Definition | Note |
|---|---|---|
| ⭐ pre-construction (preconstruction) | The planning and design phase before building starts | Frame it as "the most important phase" |
| ⭐ BIM (building information modeling) | A shared digital 3D model holding all data about a building | Worth expanding — the audience expects depth here |
| ➕ digital twin | A live virtual replica of a physical asset, updated with real data | "Live virtual replica of the asset" |
| ➕ clash detection | Automatically finding where building systems collide in a model | "Finds conflicts between systems in BIM" |
| ➕ quantity takeoff | Measuring how much material and work a project needs | The facade-drawings case study |
| ➕ bill of quantities (BoQ) | An itemized list of quantities and costs for the works | Cost estimate organized by quantities |
| ➕ scan-to-BIM / point cloud | Turning a 3D laser scan (a "point cloud") into a BIM model | Laser scanning of existing buildings — close to a renovation use case |
| ➕ generative design | AI proposing design options that satisfy given constraints | "AI proposes design options under constraints" |
| ➕ 4D / 5D BIM | BIM plus the time dimension (4D) and cost dimension (5D) | Time and money layered on top of the 3D model |
| ⭐ computer vision | AI that interprets images and video | Monitoring PPE and site progress |
| ⭐ PPE detection | Vision AI that checks for required safety gear | Personal protective equipment (helmets, vests) |
| ➕ predictive maintenance | Forecasting equipment failure before it happens | "Predict equipment failure before it happens" |
| ➕ as-built (documentation) | Records of what was actually constructed, vs. the design | "What was actually built" |
| ➕ snagging / punch list | The list of defects to fix before handover | Defects identified before final delivery |
| ⭐ compliance checking | Verifying a design or work against codes and standards | "Against codes/standards" |
| ➕ AEC/O | Architecture, Engineering, Construction & Operations | The full design-build-operate lifecycle |
| ➕ commissioning / handover | Testing and starting up systems, then transferring the asset | The transition into operations |

## 3. Business / pre-sales / project economics

| Term | Definition | Note |
|---|---|---|
| ⭐ pre-sales | The research and packaging done before winning a deal | The IT analogue of pre-construction |
| ⭐ stakeholder | Anyone with an interest in the project's outcome | "Present the pitch to stakeholders" |
| ➕ value proposition | The clear reason a customer should buy | "Why the client should care" |
| ➕ ROI / payback period | Return on investment / time to recover the investment | Spell out "return on investment" |
| ➕ TAM / SAM / SOM | Total / serviceable / obtainable market size | Used to size the market |
| ➕ total cost of ownership (TCO) | The full lifetime cost, not just the purchase price | "Not just the purchase price" |
| ➕ procurement | The process of sourcing and buying goods and services | "Public procurement" = government tenders |
| ➕ subcontractor | A firm hired by the main contractor for part of the work | Often priced out by expensive AI rollouts |
| ➕ scope creep | Uncontrolled growth of project scope over time | The enemy of a tight scope |
| ➕ due diligence | Thorough investigation before committing to a deal | A check done before a deal or build |
| ➕ feasibility study | An analysis of whether a project is worth doing | "Is this worth building?" |

## 4. Useful "lecturer" phrases (for fluent delivery)

| Phrase | How to use it |
|---|---|
| "Let me give you a concrete example…" | Transition into a case study (you have many — good) |
| "The key takeaway here is…" | Highlight the main point |
| "A common misconception is that…" | Bust a myth (AI = magic) |
| "To put this in perspective…" | Give scale to a number |
| "Let's distinguish between A and B" | The "AI vs IoT", "with AI vs AI inside" move |
| "This is where it gets tricky…" | Lead into something hard (hallucinations, security) |
| "Rule of thumb:" | A practical heuristic ("multiply by two") |
| "garbage in, garbage out" | About data quality |

> Common confusions / nuances worth flagging for students:
> - **AI vs IoT:** IoT is sensors and connected devices that *collect* data; AI is the layer that *interprets* and acts on it. They are complementary, not the same thing.
> - **"with AI" vs "AI inside":** using AI as a tool to help build a product is different from a product whose core function *is* an AI model. Ask which one you actually mean.
> - **Weak (narrow) AI vs general AI (AGI):** everything in production today is narrow — good at one task. General AI (human-level across tasks) does not exist yet; don't conflate the two.
> - **ML vs deep learning:** deep learning is a *subset* of machine learning (neural networks with many layers); not all ML is deep learning.
> - **Generative AI vs AI in general:** generation (creating content) is one capability; classification, detection, and prediction are equally "AI".
