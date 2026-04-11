# DECISIONS.md — EVALens Eval Methodology & Gating Rationale

---

## 1. Why These Metrics

### 1.1 The four metrics and what each measures

Evalens uses four DeepEval metrics to evaluate RAG quality. Each measures a different layer of the retrieval-generation pipeline. Ordered here by diagnostic value — the gated metrics first, then the ungated ones.

**Contextual Precision** — Did retrieval return the right chunks? Measures whether the most relevant chunks are ranked highest in the retrieved context. Low precision means retrieval returned noise alongside signal — irrelevant chunks that dilute the useful context the model receives.

**Contextual Recall** — Did retrieval find enough? Measures whether the retrieved context contains the information needed to answer the query. Low recall means retrieval missed key source documents — the answer existed in the corpus but wasn't fetched.

**Faithfulness** — Did the model stick to its sources? Measures whether claims in the generated answer are supported by the retrieved context. A faithfulness failure means the model fabricated information not present in its retrieved chunks — or, as eval_014 revealed, claimed information was absent when it was present.

**Answer Relevancy** — Is the response on-topic? Measures whether the generated response is topically aligned with the query. This is the loosest metric — it checks "is this response about the right topic?" not "does this response actually answer the question?"

### 1.2 Why precision and recall are gated; faithfulness and relevancy are not

Precision and recall showed the strongest separation between known-good and known-bad configurations (see Section 2). They catch retrieval failures — the dominant failure mode in this system.

Faithfulness is not gated because it was too stable across configurations (0.95 vs 0.90) to detect regression. Relevancy is not gated because the delta was too small (0.018) and the metric is too coarse — eval_004 demonstrated that a functionally useless answer scores 1.0 on relevancy simply because it's topically on-target.

### 1.3 What was considered and excluded

**RAGAS composite scores:** Similar underlying metrics, but wraps them in composite scores that obscure which layer failed. For a project demonstrating methodology, per-metric visibility matters more than a single aggregate number.

**Latency:** Infrastructure-dependent and varies by deployment. Quality metrics are invariant to where the system runs.

**Custom metrics** (e.g., contradiction detection, answer completeness): Deferred. The spot-check validation in Section 2 documents where standard metrics fall short — these gaps would inform custom metric design at production scale.

**Raw Precision@k and Recall@k:** DeepEval's contextual variants incorporate the relationship between retrieved context and the expected answer, which is more diagnostic than pure retrieval ranking.

---

## 2. Why These Thresholds

### 2.1 Pre-baseline expectations

Before running any evaluations, I expected precision around 0.60, recall around 0.50, faithfulness around 0.70-0.80 (small model + product documentation = moderate hallucination risk), and relevancy around 0.65. First-principles estimates based on model size (llama-3.1-8b-instant) and corpus characteristics (product documentation with overlapping terminology).

### 2.2 Baseline results

The actual scores were significantly better than expected:

| Metric | Expected | Actual (k=4) |
|--------|----------|--------------|
| Contextual Precision | 0.60 | 0.711 |
| Contextual Recall | 0.50 | 0.834 |
| Faithfulness | 0.70-0.80 | 0.950 |
| Answer Relevancy | 0.65 | 0.888 |

Faithfulness at 0.95 was the biggest surprise. The 8B model stays grounded in its context far more reliably than expected — likely because the system prompt instructs it to say "insufficient context" rather than speculate, and the model follows that instruction consistently.

### 2.3 Calibration method

Thresholds were set by measuring the separation between a known-good configuration (k=4, chunk_size=1000) and a known-bad configuration (k=1, chunk_size=1000). The k=1 configuration removes 75% of the retrieval context, producing measurably worse answers.

| Metric | Baseline (k=4) | Degraded (k=1) | Delta | Threshold | Gated? |
|--------|----------------|-----------------|-------|-----------|--------|
| Contextual Precision | 0.711 | 0.633 | 0.078 | 0.68 | Yes |
| Contextual Recall | 0.834 | 0.706 | 0.128 | 0.75 | Yes |
| Faithfulness | 0.950 | 0.900 | 0.050 | — | No |
| Answer Relevancy | 0.888 | 0.870 | 0.018 | — | No |

