# eval_cases_v0 Design Notes

## Overview

8 eval cases grounded in the Intercom corpus (`D:/Evalens/corpus/intercom_external/raw_md/`), designed to expose specific RAG failure modes rather than maximize topic coverage. Cases build directly on the 10 observed behaviors in `manual_eval_seed.md`.

---

## Why Each Case Is Useful

### eval_001 — factual: Pro add-on features
The Pro add-on is a real retrieval trap. The word "Pro" appears in multiple contexts: as an add-on name, as part of feature names (CX Score, Topics), and adjacent to "Expert plan." A system that can't resolve "Pro" to the add-on specifically will either hallucinate a "Pro plan" or return a muddled answer. This is a clean factual anchor — the corpus gives a definitive feature list in `intercom_16_pro_add_on.md`.

**Failure mode tested:** Label disambiguation failure. Model invents a "Pro plan" or conflates Pro add-on features with Fin features because retrieved chunks mix these concepts.

### eval_002 — factual: Early Stage eligibility
Clear, enumerable criteria with no ambiguity in the source. Three hard gates: funding cap, headcount cap, new-customer requirement. This is a positive case — a well-functioning retrieval system should pass it cleanly. Its value is as an easy-to-score baseline for factual grounding.

**Failure mode tested:** Omission of a key criterion (especially the "new customer" requirement), or hallucination of additional criteria (e.g. geography, industry, revenue) not present in the corpus.

### eval_003 — conflict: Fin for Zendesk pricing
The clearest genuine contradiction in the corpus. `intercom_00_pricing.md` implies pure pay-per-outcome pricing ($0.99/outcome, minimums apply, no base fee stated). `intercom_11_fin_for_platforms_explained.md` gives a concrete base subscription model: $49/month includes 50 outcomes, then $0.99 per additional outcome. These are structurally different billing models, not just different prices. A RAG system with k=4 retrieval may surface both, but is likely to blend them into a confident-sounding wrong answer rather than flagging the conflict.

**Failure mode tested:** Confident confabulation from conflicting chunks. System outputs a plausible-sounding price without acknowledging contradictory information.

### eval_004 — conflict: Copilot plan inclusion vs. seat-type exclusion
Directly derived from Cases 4 and 9 in `manual_eval_seed.md` where the system answered "Yes, included in all plans" — an overgeneralization. The conflict is structural: the positive framing ("every plan includes limited Copilot") and the exclusion ("lite seats cannot use Copilot") come from different docs. At retrieval_k=4, whether both surfaces depends on which chunks win the similarity race for this query. The pricing page ($29 vs $35 for unlimited Copilot) adds a secondary pricing discrepancy within the same document — annual vs monthly billing.

**Failure mode tested:** Retrieval of the general affirmative chunk only, leading to a confident but incomplete answer. The system says "Yes" and misses the lite-seat exclusion — observed behavior from the seed.

### eval_005 — oos: Stock price
Confirmed clean OOS from Case 5 in `manual_eval_seed.md`. Observed behavior ("insufficient context") was correct. The eval formalizes this baseline and also tests a retrieval noise problem: the corpus contains many pricing numbers ($0.99, $29, $85) that a noisy retrieval might surface for a "price"-related query. The system must not conflate product pricing with equity market data.

**Failure mode tested:** Retrieval of product-pricing chunks contaminating a market-data query. Or hallucinating a stock price from prior training knowledge.

### eval_006 — oos: Platform uptime SLA
Harder OOS than eval_005 because "SLA" genuinely appears in the corpus (Expert plan feature: "Service level agreements (SLAs)"). Retrieval will surface Expert plan chunks. The system must correctly interpret "uptime SLA" as different from "conversation response-time SLA." This is a semantically ambiguous query that tests whether the system can recognize when retrieved content answers a different question than what was asked.

**Failure mode tested:** Semantic mismatch between query intent and retrieved context. System retrieves relevant-looking SLA chunks and answers a different question than was asked, producing a wrong but confident response.

### eval_007 — caveat: Expert plan at Early Stage discount
The answer is an unambiguous no — `intercom_17_early_stage_program.md` contains an explicit FAQ: "No, the Early Stage program is only available on the Advanced plan... The Early Stage discount does not apply to Expert." The failure mode is a system that retrieves the general discount framing (93%/50%/25% tiers) without surfacing the plan-tier exclusion buried in the FAQ section of the same document. General discount chunks will dominate retrieval; the exclusion clause is a subordinate FAQ entry that may never be fetched at k=4.

**Failure mode tested:** Intra-document retrieval miss. System surfaces prominent general content (discount percentages) from the same document while missing a specific disqualifying clause in a lower-ranked section. Complements eval_008, which tests the new-customer exclusion from the same doc.

### eval_008 — caveat: Early Stage eligibility for existing customers
Tight eligibility question with a binary answer for the specific framing ("paid plan") plus a nearby exception that could contaminate the answer (trial users can apply). The question explicitly states "paid plan" to activate the exclusion. The corpus is clear. The failure modes are: (a) answering "yes" by missing the exclusion, or (b) correctly saying "no" but fabricating reasons not in the corpus.

**Failure mode tested:** Missing explicit exclusion rules in eligibility docs, or failing to distinguish "paid customer" from "trial user" when both appear in the same doc.

---

## Relative Case Strength

