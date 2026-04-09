Title: Fin AI Agent outcomes

URL Source: https://www.intercom.com/help/en/articles/8205718-fin-ai-agent-outcomes

Markdown Content:
All plans include access to [Fin AI Agent](https://www.intercom.com/help/en/articles/7120684-fin-intercom-s-latest-generation-of-ai-agent). An outcome is counted when Fin successfully delivers value — either by resolving a customer's issue (a **Resolution**) or by executing a Procedure that ends in a handoff to a human or workflow (a **Procedure handoff**). We'll go into what this means and how it's measured below.

## Price per outcome

Fin AI Agent is priced at **$0.99 per outcome** (United States Dollars).

An outcome will be counted when Fin successfully completes the action it was configured to perform, as part of a conversation.

Currently, Fin delivers the following outcomes:
- Resolution: A Resolution is an outcome where the customer confirms Fin resolved the issue or does not request more help after Fin answers.

- Procedure handoff: A Procedure handoff is an outcome where Fin successfully executes a Procedure that you've configured to end in a handoff to a human or a workflow. 

For high-volume pricing or specialized needs, please [talk to Sales](https://www.intercom.com/contact-sales).

Fin is available on every plan, but you won't be billed for Fin if you’re not using it. You can also [set usage reminders and hard limits](https://www.intercom.com/help/en/articles/8991894-how-to-make-the-most-of-your-usage-dashboard#h_36badc7757) to ensure you’re happy with how many resolutions Fin is able to provide.

## Resolution

A resolution is a type of outcome that is counted when, following Fin’s last answer in a conversation, the customer either confirms the answer was satisfactory (confirmed resolution), or exits the conversation without requesting further assistance (assumed resolution).

Customers can confirm a resolution by:

- Entering an affirmative response such as 'Ok thanks', 'That helped' etc.

Customers can request further assistance by:

- Entering a response that indicates their issue is not resolved, such as follow-up questions or requests to speak with a person.

Note: 

An outcome is only counted when Fin provides an actual answer to a customer's query. If Fin merely responds to a greeting, this is not considered an answer and doesn't count towards a resolution.

If a conversation is considered resolved (confirmed or assumed), but the customer later returns to the same conversation seeking further assistance—even across billing periods—that resolution will be deducted and not charged.

## Procedure handoff

A Procedure handoff is a type of outcome where Fin successfully executes a Procedure that you've configured to end in a handoff to a human or a workflow.

You'll only be charged **once per conversation**, even if Fin resolves multiple questions or runs multiple Procedures.

## outcomes billing

This is how you will be charged for outcomes:

Unit price: You will continue to be charged $0.99 (USD) per conversation for outcomes that are either:

- a Resolution, where Fin fully resolves the customer’s issue, or

- a Procedure handoff, where Fin successfully executes a Procedure that ends in a handoff to a human or a workflow.

Charged once per conversation: You will only be charged at most once per conversation, regardless of how many questions the customer asks or how many Procedures Fin runs in that conversation. For example, if a customer asks multiple questions or Fin performs several steps, and Fin resolves the issue (or completes a handoff) by the end of the conversation, it’s still just one outcome charge of $0.99.

Resolution rate metric: Fin’s Resolution Rate (the percentage of conversations that Fin resolves without human involvement) is unaffected by this change. 

No charge for unsuccessful attempts: You will never be charged for an outcome that didn’t happen. If a customer explicitly asks to speak with a human agent at any point, or if a Fin Procedure fails to complete for any reason, it does not count as an outcome and you are not billed for it. We only count outcomes (and charge for them) when Fin actually delivers a successful result. This means you’re never paying for Fin’s “attempts” – only for the outcomes you get.

## How billable outcomes are determined

To understand what you will be charged for it helps to look at what caused the conversation to be passed over to a teammate:

A Procedure handoff occurs when a conversation is passed to a teammate because Fin followed a Procedure's configured instructions or guidance to hand off to a team, teammate or workflow. This is a billable outcome.

An escalation occurs when Fin hands off based on default behavior or workspace rules, such as:

Fin's default behaviour triggers an escalation: if a customer asks for a human or shows frustration, Fin escalates based on its default logic. You are not billed for these escalations.

Fin follows workspace-level escalation rules: When Fin escalates based on global instructions set at workspace level (under Train > Escalation) you are not billed for these escalations.

The table below outlines common conversation scenarios with Fin and whether they are billed as Fin outcomes:

**Scenario****Status****Billed**
Fin handoffs to a human because of instructions you added in [Procedure-specific guidance](https://www.intercom.com/help/en/articles/13449439-building-fin-procedures#h_29d51837fb).Procedure Handoff Yes
Fin uses a configured @handoff to a workflow.Procedure Handoff Yes
Fin uses a configured @handoff to a team or teammate.Procedure Handoff Yes
Fin escalates due to workspace level guidance or escalation rules.Escalated - Not an outcome No
Procedure Failure: A technical error or logic issue prevents a Procedure from finishing.Escalated - Not an outcome No
Standard workflow: Fin will hand over if it's unable to resolve the customer's question, a customer asks for human support, or an escalation rule or guidance applies.Escalated - Not an outcome No

## FAQs

### Can there be multiple outcomes in a conversation?

You will only be billed once per conversation, even if the conversation is reopened or multiple Procedures run.

### What happens if a teammate joins the conversation?

When a teammate joins a conversation where Fin AI Agent is involved:

If the customer has already received an answer from Fin and they haven't explicitly asked to get additional help or speak to a person, the conversation is considered 'resolved' and you would be charged for this.

If the customer has asked to get additional help or speak to a person, the conversation is considered 'unresolved' and you would not be charged for this.

Note: With Conversational Fin, Fin can follow up with a customer after they have been inactive for 4 minutes. This follow up message isn't considered an answer, and doesn't affect whether the conversation is considered resolved or not.

### How do I turn Fin AI Agent off?

To turn Fin off and avoid any charges, simply remove Fin from any live Workflows or pause Fin in the **Simple deploy**section where Fin was set live. This will stop Fin from replying to your customers and resulting in outcomes.

### Are Custom Answers billed as outcomes?

This depends on your current subscription. If you are on one of our [current pricing plans](https://www.intercom.com/pricing), Custom Answers and AI Answers are both billed as resolutions.

### Can I start a free trial of Fin AI Agent?

Yes, new customers can start a 14-day free trial of Fin AI Agent from your workspace. When transitioning from a free trial to a paid plan, you must add a payment method to continue usage. Failure to do so may result in your service being paused.

* * *

💡**Tip**

**Need more help?** Get support from our [Community Forum](https://community.intercom.com/?utm_source=ii-help-center&utm_medium=internal)

Find answers and get help from Intercom Support and Community Experts

* * *

Related Articles

[Deploy Fin AI Agent over chat](https://www.intercom.com/help/en/articles/8286630-deploy-fin-ai-agent-over-chat)[Report on Fin Procedures](https://www.intercom.com/help/en/articles/13170674-report-on-fin-procedures)[Fin AI Agent automation rate](https://www.intercom.com/help/en/articles/13533623-fin-ai-agent-automation-rate)[Troubleshooting Fin Procedures and Data connectors](https://www.intercom.com/help/en/articles/13704396-troubleshooting-fin-procedures-and-data-connectors)[Deploy Fin Ecommerce Agent](https://www.intercom.com/help/en/articles/14420740-deploy-fin-ecommerce-agent)