**Precision threshold (0.68):** Placed between 0.711 and 0.633 — the midpoint where the gate distinguishes between the two configurations.

**Recall threshold (0.75):** Same logic, placed between 0.834 and 0.706.

**Faithfulness not gated:** Delta of only 0.05. Both configs score above 0.90. A system could degrade meaningfully in retrieval quality while faithfulness remains high, because faithfulness only measures whether the model sticks to whatever context it receives — even if that context is incomplete or wrong.

**Relevancy not gated:** Delta of 0.018 — too small to threshold reliably. Beyond the small delta, the metric is too coarse. eval_004 demonstrated that a functionally useless answer scores 1.0 on relevancy because the response is topically about Intercom plans, even though it provides no substantive answer.

### 2.4 Spot-check validation

I manually read 4 queries near the threshold boundary to validate that metric scores correlate with observable quality differences. Each query's pathology label describes the specific failure mode it was designed to test.

#### eval_004 — Factual / multi_entity_retrieval
**Scores:** P=0.0, R=0.2, F=0.833, AR=1.0

**Query:** "What are the Intercom plans and what does each include?"

The system retrieved pricing FAQs, early stage program, and proactive support add-on — none of which are the plans overview document. Complete retrieval miss. Precision 0.0 and recall 0.2 match my human judgment exactly — no useful chunks were retrieved.

The system hedged appropriately ("the provided context does not explicitly mention...") rather than hallucinating, keeping faithfulness at 0.833. It also surfaced hyperlinks embedded in the corpus markdown files as if they were answers — a common production RAG issue where navigation links in source documents get chunked and retrieved as content.

Answer relevancy scored 1.0 despite the answer being functionally useless, because the response is topically about Intercom plans. **This case illustrates why precision and recall are gated and faithfulness and relevancy are not** — the gated metrics caught the failure that the ungated metrics missed.

#### eval_010 — Caveat / conditional_truth_collapse
**Scores:** P=1.0, R=0.667, F=1.0, AR=1.0

**Query:** "Can I use Fin on WhatsApp if I'm on the Essential plan?"

The system punted entirely: "No information is provided about the Essential plan." The retrieved chunks included relevant Fin channel documentation and the plans explanation page — the information was there.

Recall at 0.667 correctly flags incomplete coverage but is slightly generous — a human would score this lower because the system had relevant context and refused to use it. Precision 1.0 is correct because the retrieved chunks were genuinely relevant.

The pathology is conditional_truth_collapse: the answer depends on combining a channel fact (Fin supports WhatsApp) with a plan fact (WhatsApp is available on Essential), and the system collapsed this conditional into a refusal rather than attempting the combination.

#### eval_013 — Caveat / same_doc_multi_fact
**Scores:** P=0.833, R=1.0, F=0.667, AR=1.0

**Query:** "How much does Copilot cost if I pay monthly versus annually?"

The system retrieved the right document (intercom_00_pricing.md) and reported the $29/month annual price, but stated "there is no mention of a monthly cost for unlimited usage" — when the $35/seat/month figure appears in the same document's "What is Copilot?" FAQ section.

Recall 1.0 means retrieval succeeded. Precision 0.833 is fair. But the answer missed a key fact that was in the retrieved context. Faithfulness at 0.667 correctly flags the false claim that "there is no mention" when there is.

**This illustrates a fundamental limitation:** contextual precision and recall measure retrieval quality, not whether the model uses what it retrieved. A generation failure that retrieval metrics don't capture. In production, this gap would require a separate answer-completeness metric.

#### eval_014 — Synthesis / cross_doc_assembly
**Scores:** P=1.0, R=0.333, F=0.0, AR=1.0

**Query:** "Can I use Fin with unlimited Copilot on the Essential plan?"

The system said "No information is provided about the Essential plan's limitations on Fin or Copilot usage" despite having retrieved the plans explanation and pricing docs — both of which contain relevant information about Essential plan features and Copilot pricing.

Faithfulness 0.0 is correct in a technical sense: the claim "no information is provided" is contradicted by the retrieved context. **But this is not hallucination — it's a false negative,** where the model fails to recognize relevant information in its own context. The metric scores a complete refusal the same as a confident fabrication (both get 0.0), but these are fundamentally different failure modes requiring different fixes.

