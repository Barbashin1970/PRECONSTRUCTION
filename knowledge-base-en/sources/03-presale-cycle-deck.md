---
title: Project Presale Cycle with AI Assistants (presentation + case study)
description: The 5 presale stages + a real case — why ChatGPT does not solve facade-drawing recognition and how AI helps do it the right way.
tags: [preconstruction, presale-cycle, case-study, source]
source: "Пресейл-цикл проекта с ИИ-ассистентами для строителей.pptx.pdf"
---

# Project Presale Cycle with AI Agents for Builders

## Part 1. Presale as the phase BEFORE construction, where millions are saved

Presale (preconstruction) is the stage of research, design, and planning BEFORE construction
begins. **70–80% of a project's success is determined at this stage.** Projects with
high-quality presale: −30% budget overruns, −25% delays. 98% of megaprojects
finish with overruns or delays — and this can be prevented.

**The preconstruction ↔ IT-presale analogy.** In construction: site analysis, drawings, cost
estimate, permits. In IT: infrastructure analysis, technology selection, budget and timeline estimation.

### The 5 presale stages with AI assistants

1. **Problem identification** — who is affected? what is the scale? AI: data search, trend analysis
   (10–20× speedup).
2. **Business analysis** — market, competitors, SWOT. AI: market parsing, financial models,
   monetization models.
3. **Technical expertise** — feasibility, regulations (SP/GOST/FZ (Russian building codes & federal laws)), technologies, risks.
   AI: regulatory analysis, tech-stack selection (10–20× speedup).
4. **AI applicability analysis (critical stage)** — is AI actually needed IN the product? Benefits
   (accuracy, automation, UX) vs. risks (complexity, model training, data dependency).
5. **Packaging into a pitch** — presentation, visualization, elevator pitch, justification to
   management. AI: generating structure and texts (2–3× speedup).

**Part 1 takeaways:** presale is the key stage; AI speeds things up and improves quality; the
IT analogy helps you grasp it; the 5 stages provide a structured approach.

---

## Part 2. A real case: why ChatGPT does not solve automation and how AI helps the right way

### The business challenge

A construction company wanted to speed up the calculation of quantities and cost estimates from
PDF facade drawings using AI: derive a bill of work quantities and materials from the drawings,
then model the estimates. The expectation: upload a drawing → get a ready table of dimensions and
elevation marks.

### What went wrong

The attempt to use ChatGPT led to critical errors:

- "ChatGPT version 5 does not recognize all the digits and makes up results."
- Dimensions are merged, some numbers are skipped. Example of an error: `670` and `450` → `670450`.
- With such results it is **impossible to calculate the facade area**.

### Why LLMs make these mistakes

- ChatGPT processes tokens, not perceiving the image as an object.
- It does not distinguish the visual boundaries of dimensions and markings.
- It is incapable of spatial analysis.
- Result: errors, wasted time, manual checks, reduced ROI.

### How to use AI correctly

AI (LLMs) is excellent for **analysis, reviews, and assessing the maturity of solutions**: it
generates comparison tables, use-case scenarios, "baskets of solutions"; automates research into
new tools, review analysis, best-in-class selection; helps calculate the payback period of paid
subscriptions.

**What the prompt engineer does:** describes the business task for the AI agent.
**What the AI agent does:** conducts market research; produces comparative metrics for
solutions (accuracy, price, automation); proposes specialized platforms and
justifies their applicability.

### The new path — AI agents and prompt engineering

- We formulate case research to find the optimal solution.
- Prompt engineering to analyze off-the-shelf solutions.
- We obtain a list and ranking of solutions fit for the task.
- We can justify the need for in-house AI development if no analogs exist.
- We calculate the benefit and can decline if it is not worthwhile.

**Result:** a ready, structured implementation plan; analysis of accuracy, output format, and
ROI; the ability to immediately test a working product.

---

## Part 3. The presale cycle using this case as an example

1. **Problem identification.** Who is affected: employees manually transferring dimensions from
   drawings into tables and estimates (hours of work + errors); management, owners, clients.
   Scale: manual entry slows the process, errors → overruns and missed deadlines → lost money.
   AI: searching for statistics and cases, estimating economic losses.
2. **Business analysis.** Competitors already use AI, but it is unknown "exactly which one." The
   market offers various solutions; a reliable accuracy assessment requires analysis and tests. AI:
   market parsing, SWOT, calculation of economic benefit.
3. **Technical expertise.** GPT (LLM) failed at accurate dimension recognition.
   The question: where are the specialized solutions? AI: regulatory analysis (SP/GOST), search for proven platforms.
4. **AI applicability analysis.** The critical moment: is AI really needed in the product? Often
   tasks are better solved by classic tools (for example, computer vision), while language models
   are applicable for **research and assessment**. AI: research and generation of
   implementation plans.
5. **Packaging into a pitch.** AI builds the presentation, visualizations, and texts to convey
   the value to management.

---

## Conclusion

- The presale cycle = 5 stages: identification → business analysis → technical expertise → AI applicability → packaging.
- AI helps at every stage, speeding things up and improving quality.
- Assessing applicability is important to avoid excessive solutions.
- **AI speeds up research and decision-making, but is not always suitable for direct
  automation of complex technical work**, where specialized technologies (computer
  vision) and a team of ML engineers are needed.

**Recommendations:**

- Use LLMs/AI agents for market research and tool selection.
- Do not solve technical tasks "head-on" through ChatGPT.
- Deploy specialized software after testing on real drawings from real projects.
- Specialized platforms (for example, **KREO, Togal.AI, Bluebeam Revu**) provide
  accuracy; ChatGPT is useful for analysis and research, but not for direct automation.
