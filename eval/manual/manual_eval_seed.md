# Evalens Manual Eval Seed

## 1. What is Fin AI Agent?
- Category: factual
- Expected behavior: grounded summary from Fin docs
- Observed: mostly good
- Notes: verbose but acceptable

## 2. How much does Fin cost?
- Category: pricing ambiguity
- Expected behavior: should answer with caveats if pricing depends on context
- Observed: gave $0.99 per outcome
- Notes: likely oversimplified / incomplete

## 3. Can I use the Early Stage program with current Intercom plans?
- Category: eligibility / policy
- Expected behavior: grounded answer from Early Stage docs
- Observed: good
- Notes: likely usable as positive example

## 4. Is Copilot included in all Intercom plans?
- Category: plan ambiguity / faithfulness risk
- Expected behavior: should distinguish limits / add-on / plan dependency
- Observed: answered “Yes”
- Notes: likely incorrect overgeneralization

## 5. What is Intercom’s stock price?
- Category: out_of_scope
- Expected behavior: should say insufficient context / not in docs
- Observed: insufficient context
- Notes: acceptable refusal behavior

## 6. Does Fin work on WhatsApp?
- Category: feature support
- Expected behavior: grounded yes/no with channel caveats if needed
- Observed: answered “Yes, Fin works across WhatsApp.”
- Notes: directionally plausible and likely grounded, but answer may overgeneralize support depending on setup / integrations / channel configuration. Good medium-risk faithfulness case.

## 7. Is Fin included in the Pro add-on?
- Category: plan / add-on ambiguity
- Expected behavior: should distinguish Pro add-on reporting features from Fin product availability / pricing
- Observed: answered “No,” and explained that Pro affects reporting, not Fin functionality
- Notes: this is a useful ambiguity test because “Pro” and “Fin” are related in retrieved docs but not the same thing. Likely decent answer, but worth verifying against source docs.

## 8. Can I add my own content to Fin?
- Category: feature capability
- Expected behavior: grounded answer from content/guidance docs
- Observed: answered “Yes,” with specific workflow details for adding internal/public content
- Notes: strong positive retrieval case. Good candidate for a “should pass” eval example.

## 9. Is Copilot an add-on or included by default?
- Category: inclusion ambiguity
- Expected behavior: should distinguish default included usage vs paid expanded / unlimited usage
- Observed: answered that Copilot is included by default in every Intercom plan, with limited usage
- Notes: better than the earlier “included in all plans” answer, but still potentially risky because it compresses default access and paid expansion into one neat statement. Good high-value ambiguity eval case.

## 10. Can legacy pricing customers use Fin AI Agent?
- Category: legacy vs current conflict
- Expected behavior: grounded answer with legacy/current distinction or explicit uncertainty if docs do not support it
- Observed: answered “No information is provided about legacy pricing customers using Fin AI Agent.”
- Notes: this is actually useful boundary behavior. The system resisted making up an answer despite retrieving Fin-related chunks. Good abstention / insufficiency eval case.