Recall at 0.333 reflects that only 2 of the 4 needed source documents were retrieved — a compound failure of partial retrieval miss plus a model (llama-3.1-8b-instant, 8B parameters) that defaults to refusal rather than attempting partial synthesis across chunks. In production, separating "made stuff up" from "denied having information it had" would require a coverage or completeness metric.

### 2.5 What would replace this in production

These thresholds are calibrated from the separation between known-good and known-bad configurations, validated by manual spot-checks. They are not derived from user feedback or production failure data. In production, I would replace empirical calibration with:

**User feedback annotation:** Sample production queries, have humans rate responses, correlate ratings with metric scores to find the threshold where "unacceptable" responses cluster.

**Failure triage:** When users report bad answers, run those queries through the eval pipeline, identify which metric would have caught the failure, and calibrate the threshold to catch it.

**Progressive tightening:** Start with loose thresholds, tighten as the system improves, never loosen without justification.

---

## 3. Why DeepEval

### 3.1 The deciding factor

**Pytest-native CI integration.** DeepEval is built on Pytest, which means eval runs produce standard test results that integrate directly into GitHub Actions workflows. The CI quality gate — the headline deliverable of this project — required a framework that could produce pass/fail signals in a CI pipeline with minimal custom wiring. DeepEval's Pytest foundation made this straightforward; alternatives would have required building the CI integration layer from scratch.

### 3.2 Alternatives considered

**DeepEval vs. RAGAS:** RAGAS provides similar RAG-specific metrics (faithfulness, context precision, context recall) but is primarily a scoring library. It would have required more custom wiring to produce pass/fail gates in GitHub Actions. DeepEval's Pytest-native approach means eval results are test results, and CI frameworks already know how to gate on test results.

**DeepEval vs. Evidently:** Evidently is a general-purpose ML monitoring framework covering data drift, model performance, and data quality. Its RAG-specific metrics are less mature than DeepEval's purpose-built ones. Evidently would be the choice if the project scope included production monitoring alongside evaluation. For a project focused specifically on retrieval evaluation and CI gating, DeepEval is a more targeted fit.

**DeepEval vs. custom metrics:** Custom LLM-as-judge prompts could replicate any individual metric. The tradeoff is development time vs. standardization. DeepEval's metrics are documented, versioned, and reproducible. Custom metrics would require maintaining prompt templates and validating scoring consistency across runs. The spot-check validation in Section 2 documents where standard metrics fall short, which would inform custom metric design at production scale.

### 3.3 Judge model selection

**gpt-4o-mini.** At 120 judge calls per eval run, total cost is $0.0234. gpt-4o would cost approximately 10x more with no meaningful improvement in scoring quality at this eval set size.

---

## 4. Why Intercom Docs as Corpus

### 4.1 Selection criteria and process

Three candidate corpora were evaluated — Intercom, Zendesk, and Stripe — against criteria designed for RAG evaluation quality, not general coverage: natural version conflicts, plan-tier ambiguity, clear out-of-scope boundaries, public accessibility, and document extraction quality.

### 4.2 Why Intercom won

**Natural conflict pairs from documentation inconsistencies.** Intercom's documentation contains genuine inconsistencies across documents describing the same concepts. Multiple documents frame Copilot availability differently — the pricing page and plans page say "included on all plans" while the pricing FAQs explicitly exclude lite seats. The Fin outcomes page and the Fin for Platforms page describe pricing for external helpdesks with structurally different models. These are the adversarial eval conditions the project needs — inconsistencies baked into real documentation, not fabricated for testing.

**Strong plan-tier ambiguity.** Intercom has three plans (Essential, Advanced, Expert) with features that differ across tiers, plus add-ons (Pro, Copilot, Proactive Support Plus) with their own pricing models. A question like "Is Copilot included?" has a different answer depending on seat type, plan tier, and whether "included" means "free limited usage" or "unlimited." This ambiguity is what the Caveat and Conflict eval categories are designed to test.

### 4.3 Why not the alternatives

**Zendesk:** Help center uses heavy JavaScript rendering that made automated extraction unreliable. Content quality was good but extraction friction was high.

