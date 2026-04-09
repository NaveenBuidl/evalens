All Collections
Fin AI Agent
Train
Provide Fin AI Agent with specific guidance
Provide Fin AI Agent with specific guidance
How to use Guidance to customize Fin's responses to match your support policies and communication style.


Written by Julia Godinho
Updated over 3 weeks ago

Train Fin to support your customers—just like your best agent.

Fin Guidance lets you train Fin to speak in your brand’s voice, follow your policies, and handle conversations the way you want—using simple, natural-language instructions. 

This means faster resolution times, more consistent support quality, and a better customer experience.

You can set clear rules for what Fin should say and do, from using the right content and terminology to escalating sensitive issues. 

Built-in reporting shows how well Fin is following your guidance, with AI-powered suggestions to help you fine-tune responses over time.

 

Get started
Go to Fin AI Agent > Train > Guidance.

 


 

To help get you started, we have created different categories of guidance:

Communication style: Ensure every response reflects your company’s tone and terminology. Define how Fin communicates so it speaks like your best-trained agents—delivering high-quality support that stays true to your brand

Context and clarification: Guide Fin to ask thoughtful follow-up questions, reducing miscommunication and helping it get to the right answer faster—so customers reach a resolution sooner.

Content and sources: Specify which content sources (like articles or webpages) Fin should use when answering particular types of customer questions. 

Spam: Spam Guidance is a powerful feature that allows customers to define custom guidelines for how the AI spam detection system should behave, ensuring the system aligns with their specific business needs.

Other: Anything that does not fit into the above categories should be added here. This could be specific company or support policies that you’d like Fin to adhere to, such as never asking customers to contact you by phone. 

You'll find guidance templates within each category to help you get started. You can modify the wording of a template to suit your needs.

 

Tip: Read our Fin Guidance best practices before you get started to learn the dos and don’ts of writing good guidance prompts.

 

Note: 

To ensure guidance works effectively, make sure it is assigned to the correct category.

Only 100 pieces of guidance can be active per conversation, but you're not limited to creating just 100. Segmenting by audience and channel means each conversation only draws from a relevant subset, so your total guidance count can exceed 100. Each guidance can be up to 2,500 characters in length.

 

Create new Fin Guidance
Go to Fin AI Agent > Train > Guidance and click + New to add new guidance to the appropriate category.

 


 

Enter your guidance in the text field or choose from one of the templates to get started quickly.

 


 

Optimize guidance
After writing a piece of guidance, click the lightbulb to have it reviewed by our AI-powered writing assistant. This tool helps refine your guidance by checking for common issues and suggesting improvements.

 


 

The Fin Guidance writing assistant looks for:

Ambiguity – Guidance that could be interpreted in multiple ways or lacks clarity.

Redundancy – Guidance that repeats information already covered elsewhere.

Contradiction – Conflicting or opposing guidance that may cause inconsistencies.

Clarity and effectiveness – Guidance that could be reworded to be clearer, more concise, and more effective.

System limitations – Instructions that attempt to perform actions Fin cannot take. Learn more about what Fin Guidance can't be used for.

 

If an issue is found, the writing assistant will explain why and suggest possible improvements. 

 

It may also offer a reworded version of your guidance for better clarity and effectiveness. You’ll be able to compare the suggestion with your original text and choose to accept, edit, or refine it further.

 

Tip: If you’re unsure how to write a prompt for a specific use case, try using a writing tool like Claude AI or ChatGPT. Describe the scenario and ask it to generate a clear, AI-friendly prompt that’s easy to interpret.

 

Add audience rules to guidance
Apply audiences to Fin Guidance if you want to target specific customer segments with tailored guidance. This ensures that Fin only uses guidance for customers who match the selected audience, and ignores it for those who don’t—resulting in more accurate and controlled guidance behavior.

 

Simply create your guidance and then select an audience from the Audience dropdown menu. 

 


 

Note: Audiences must be set up in your workspace to use them with Fin.

 

Use attributes in guidance
User, company, or conversation attributes can also be included in your guidance to personalize responses. For example:

 

“When relevant and appropriate, refer to the user's name as {First name} or their company name as {Company name} to make responses feel more personal and engaging."

 


 

Here, the placeholders {First name} will automatically populate with the customer’s name before Fin generates a response. 

 

Note: 

Data attributes won't always be used by Fin. If you want to set strict targeting rules, add an audience to the guidance prompt instead. This gives you precise, reliable control over when and how Fin applies guidance—making your support experience more predictable and tailored to each customer segment.

