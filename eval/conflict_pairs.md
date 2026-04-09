# Evalens — Seeded Conflict Pairs

These are the natural contradictions and tensions in the Intercom documentation corpus that the eval set is designed to expose.

## Conflict 1: Fin for Zendesk pricing (eval_015)
- **Documents:** intercom_00_pricing.md vs intercom_11_fin_for_platforms_explained.md
- **Contradiction:** intercom_00 describes Fin for external helpdesks as $0.99/outcome with a 50-outcome minimum and no base fee. intercom_11 describes a $49/month base subscription including 50 outcomes, then $0.99 per additional outcome.
- **Why it matters:** Different pricing structures that produce different cost totals. A system that quotes one without surfacing the other gives a confidently wrong answer.

## Conflict 2: Copilot plan inclusion (eval_016)
- **Documents:** intercom_00_pricing.md, intercom_01_plans_explained.md vs intercom_03_pricing_faqs.md
- **Contradiction:** intercom_00 and intercom_01 frame Copilot as included on all plans (up to 10 conversations/month). intercom_03 explicitly states lite seats cannot use Copilot. The positive framing omits the seat-type restriction.
- **Why it matters:** A customer on any plan with lite seats would get a misleadingly positive answer if the system only retrieves the first framing.

## Conflict 3: Copilot seat requirement (eval_017)
- **Documents:** Same as Conflict 2
- **Contradiction:** Same underlying tension, tested from a different question angle (access requirement vs. plan inclusion). The system may retrieve the same chunks but the answer framing changes.

## Conflict 4: Fin billing terminology (eval_018)
- **Documents:** intercom_00_pricing.md, intercom_05_fin_ai_agent_explained.md, intercom_06_fin_ai_agent_outcomes.md, intercom_07_fin_ai_agent_faqs.md
- **Contradiction:** The corpus uses "outcome," "resolution," and "per conversation" with overlapping but non-identical meaning. intercom_06 defines outcome as including both Resolutions and Procedure handoffs. intercom_00 uses "per outcome" pricing. intercom_07 says "charged at most once per conversation." A system that answers "per resolution" or "per conversation" without surfacing the definitional layers gives an incomplete answer.