**Stripe:** Documentation is technically excellent but too clean for eval purposes. Stripe's docs are internally consistent, well-versioned, and rarely contradictory — the conflict and caveat eval categories would have been thin. The eval set needs a corpus where the system can fail in interesting ways.

### 4.4 Corpus composition

**21 local documents** include the pricing page, plans explanation, pricing FAQs, Fin AI Agent documentation (explained, FAQs, outcomes, reporting, guidance, procedures, automation rate), platform integration docs, add-on descriptions (Pro, Copilot, Proactive Support Plus), the Early Stage program, and subscription management.

**1 deliberate noise source:** intercom_04 is an article from Perspective, a company that hosts its help center on Intercom's platform. It describes completely different plans (Pro, Business, Advanced → Start, Grow, Expand) from a different company. I deliberately kept it to test whether retrieval handles irrelevant content — a common production scenario where documentation indexes include third-party or outdated pages. Eval_028 (adversarial/authority_contamination) specifically tests whether the system is confused by this document.

**3 CI smoke documents** are condensed summaries stored in the repository for GitHub Actions runs, covering pricing/plans, Early Stage eligibility, and scope boundaries.

---

## 5. Cost Per Eval Run and Projected Cost at Scale

### 5.1 Actual cost

Each 30-query eval run costs **$0.0234**.

| Component | Cost | Notes |
|-----------|------|-------|
| Judge calls (DeepEval) | $0.0234 | 120 calls, gpt-4o-mini ($0.15/1M input, $0.60/1M output) |
| Generation (Groq) | $0.00 | Free tier, llama-3.1-8b-instant |
| Embeddings | $0.00 | Local SentenceTransformer (all-MiniLM-L6-v2) |
| **Total** | **$0.0234** | |

Cost is dominated by DeepEval's LLM-as-judge calls. Each of the 30 queries is scored on 4 metrics, producing ~120 judge calls.

### 5.2 Projected cost at scale

| Scale | Queries/day | Runs/day | Daily cost | Monthly cost |
|-------|-------------|----------|------------|-------------|
| Current (portfolio) | 30 | 1 | $0.02 | $0.70 |
| Small team (10 PRs/day) | 300 | 10 | $0.23 | $7.00 |
| Medium team (CI on every commit) | 3,000 | 100 | $2.34 | $70.20 |
| Production sampling (5% of traffic) | 30,000 | 1,000 | $23.40 | $702.00 |

At production scale, cost reduction would come from three levers: cheaper judge model (or self-hosted), caching repeated evaluations, and sampling rather than evaluating every query. Even at 1,000 runs/day, eval cost ($23.40/day) is negligible relative to the generation and embedding costs it protects against.

---

## 6. What Would Change at Production Scale

### 6.1 Eval set

30 queries across 7 categories is sufficient for a portfolio project. Production would require 500+ queries built from actual user questions and failure cases. The eval set would be versioned and updated quarterly.

### 6.2 Online monitoring

Current eval runs offline against a fixed eval set. Production would add LLM-as-judge scoring on sampled live traffic (1-5%), with alerts when scores drop below threshold over a rolling window. This catches corpus drift and model degradation that a fixed eval set cannot.

### 6.3 A/B testing

Configuration changes would be tested via A/B experiments with eval metrics as success criteria, not deployed and checked post-hoc.

### 6.4 Eval set maintenance

Queries that consistently score 1.0 are no longer diagnostic and should be replaced with harder cases. Queries where the expected answer has changed need to be flagged and revised.

### 6.5 Separate retrieval and generation evaluation

Current metrics conflate retrieval and generation quality. eval_013 demonstrated this — retrieval succeeded (recall 1.0) but the model failed to use the retrieved information. Production would separate these: retrieval metrics against a retrieval-only endpoint, generation metrics against a generation endpoint with controlled context injection. This isolates which layer is degrading.

### 6.6 User-data threshold calibration

Replace empirical bracketing with thresholds derived from annotated user feedback, where human raters score response quality and the threshold is set where metric scores predict user dissatisfaction.

---

## 7. What Was Deliberately Not Built

**RAG system optimization.** The RAG target exists as a controlled test surface. Bad answers are eval material, not problems to fix. When the system scores 0.0 on faithfulness (eval_014) or misses a $35/month figure in its own context (eval_013), those are exactly the findings the eval methodology is designed to surface.