Learn when to use audience targeting vs. user attributes in your guidance.

​ 

Give channel specific guidance
Tailor Fin's behavior based on the channel customers use to contact you. Each guidance card has a built-in channel selector — simply choose which channels (Chat, Email, or Voice) the guidance should apply to directly on the card. This ensures Fin responds appropriately based on the channel context.

 

For example:

“Avoid suggesting they contact us by phone for further support.”

 


 

Give content guidance
Content guidance lets you specify the content Fin should refer to when answering particular types of questions. This gives you more control over which knowledge sources Fin relies on, ensuring more accurate and consistent answers:

Point Fin to specific content when answering a specific type of question.

Guide Fin to avoid relying on outdated or general sources by specifying preferred ones.

Combine Content Guidance with audiences to tailor behavior to different customer segments.

 

For example:
​“When a customer asks for advice on how to manage their projects more effectively, use Public article: Project management best practices.”

 


 

To add content guidance, click + New under Content and sources. Write a condition for when the guidance should apply (e.g., “If a customer asks about refunds…”) Then use @ to insert a Fin-enabled content source. You can start typing the title to filter.

 

Once enabled, Fin will prioritize the specified source if it’s relevant to the query and combine it with other content it deems as relevant.

  

Note:

You can write phrasing like “Don’t use [article],” but Fin may still use it if it’s the best match. To prevent usage, remove that source from Fin’s content availability settings or restrict it to the right audience.

Content guidance is prioritised over audience targeting. If content guidance uses a resource with audience targeting, but the customer is not part of that audience, the resource will still be used. Make sure to set the correct audience in your guidance.

If you add URLs to your guidance, Fin can link to these in answers even if the URL is not one of the sources you've enabled for Fin.

 

Test Fin Guidance
Before you save or enable a piece of guidance, you can use the Preview panel to ask Fin some questions and see how your new guidance is applied.

 


 

To preview how Fin applies your guidance to a specific user or brand, select the Preview user dropdown at the top of the preview and then select User or lead. This let's you impersonate real users/leads and see exactly how Fin will respond. You can simulate real scenarios using live or dummy data, test data connectors, and validate every answer.

 


 

When you're happy with how Fin is using your guidance, click Enable to set the guidance live for Fin's conversations with customers.

 

Note:

You may notice that all Guidance preview conversations appear in your inbox and this is expected. However, these conversations are not included in your reporting.

When you test Guidance in Preview, all types of Guidance are included (draft, paused, and live). This ensures you can fully test and refine your Guidance without needing to publish it first.

 

See Fin Guidance performance
Once your guidance is enabled, you can track its impact on Fin’s conversations. Go to Fin AI Agent > Train > Guidance to see how often a piece of guidance was used and what percentage of those conversations were resolved or escalated to your team.

 


 

Click on these stats to:

View a list of conversations where the guidance was used.

Use advanced filtering to uncover patterns and insights.

Click into a conversation to preview the interaction and see how guidance influenced Fin’s response.

These insights help you refine your guidance, ensuring Fin consistently delivers accurate and effective support.

 

In Reports
Create a report from Reports and add the "Guidance applied" filter to see metrics where that guidance was used.

 


 

You can also add the "Escalation rule applied" filter to see metrics where that escalation rule was used.

 


 

Then analyze your Guidance performance by tracking key metrics: 

 

Fin AI Agent escalated conversations: This metric shows the total number of conversations Fin handed over to a human.


 

Fin AI Agent escalation rate: The percentage of total Fin conversations that resulted in an escalation.

 


 

Fin AI Agent: Configuration based escalation reason: A granular attribute that identifies exactly why Fin escalated, such as Guidance applied, Escalation rule applied, or Fin in one-time mode.


 

These insights provide valuable information about how often Fin escalates conversations and the effectiveness of those escalations in leading to a positive teammate interaction.

 

In the Inbox
You can also see when Fin applies your guidance in the Inbox. The conversation events record which specific pieces of guidance were used as part of a response.

 


  

FAQs
How does Fin Guidance work?
Fin Guidance works alongside the other content and data sources you provide. Before generating a response, our AI Engine checks for relevant guidance and applies it to ensure Fin’s response aligns with your policies.

Guidance can also use the following context to adjust Fin's response if these are referenced in the guidance prompts:

The current date and time.

The channel the conversation is using (Messenger chat, Android, iOS, email, WhatsApp, Facebook Messenger, Instagram, and SMS).

Audience rules that have been applied to the guidance.

Attributes that have been specifically referenced in the guidance.

The conversation history.

