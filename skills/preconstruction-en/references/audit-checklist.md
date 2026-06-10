# Audit checklist (Phase 2)

Stream reports are a draft, not truth. Launch auditor streams (one per report; in "full" mode,
2 independent auditors on stage 4 and on key market numbers). The auditor is **skeptical**: by
default, treat a claim as unproven until confirmed.

## What the auditor checks

1. **Numbers and facts.** Does each number have a source? Did the LLM fabricate it? (Special
   risk — precise numbers without a citation; see the LLM-limits lesson in the knowledge base.)
2. **Vendor-claims and sanity.** Is the number independent/primary or vendor/marketing? Discount
   vendor-claims (effects like "−50%", "98% accuracy" are usually marketing). Sanity-check
   **magnitude**: catch gross 10–20× errors (a common failure — market/volume off by an order).
3. **Source spread.** If estimates diverge — the report must show a range, not one "confident"
   number. Divergence by multiples = low confidence.
4. **Sources.** Are links real and relevant? No swapping "sounds plausible" for "verified"?
5. **Cross-stream contradictions.** Compare A↔B↔C↔D. E.g. "huge market" (B) vs "not feasible
   under codes/economics" (C); "AI needed" (client wish) vs "classic is better" (D).
6. **Bottom-up demand.** Is payable demand proven BOTTOM-UP (target clients × ARPU × conversion)
   or only top-down TAM? **Top-down without bottom-up = commercial thesis unproven (the main go/no-go).**
7. **Gaps and forgotten players.** Audience unaddressed (incl. the financing side)? An incumbent
   with a free/bundled alternative, a government/federal platform, an adjacent instrument forgotten? No anti-plan?
8. **AI-applicability verdict (stage 4).** Re-check for honesty: no "AI for AI's sake"; are "with
   AI" and "AI inside" separated; is each YES/NO justified; are layers proposed (no-AI MVP → AI phase 2)?
9. **Blocking (go/no-go) questions.** Are blocker facts surfaced explicitly even if unanswered
   (land/ownership, financing, regulation/privacy, payable demand)? They must be a separate
   section, not dissolved into the text.
10. **Problem framing and scope.** Is the problem framing correct (not substituted)? Any scope
    drift (another topic bleeding into a stream)?

## Auditor verdict format

```
# Audit: [which report]
## Confirmed (usable as is)
- ...
## Doubtful / needs fixing
- claim — reason — action (re-verify / lower confidence / remove / vendor-claim)
## Rejected (not supported)
- claim — why
## Missing (add to research)
- ... (incl. forgotten incumbents/instruments, the financing side)
## Blocking (go/no-go), left unresolved
- ...
## Contradictions with other streams
- ...
```

## Actions after the audit

- Serious gap/error → re-run the relevant stream narrowly with a refined prompt.
- Cross-stream contradiction → put it in the final doc's "Open questions" and, if critical,
  resolve it (which source carries more weight and why).
- Lower the confidence of unconfirmed numbers; tag and discount vendor-claims explicitly.
- Unresolved blockers → into the final doc's "Blocking questions (go/no-go)" section.