Langfuse tracing. Eval runs are already observable: per-case scores, retrieved chunks, and cost estimates are logged to JSON on every run. Adding a tracing layer would instrument the same pipeline that the eval results already describe. The signal would be redundant with what run_eval.py already captures.

**Custom UI or dashboard.** Eval results are JSON files compared via CLI. The CI gate and README screenshots communicate the same information more efficiently.

**Fine-tuning.** The RAG target uses llama-3.1-8b-instant via Groq's free tier. The eval layer should work regardless of which model generates answers. A fine-tuned model that scores higher would be a better system, not a better eval.

**Multi-model comparison.** Running the eval set against GPT-4, Claude, and Llama-70b would be a natural extension. Deferred because it multiplies cost without contributing to the CI gating story.

**Custom metrics.** Contradiction detection for conflict pairs, or completeness checking for synthesis queries, would add diagnostic power. Section 2 identifies where these would help: eval_014 showed faithfulness can't distinguish hallucination from false negatives; eval_013 showed retrieval metrics can't catch generation failures. These gaps are the starting point for custom metric development.

---

## Appendix A: Configuration Impact and Chunk Size Findings

### A.1 Three-configuration comparison

Three configurations were tested to validate that the eval distinguishes meaningful regressions from non-impactful changes.

| Config | Precision | Recall | Faithfulness | Relevancy | Gate |
|--------|-----------|--------|-------------|-----------|------|
| Baseline (k=4, chunk=1000) | 0.711 | 0.834 | 0.950 | 0.888 | PASS |
| Degraded retrieval (k=1, chunk=1000) | 0.633 | 0.706 | 0.900 | 0.870 | FAIL |
| Reduced chunking (k=4, chunk=200) | 0.736 | 0.839 | 0.988 | 0.806 | PASS |

### A.2 k=1 — The real regression risk

Dropping retrieval depth from 4 to 1 degraded precision by 0.078 and recall by 0.128. The gate correctly blocked it. This is a blunt degradation — removing 75% of retrieval context — but it validates the core gate behavior: config change → quality drop → merge blocked.

The k=1 regression hit hardest on categories that depend on having multiple relevant chunks: Conflict queries dropped from 0.861 to 0.568 (need chunks from different documents to surface contradictions), and Factual queries dropped from 0.908 to 0.714 (multi-part topics like plan comparisons need broad retrieval coverage).

### A.3 chunk=200 — Not a regression, and the reason is instructive

Reducing chunk size from 1000 to 200 characters did not degrade quality. Precision marginally improved (0.711 → 0.736), recall held steady (0.834 → 0.839), and faithfulness increased to 0.988. Answer relevancy decreased slightly (0.888 → 0.806). The gate correctly passed it.

**Why chunk=200 improved on this corpus:** Intercom's help center articles are written in short, focused sections with clear headings. The baseline chunk_size of 1000 meant each chunk often contained 3-4 unrelated sections concatenated, introducing noise. Reducing to 200 aligned chunks with the natural information boundaries in the source documents — each chunk was more topically focused, and retrieval returned more precise context.

**This finding is corpus-dependent, not universal.** A corpus with long-form narrative content (legal contracts, research papers, policy documents) would likely degrade at chunk=200 because important context would be split across chunk boundaries. Chunk size optimization must be evaluated empirically per-corpus, not set from generic best practices.

### A.4 The meta-finding

The eval distinguishes impactful configuration changes (retrieval depth reduction) from non-impactful ones (chunk size reduction on well-structured documents). A noisy gate would block both changes. A useful gate blocks only the one that actually degrades quality. This is the difference between a gate that enables confident iteration and one that becomes a bottleneck teams learn to work around.

---

## Appendix B: Eval Set Design Philosophy

### B.1 The design framework

The eval set is organized around three questions about how RAG systems fail in production, tested through progressively harder conditions — from ideal retrieval to adversarial attack:

**Question 1 — Can it find the right answer?** These test retrieval and faithfulness when conditions range from ideal to challenging. Factual queries establish the baseline ("here's what it can do when conditions are ideal"). Caveat queries add a condition ("does it still get it right?"). Synthesis queries are the hardest variant ("the answer is spread across multiple documents — can it assemble them?").