The language the customer is using in the conversation.

The brand name and bot identity you have configured for your workspace.

Learn more about the technology behind Intercom's patented AI agent, Fin.

 

How does using Fin Guidance impact Fin’s response time?
We've made significant improvements to make Fin's response time faster when using Guidance. With this improvement, the delay caused by applying Guidance is eliminated, resulting in a much faster and more seamless experience.

 

What can Fin Guidance not be used for?
Fin Guidance cannot:

Take actions on the conversation (other than handing over to the team). For example, guidance cannot be used to route handovers or escalations to a specific team inbox, tag conversations, update conversation attributes, mark conversations as priority or take any other actions. Instead, these should be configured via Fin AI Agent Simple deploy or Workflows. 

Read or re-write Custom Answers. Custom Answers are hardcoded and not supported with Fin Guidance.

Add conversation tags or pull information from specific content sources based on a prompt.

 

How can I ensure my guidance is written effectively?
Follow our best practices and review the examples.

Check your guidance wording by running it through a writing tool like Claude AI or ChatGPT to ensure clarity and ease of interpretation.

Test your guidance using the preview to see how Fin would answer related questions. Whenever you update your guidance, you can test it before you set it live.

 

How can Guidance be used to customize Fin’s escalation behavior for customers?
Guidance settings let you tailor how Fin escalates customer conversations. For example, you can set Fin to escalate directly (not just offer) when a customer requests human support, appears angry, or gets stuck in a repetitive loop. Guidance also allows you to adjust Fin’s sensitivity to frustration or specific keywords, like “agent”—so escalation happens exactly when and how you want. This ensures customers get the right support at the right time.

 

Do Fin Guidance based handovers contribute to the Fin AI Agent escalated to team rate?
Yes, Fin Guidance based handovers and escaltions

 follow the same route as non-guidance based handovers.

 

Can Fin Guidance be written in a language other than English?
Yes, Fin Guidance can be written in another language. However, it is recommended to use the language you are most comfortable with to clearly express the guidance you need Fin to follow.

 

Can emojis be used with Fin Guidance?
By default, Fin will not use emojis in it's AI answers; however, you can add guidance in the 'Communication Style' category to prompt usage. For example, adding "Use one or two emojis in your responses to create a friendly and engaging tone" will then lead Fin to use one or two emojis in your responses. 

 

 How do I test escalation guidance in Fin over email?
To test Fin's escalation guidance over email, you can use the email preview option.

Go to Fin AI Agent > Deploy > Email.

Click "Copy address".

Send an email to the copied address from the email address you used to sign up to Intercom.

Once you've previewed the experience, you can set Fin live.

 

Can I create guidance without a title?
No, you won't be able to save new guidance without adding a title. This ensures all guidance is easy to identify.

 

Where did the "Handover and escalation" category go?
If you're wondering where the "Handover and escalation" category went, we've moved it. To make escalation more powerful and easier to manage, it's no longer a category within the main Guidance tab. It now has its own dedicated tab, which you can find by navigating to Fin AI Agent > Train > Escalation.

 

How do I make Fin escalate conversations now?
To make Fin escalate conversations, you'll use the new, dedicated Escalation tab (at Fin AI Agent > Train > Escalation). This gives you two powerful ways to control handoffs:

Escalation Rules: For deterministic escalations based on data (e.g., "Customer plan IS Pro" or "Customer Sentiment is angry).

Escalation Guidance: For nuanced, scenario-based escalations using natural language (e.g., "If a customer mentions 'refund'").

For a complete guide on this new escalation feature, see our article: Optimizing Fin Al Agent for customer escalation and interaction.

 

Can guidance be used to detect how many links are contained in a customer's message?
Fin Guidance does not perform structured URL analysis. It cannot:

Count how many URLs are included in a message

Identify unique domains

Extract or compare domains

Perform multi-step parsing of links

Guidance is designed to control how Fin responds based on specific questions, keywords, or customer attributes (such as routing, escalation, or tone of voice). It is not intended for complex data extraction or structured analysis.

 

Can guidance detect when a message includes a link?
Fin Guidance won’t reliably detect an actual URL if you explicitly instruct it to “detect a URL.” Instead, it works better when you simplify the condition and ask it to check for a specific string or pattern in the customer’s message.

For example, instead of writing:

“If a user reaches out and their message contains the link [examply.com/pricing]…”

Write:

“If a user reaches out and their message contains ‘examply.com/pricing’…”

This simple change allows guidance to detect whether the customer’s message contains that specific phrase or text string.