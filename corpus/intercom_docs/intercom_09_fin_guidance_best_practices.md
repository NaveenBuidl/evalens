Title: Fin Guidance best practices

URL Source: https://www.intercom.com/help/en/articles/10560969-fin-guidance-best-practices

Markdown Content:
[Fin Guidance](https://www.intercom.com/help/en/articles/10210126-provide-fin-ai-agent-with-specific-guidance-beta) allows you to fine-tune how Fin responds to customers - whether that’s how it speaks, how it asks follow-ups, when it escalates, or which content it prioritizes. This ensures its answers are accurate, on-brand, and aligned with your support policies.

Fin uses its language model to make a judgment call on whether to follow a guidance instruction to get the best results, the clarity and precision of your wording are crucial. To get the best results, follow these best practices when writing guidance for Fin.

### What can I use Guidance for?

Guidance is perfect for shaping Fin's personality and directing its actions in key situations.

Some common examples include:

## Fin Guidance best practices

## Start with the outcome in mind

Before writing Fin Guidance, consider the **specific result** you want to achieve. Work backward from this goal to create clear, actionable instructions.

❌ **Bad example (vague and ineffective):**

“Make sure Fin understands our different product types before answering.”

✅ **Good example (clear and structured):**

“If a customer asks about the ‘search’ feature, first ask which product they are using before responding. Then, provide product-specific instructions based on their answer.”

By structuring guidance with clear steps and conditions, Fin can apply it consistently and correctly.

## Use simple and precise language

Ambiguous or overly complex Fin Guidance can lead to inconsistent responses. Write as if you’re training a new support agent—be **direct, specific, and easy to understand**.

❌**Bad example (unclear and open to interpretation):**

“Fin should be professional but also friendly, keeping responses engaging.”

✅ **Good example (defined and actionable):**

“Use a professional yet approachable tone. Keep responses concise, avoid jargon, and use reassuring language when addressing customer frustrations (e.g., ‘I understand how that can be frustrating. Here’s how we can resolve it’).”

## Provide context and concrete examples

Fin performs best when it understands when and how to apply guidance. Use words like “if,” “when,” and “then” to define conditions, and include clear examples.

**❌ Bad example (lacks context):**

“When customers ask about pricing, make sure Fin answers correctly.”

✅**Good example (context-driven and detailed):**

“If a customer asks about pricing, first check if they mention a specific plan. If they don’t, ask which plan they’re interested in before providing details. Always refer to prices as ‘starting at [lowest tier price]’ unless the customer specifies a plan.”

## Create separate, focused guidance

Each piece of Fin Guidance should address a single objective. Avoid mixing multiple instructions, as this can make it harder for Fin to apply them correctly.

**❌ Bad example (too broad and unfocused):**

“Fin should use a friendly tone, clarify questions before answering, and escalate billing issues to an agent.”

**✅ Good example (one clear purpose per entry):**

## Write a descriptive title

A good title should summarize the purpose of the guidance, making it easy for you and your team to understand what each piece of guidance does at a glance. For example, instead of a generic title like "Greeting," use something more specific like "Greeting for VIP Customers."

## Speak directly to Fin in your guidance

When writing Fin Guidance, avoid referring to Fin in the third person or commenting on how it should modify its responses. Instead, write as if you are speaking directly to Fin, telling it exactly what to do.

**❌ Bad example (third-person and indirect):**

_“If the AI answer tells the customer to uninstall and reinstall the app, then rewrite the answer to remove that information, as reinstalling is not a valid troubleshooting step.”_

**✅ Good example (direct and actionable):**

_“Never tell the customer to uninstall and reinstall the app. Reinstalling is never a valid troubleshooting step, and you should never communicate this to the customer.”_

## Address Fin as 'you'

The most effective guidance is written as a direct command to Fin. You should always address Fin as “you” in your instructions.

**❌ Bad example:**

_"Fin should escalate when a customer mentions a refund."_

**✅ Good example:**

_"When a customer mentions a refund, you should escalate to the support team."_

## Give complete instructions

Always write a full, complete command rather than a fragment. Fin doesn’t have the context of a user interface, so it relies on your instructions to know what action to perform.

**❌ Bad example:**

_"When a customer mentions refunds."_

**✅ Good example:**

_"Escalate when a customer mentions refunds."_

## Be concise and clear

Keep your guidance short and to the point. Avoid complex instructions with multiple "and/or" conditions, as this can make the guidance unreliable. It's better to create several simple rules than one complex one.

**❌ Bad example:**

_"When someone mentions refunds and would like to return their purchase or would like to do an exchange, escalate immediately."_

**✅ Good example:**

_"When a customer would like to have a refund, escalate immediately."_

## Offer an alternative

When you instruct Fin _not_ to do something, you should also provide a positive instruction on what it should do instead. This gives Fin a clear action to take and leads to more reliable behavior.

**❌ Bad example:**

_"When a customer is angry, do not apologise."_

**✅ Good example:**

_"When a customer is angry, do not apologise. Instead, ask them to calm down politely."_

## Avoid contradictions

Review your active guidance to ensure you don't have rules that conflict with one another. Contradictory instructions can cause Fin to behave in unpredictable ways.

For example, imagine you have these two active guidance instances:

These guidance rules directly conflict. One empowers Fin to resolve certain billing issues, while the other requires immediate escalation for any billing-related keywords. Always review active guidance to avoid contradictory actions.

## Use Content guidance when specificity matters

This feature lets you set rules like “If the customer asks about refunds, always refer to [article name],” ensuring Fin draws answers from the most trusted source.

## Don't use one piece of guidance to trigger another

Each piece of guidance works independently. One piece of guidance (for example, _Guidance A_) can’t directly trigger another piece (like _Guidance B_) after _Guidance A_ has been used in a conversation. Each guidance rule is evaluated separately by Fin at every point in the conversation, and all relevant guidance is applied as needed. There’s no built-in way to chain or cascade guidance automatically.

## Advanced guidance techniques for Fin

Once you're comfortable writing basic guidance, you can use more advanced techniques to fine-tune Fin's behavior.

## Use capital letters for emphasis on critical instructions

To make sure Fin follows a critical instruction, you can use **capital letters**to add emphasis. This is useful for rules that should always be followed without exception.

**For example:**

## Dictating verbatim responses vs. guiding the tone

You have two options when telling Fin what to say in a specific situation: you can either dictate the exact phrase to use or guide Fin on what to communicate, allowing the AI to phrase it naturally.

**To dictate a response:** Tell Fin exactly what to say.

**For example:**

**To guide the tone:** Tell Fin the information you want it to convey, and let it handle the specific wording.

**For example:**

## Using text styles like bold or italics

You can instruct Fin to format its messages with text styles like **bold** or _italics_.

**For example:**

To make a specific part of a message stand out, you could write guidance like this:

## Using the "question mark trick" to manage follow-up questions

By default, after providing a direct answer, Fin will generate a contextual feedback question to check if the customer's issue has been resolved. These questions are generated by Fin's language model and follow your Guidance settings (such as language formality and tone). Fin typically asks questions like "Is that what you were looking for?" or "Did that answer your question?" but can vary based on the conversation context.

You can override this behavior by ending your guidance with a question mark. When a piece of guidance ends with its own question, Fin will ask that question instead of generating its own feedback request.

**For example:**

## Using Communication style guidance to customize answer length

[Fin's answer length setting](https://www.intercom.com/help/en/articles/13177409-customize-fin-ai-agent-tone-of-voice-and-answer-length) lets you define default rules for how long responses should be. As a best practice, we recommend starting with Fin's answer length setting and only adding guidance if you need stricter or more specific control.

One important consideration is that Fin's answer length setting applies globally and can't be targeted to specific audiences, whereas guidance _can_ be audience-specific.

For example, if some customers frequently contact you through social channels like Facebook or Instagram, where messages have a strict 1,000-character limit, you may want to add explicit length constraints in your Communication style guidance for an [audience targeted at those channels](https://www.intercom.com/help/en/articles/10210126-provide-fin-ai-agent-with-specific-guidance#h_9a4371cd62).

**Example guidance:**

## Determine when to use audience targeting vs. user attributes

If you’re deciding whether or not your Fin Guidance should apply based on a user’s data, it’s usually best to use the [Audience targeting](https://www.intercom.com/help/en/articles/10210126-provide-fin-ai-agent-with-specific-guidance#h_165707de2a) feature. Targeting an audience completely hides any non-matching guidance from Fin, which means there’s no risk of confusion or duplication.

**For example:**

If you _only_ want the guidance to apply when a user is on the “Pro” plan, [create an audience](https://www.intercom.com/help/en/articles/9357948-manage-content-and-guidance-targeting-for-ai-answers) for _"Plan is Pro"_, then select this audience when creating your guidance. Fin will only see that guidance when it’s relevant.

On the other hand, if you want Fin to reference the actual value of a [user attribute](https://www.intercom.com/help/en/articles/10210126-provide-fin-ai-agent-with-specific-guidance#h_84c6a090df) in its response, you should include that attribute directly in your guidance.

**For example:**

## Continuously refine your guidance

Think of Fin Guidance as an ongoing process. Start with essential instructions and improve them over time based on real interactions and performance metrics.

## Fin Guidance examples

Below you will find some examples of Fin Guidance. You can use these as inspiration or adapt these for your specific needs.

## Communication style

Specific vocabulary and terminology Fin should use.

## Context and clarification

Follow-up questions Fin should ask, to ensure accurate answers.

## Escalation

Escalation is now managed on its own dedicated page, separate from the main Guidance tab. Go to **Fin AI Agent > Train > Escalation** to set up Escalation Rules (data-driven conditions) and Escalation Guidance (natural language instructions). See [Manage Fin AI Agent's escalation guidance and rules](https://www.intercom.com/help/en/articles/12396892-manage-fin-ai-agent-s-escalation-guidance-and-rules) for a full guide, examples, and best practices.

## Understanding the limitations of Guidance

It's important to know what Guidance is designed for and what its current limitations are.

* * *

💡**Tip**

**Need more help?** Get support from our [Community Forum](https://community.intercom.com/?utm_source=ii-help-center&utm_medium=internal)

Find answers and get help from Intercom Support and Community Experts

* * *

Related Articles

[Provide Fin AI Agent with specific guidance](https://www.intercom.com/help/en/articles/10210126-provide-fin-ai-agent-with-specific-guidance)[Best practices for Fin Tasks](https://www.intercom.com/help/en/articles/10539969-best-practices-for-fin-tasks)[Prevent emails from being closed using Fin Guidance](https://www.intercom.com/help/en/articles/11829564-prevent-emails-from-being-closed-using-fin-guidance)[Manage Fin AI Agent's escalation guidance and rules](https://www.intercom.com/help/en/articles/12396892-manage-fin-ai-agent-s-escalation-guidance-and-rules)[Use Fin previews](https://www.intercom.com/help/en/articles/12599471-use-fin-previews)