**Question 2 — Can it handle bad information situations?** These test what happens when the corpus contradicts itself or doesn't contain the answer. Conflict queries test whether the system notices when its sources disagree, or papers over contradictions. OOS queries test whether the system knows the boundaries of what it knows.

**Question 3 — Can it be trusted in production?** These test behavior under pressure. A system that passes factual and conflict tests but fails safety tests isn't production-ready. Safety queries probe boundaries with PII requests, prompt injection, and ungrounded persuasion. Adversarial queries test robustness when the question itself is the problem — false premises, loaded questions, ambiguous references.

### B.2 Category distribution and pathology labels

| Category | Count | Question | Progression |
|----------|-------|----------|-------------|
| Factual | 7 | Can it answer? | Ideal conditions |
| Caveat | 6 | Can it answer? | First stress test |
| Synthesis | 1 | Can it answer? | Hardest retrieval test |
| Conflict | 4 | Can it handle bad info? | Source disagreement |
| OOS | 4 | Can it handle bad info? | Boundary test |
| Safety | 5 | Can it be trusted? | Trust test |
| Adversarial | 3 | Can it be trusted? | Robustness test |
| **Total** | **30** | | |

Each query is also tagged with a pathology label describing the specific failure mechanism it targets (e.g., conditional_truth_collapse, cross_doc_assembly, authority_contamination, pii_fabrication). These are more diagnostic than category labels alone — they identify the mechanism of failure, not just the topic area. Pathology-level scores in the results JSON allow tracking whether specific failure modes improve or regress across configurations. The `analyze_pathology.py` script surfaces these scores as a formatted breakdown, grouping DeepEval results by failure mechanism rather than question type.

### B.3 Category-level scores validate the progression

| Category | Avg Score | Interpretation |
|----------|-----------|---------------|
| Factual | 0.908 | Performs well under ideal conditions |
| Caveat | 0.957 | Conditional reasoning is strong on this corpus |
| Synthesis | 0.771 | Cross-document assembly is a clear weakness |
| Conflict | 0.861 | Handles some contradictions, misses others |
| OOS | 0.812 | Boundary recognition is adequate |
| Safety | 0.696 | Lowest — expected for boundary-probing queries |
| Adversarial | 0.722 | Robustness degrades under adversarial inputs |

The progression from Factual (0.908) to Safety (0.696) validates the eval set design: scores degrade predictably as conditions move from ideal retrieval through information problems to active boundary probing.

### B.3a Pathology-level findings

Category averages mask per-pathology variation. Within Factual (avg 0.908), `multi_entity_retrieval` scored precision 0.000 / recall 0.200 while `clean_retrieval_baseline` scored 0.979 / 0.917 — a 0.979-point precision spread inside a single category, driven by fundamentally different retrieval requirements (one document vs. an implicit multi-document join across plan tiers).

The k=1 regression was not uniform across pathologies. Multi-document pathologies degraded most: `framing_dependent_conflict` collapsed from precision 0.542/recall 0.833 to 0.000/0.000 (Δprec=−0.542, Δrecall=−0.833), and `cross_doc_contradiction` lost all recall (0.500→0.000, Δrecall=−0.500) while precision held — retrieving only one chunk is often sufficient to find a number, but never sufficient to surface a contradiction between two sources. `cross_doc_assembly` was already degraded at baseline (recall=0.333) and held there under k=1, suggesting its single test case consistently surfaces the same top chunk regardless of retrieval depth. Single-document pathologies like `conditional_truth_collapse` (Δprec=0.000, Δrecall=0.000) and `cross_doc_retrieval` (Δprec=0.000, Δrecall=0.000) were unchanged — when one chunk contains the full answer, reducing k from 4 to 1 costs nothing.

Per-pathology gating becomes viable at 500+ eval entries, where each pathology has enough cases to produce stable threshold estimates. With sufficient volume, thresholds would be calibrated per failure type rather than as a single aggregate gate — a `framing_dependent_conflict` threshold set near 0.54 would catch a regression that a blended precision threshold of 0.68 might absorb.

```
python eval/analyze_pathology.py eval/results/baseline_results.json
```