### Strongest cases
- **eval_003** (Fin/Zendesk pricing conflict): The genuine cross-doc pricing contradiction is the most valuable case in this set. It will reveal whether the system merges conflicting chunks silently or surfaces uncertainty. High stakes in a real product deployment.
- **eval_004** (Copilot conflict): Directly validated by observed failure in Case 4. High probability of catching the same failure pattern again. Good for regression testing once a fix is attempted.
- **eval_006** (uptime SLA, OOS): Tests semantic disambiguation rather than simple keyword absence. More diagnostic than eval_005.
- **eval_007 + eval_008** (Early Stage caveat pair): Both test intra-document retrieval precision against the same source doc. eval_007 targets the plan-tier exclusion (Expert not eligible); eval_008 targets the customer-status exclusion (existing customers not eligible). Running both together reveals whether failures are random or systematic within that doc.

### Weakest cases
- **eval_005** (stock price, OOS): Already confirmed working. Low diagnostic value beyond serving as a regression anchor. Keep for baseline stability, not signal.
- **eval_002** (Early Stage eligibility, factual): Likely to pass. Useful as a positive case to confirm the system does retrieve cleanly when the answer is well-structured and unambiguous.

---

## Most Useful Corpus Documents

| Document | Cases | Why |
|---|---|---|
| `intercom_00_pricing.md` | 003, 004, 007 | Pricing page — most retrieved doc for price queries. Contains both the Copilot free-access framing and the Fin-for-platforms price (conflict source for eval_003). |
| `intercom_17_early_stage_program.md` | 002, 008 | Dense eligibility and pricing information. Well-structured, low ambiguity. |
| `intercom_16_pro_add_on.md` | 001 | Sole source for Pro add-on features. Unambiguous if retrieved. |
| `intercom_11_fin_for_platforms_explained.md` | 003 | Contains the $49/month base pricing model that conflicts with `intercom_00_pricing.md`. Key conflict source. |
| `intercom_03_pricing_faqs.md` | 004 | Contains the explicit lite-seat Copilot exclusion. Lower retrieval priority than pricing page for Copilot queries — likely to be the missed doc. |
| `intercom_01_plans explained.md` | 004, 007 | Feature comparison table. Contains the full-seat Copilot qualifier. |

---

## Where Contradiction Surfaces Live

1. **Fin for Zendesk pricing** (`intercom_00_pricing.md` vs `intercom_11_fin_for_platforms_explained.md`): The conflict is between "pay per outcome, minimums apply" vs "$49/month for 50 outcomes + $0.99 per additional." Both docs are in the corpus. This is the sharpest contradiction.

2. **Copilot unlimited pricing** (within `intercom_00_pricing.md`): The add-on list shows $29/agent/mo billed annually; the "What is Copilot?" FAQ in the same document says $35/seat/month. Both are correct (annual vs monthly billing) but the document does not explicitly connect them, creating potential confusion.

3. **Copilot access by seat type** (`intercom_00_pricing.md` + `intercom_01_plans_explained.md` vs `intercom_03_pricing_faqs.md`): Positive framing in two docs vs explicit exclusion in the FAQ doc. Classic retrieval precision problem.

---

## Corpus Quality Notes

- **`intercom_04_overview_of_old_legacy_plans.md`** is not from Intercom. It is from a company called "Perspective" (perspective.co) that happens to host its help center on Intercom's platform. The document describes Perspective's own legacy plans (Pro, Business, Advanced) and their new plans (Start, Grow, Expand). This has nothing to do with Intercom's legacy pricing and could contaminate any query about Intercom's historical or legacy plans. Case 10 from `manual_eval_seed.md` ("Can legacy pricing customers use Fin AI Agent?") likely suffered from this noise source.

- **`intercom_02_switch_pricing_legacy_plans.md.md`** covers the "Switch" add-on (calls deflected metric) under Intercom's legacy pricing plans. This is a real Intercom document but covers a narrow, deprecated product. It may contaminate queries about "legacy plans" with irrelevant tiered pricing data ($149, $299, $599...) that applies to a deflection-counting model, not to Fin or current plans.

- The combined effect of docs 02 and 04 means queries about "legacy customers" or "old plans" retrieve a mix of a third-party company's plan structure and a deprecated Intercom add-on pricing table. A case explicitly probing legacy-Fin compatibility (like Case 10) is almost guaranteed to get either a wrong answer or a well-founded abstention, depending on which chunks win retrieval.

---

## Gaps for Later Expansion

1. **Channel-specific Fin behavior**: Does Fin work on WhatsApp the same way as on chat? (Case 6 in manual_eval seed was directionally correct but potentially overgeneralized.) Channel-by-channel capability matrix is a rich area.

2. **Legacy-to-current migration**: What happens if a legacy pricing customer wants to switch to current plans? The corpus has `intercom_02_switch_pricing_legacy_plans.md.md` (Switch add-on) and the Perspective doc (irrelevant), but no direct Intercom doc on legacy-to-current migration. This is a corpus gap.

3. **Fin Voice pricing**: Docs say "custom pricing plan, contact Sales." A question about Fin Voice price is a conditional OOS: in corpus enough to know it exists, not in corpus enough to give a price. Good medium-difficulty OOS case.

4. **Multi-workspace billing**: `intercom_15_how_to_manage_your_intercom_subscription.md` mentions that usage is counted across all workspaces. A question about how multi-workspace billing works could produce answers that are too simplified.

5. **Early Stage + Expert plan**: The corpus explicitly says Early Stage does NOT apply to the Expert plan. A question asking "Can I get the Expert plan at the Early Stage discount?" is a clean caveat case not yet covered.

6. **Fin outcome counting edge cases**: What counts as an outcome vs. not? The definitions appear across multiple docs with slightly different emphasis. A precision question about outcome counting (e.g. "If a customer asks two questions and Fin resolves both, how many outcomes am I charged?") would test whether the system finds the "charged once per conversation" clause.
