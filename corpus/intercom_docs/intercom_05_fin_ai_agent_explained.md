Title: Fin AI Agent explained

URL Source: https://www.intercom.com/help/en/articles/7120684-fin-ai-agent-explained

Markdown Content:
Fin is the most powerful Customer Agent in the market, ready to resolve your most complex queries on all your channels.

As part of our Customer Agent architecture, Fin is evolving to take on [specialized roles](https://www.intercom.com/help/en/articles/12508017-fin-as-a-customer-agent), each trained to world-class expertise.

## The three layers of Fin

## 1. The App Layer

Fin’s [flywheel](https://www.intercom.com/help/en/articles/10742658-navigating-fin-from-setup-to-deploy) powers continuous improvement:

- Train Fin with new knowledge, policies, and connected systems.

- Test changes before going live.

- Deploy across channels and customer segments.

- Analyze performance at scale and retrain as needed.

## 2. The AI Layer

Our industry-leading retrieval-augmented generation (RAG) system ensures Fin delivers accurate, reliable answers:

- Understands context and clarifies questions.

- Uses advanced search to find the right information.

- Applies your guidance and policies.

- Generates a response that avoids halluncinations.

## 3. The Model Layer

We have invested deeply in [custom LLMs](https://fin.ai/cx-models) trained on real customer service interactions. These models include:

- A retrieval model to find potential answers.

- A reranker model to prioritize the best content.

- A summary model to contextualize customer issues.

- A model that detects when to escalate to humans.

- A model to understand the customer’s response.

## Capabilities

## Train

Customize Fin's tone of voice, teach it your support knowledge and policies, and configure how it handles complex tasks in over 45 languages.

[![Image 1](https://downloads.intercomcdn.com/i/o/tx2p130c/1526237664/d0921b89e4dbaa51581cc7042018/CleanShot+2025-05-15+at+19_14_15%402x.png?expires=1775640600&signature=f1e0399ba0d087362a32a700130377c7f0f4ca9ed3319eee2924cc3e1c8528cb&req=dSUlEMt9modZXfMW1HO4zc4QlKHVbJLUh7JIpRL5W3P2BToIafLjoqssWStj%0AEnVW4xhO4m1agakA3Tw%3D%0A)](https://downloads.intercomcdn.com/i/o/tx2p130c/1526237664/d0921b89e4dbaa51581cc7042018/CleanShot+2025-05-15+at+19_14_15%402x.png?expires=1775640600&signature=f1e0399ba0d087362a32a700130377c7f0f4ca9ed3319eee2924cc3e1c8528cb&req=dSUlEMt9modZXfMW1HO4zc4QlKHVbJLUh7JIpRL5W3P2BToIafLjoqssWStj%0AEnVW4xhO4m1agakA3Tw%3D%0A)

### Multi-source generative answers

Fin builds answers using only the most relevant information from multiple knowledge sources—creating more complete and accurate answers to even the most complex questions.

### Content

Fin’s [Content](https://www.intercom.com/help/en/articles/7837514-add-your-support-content-for-fin-ai-agent) library makes it easy for your team to control, update and maintain all of the content Fin learns from in a centralized location - keeping answers accurate and complete as your business changes and grows. Fin can learn from a variety of public and private knowledge sources, including Help Center articles, internal support content, PDFs, and webpages.

### Audiences

Fin can [target content](https://www.intercom.com/help/en/articles/9357948-manage-knowledge-audiences-and-content-targeting-for-fin) to customers based on their plan, location, brand, and more. You can specify what content is relevant for specific groups of customers, to ensure Fin only ever gives relevant answers.

### Tone of voice

Customize [Fin's personality](https://www.intercom.com/help/en/articles/9794969-customize-fin-ai-agent-s-personality) by choosing a tone of voice like professional, friendly, humorous, and more. Then select how long Fin’s answers are, from shorter and concise, to longer and more thorough.

### Guidance

[Fin Guidance](https://intercom.help/intercom/en/articles/10210126-fin-guidance-beta) enables you to coach Fin on how it should answer questions. You can provide Fin with custom instructions to ensure it always follows the correct support policies and communication style with your customers.

### Suggestions

[Suggestions](https://www.intercom.com/help/en/articles/11394959-use-ai-powered-suggestions-to-improve-fin-s-content) is an AI-powered feature that recommends content improvements based on conversations Fin couldn't resolve. They update content, create new content, flag duplicates, learn from rejected Suggestions, and work across content in Intercom, Zendesk, and Salesforce.

### Data connectors

Set up [Data connectors](https://www.intercom.com/help/en/articles/9569407-fin-ai-agent-personalized-answers-beta) to your external systems, enabling Fin to provide more personalized answers and perform complex tasks on behalf of your customers.

### Personalised responses

When Identity Verification (IDV) is enabled, Fin automatically receives a set of basic user attributes and uses them to personalise responses. This includes addressing customers by name, considering their location, and tailoring tone based on who they are, no additional configuration required.

The following attributes are available to Fin when IDV is enabled:

- Name

- Email

- City

- Country

- Browser locale

- Conversation start time

### Custom Data Attributes

Fin can access and use [Custom Data Attributes](https://www.intercom.com/help/en/articles/179-custom-data-attributes) (CDAs) when generating answers, allowing it to personalize responses based on what it already knows about a customer. Currently, Fin can access 6 specific attributes that have been made available, all other CDAs require explicit configuration (for example, via Guidance, Data connectors, or Fin Procedures) before Fin can use them.

For example, the image below shows where a CDA has been added in Guidance.

[![Image 2](https://downloads.intercomcdn.com/i/o/tx2p130c/2221909713/859d370f14a52306bfeb79e92676/CleanShot+2026-03-31+at+10_11_20%402x.png?expires=1775640600&signature=a992e96b404244f130d6049b33524981fe7e38f4577788976a7d028d4e983736&req=diIlF8B%2BlIZeWvMW1HO4zbXtKW6fB0XevMKBNw9rv1Bp05WQtfokZIQ%2BEgW9%0A651KU5sjKodehkomp%2Fg%3D%0A)](https://downloads.intercomcdn.com/i/o/tx2p130c/2221909713/859d370f14a52306bfeb79e92676/CleanShot+2026-03-31+at+10_11_20%402x.png?expires=1775640600&signature=a992e96b404244f130d6049b33524981fe7e38f4577788976a7d028d4e983736&req=diIlF8B%2BlIZeWvMW1HO4zbXtKW6fB0XevMKBNw9rv1Bp05WQtfokZIQ%2BEgW9%0A651KU5sjKodehkomp%2Fg%3D%0A)

### Tasks `managed availability`

[Fin Tasks](https://www.intercom.com/help/en/articles/10257113-beta-fin-triggered-workflows) allow you to automate more complex processes with Fin. Often times, these processes may involve multiple actions and for Fin to reliably follow your specific business rules (e.g. cancel an order, refund a subscription). Fin will trigger the task and be actively involved each step to resolve customer queries.

### Procedures `managed availability`

[Procedures](https://www.intercom.com/help/en/articles/12495167-fin-procedures-explained) are the next step in Fin’s ability to handle complex queries. With Procedures, we’ve taken what worked well with Fin Tasks and made it simpler and smarter: a simple document-style editor ability to add code and data connectors within steps. This makes them faster to set up, easier to maintain, and more reliable to run—especially as processes get more complex.

### Real-time translation

Fin can automatically detect and resolve issues in more than 45 languages, giving you complete control over which languages Fin will answer in. Fin can use all of your support content in its [multilingual answers](https://www.intercom.com/help/en/articles/8322387-use-fin-ai-agent-in-multiple-languages), even if the content hasn’t been localized to the language Fin is answering in.

### Vision

[Fin Vision](https://www.intercom.com/help/en/articles/10696494-learn-how-fin-ai-agent-understands-images-in-conversations) means solving issues faster by letting your customers show, not tell. Fin can read and understand images—like screenshots, invoices, and error messages—so customers can share what they see without lengthy explanations.

## Test

Use real customer questions to test Fin’s answer quality and refine its sources and settings, so it always reflects your latest support content and policies.

[![Image 3](https://downloads.intercomcdn.com/i/o/tx2p130c/1527048335/7b9ae98655f27f3027d8fb000c3c/CleanShot%2B2025-05-15%2Bat%2B19_15_50-402x.png?expires=1775640600&signature=f7527e9a296c108e37017ae063ff73d3774527ff8fef9c270ae20d4edb41781f&req=dSUlEcl6lYJcXPMW1HO4zVOHbHfvVPv7s4glwwlKcpbX20T3UhIDfsXqI%2B4O%0ABB%2Fb72F6di%2FMLvPQKUk%3D%0A)](https://downloads.intercomcdn.com/i/o/tx2p130c/1527048335/7b9ae98655f27f3027d8fb000c3c/CleanShot%2B2025-05-15%2Bat%2B19_15_50-402x.png?expires=1775640600&signature=f7527e9a296c108e37017ae063ff73d3774527ff8fef9c270ae20d4edb41781f&req=dSUlEcl6lYJcXPMW1HO4zVOHbHfvVPv7s4glwwlKcpbX20T3UhIDfsXqI%2B4O%0ABB%2Fb72F6di%2FMLvPQKUk%3D%0A)

### Simulations `coming soon`

Trust Fin to handle complex queries reliably and safely with [Simulations](https://www.intercom.com/help/en/articles/12495167-fin-procedures-explained#h_dfcfc980f5). Test Fin’s performance across real-world scenarios, from simple flows to tricky edge cases. Confirm it behaves as expected and catch issues before they reach customers.

### Batch testing

[Batch test](https://www.intercom.com/help/en/articles/10521711-test-fin-ai-agent-beta) how ready your content is for Fin. Easily import conversations from your support inbox, other sources, or add them manually to evaluate Fin’s accuracy and performance.

### Answer rating

Review and rate each of Fin's answers. Ratings and comments are captured in a report so you can prioritize what needs work and improve your content.

### Fin preview

Test and refine Fin in real time. Instantly see how updates to guidance, deployment settings, or intro messages will appear to customers, helping you perfect the experience before going live. You can also see how Fin answers for various customer types across multiple brands, audiences, or personas.

### Answer inspection

Get full visibility into how Fin generated an answer. See exactly which sources and settings—like tone of voice and Guidance—shaped the response.

## Deploy

Deploy Fin across email, voice, live chat, social, and more. Fin can answer, triage, and collaborate with your team to deliver consistent experiences across channels.

[![Image 4](https://downloads.intercomcdn.com/i/o/tx2p130c/1526232778/dbaaf32fb83fcfc21bd6c4fa5ed9/CleanShot+2025-05-15+at+19_10_41%402x.png?expires=1775640600&signature=3d964e02596adb2555cf91d55606838ff98487912d3e1708d355f7cb56b45c9d&req=dSUlEMt9n4ZYUfMW1HO4zQjuW%2BvxB%2BPufW9KBGFuJ9YoGAj7RBZjg17toV3e%0ADfTwzkMCzLrzufvCFMs%3D%0A)](https://downloads.intercomcdn.com/i/o/tx2p130c/1526232778/dbaaf32fb83fcfc21bd6c4fa5ed9/CleanShot+2025-05-15+at+19_10_41%402x.png?expires=1775640600&signature=3d964e02596adb2555cf91d55606838ff98487912d3e1708d355f7cb56b45c9d&req=dSUlEMt9n4ZYUfMW1HO4zQjuW%2BvxB%2BPufW9KBGFuJ9YoGAj7RBZjg17toV3e%0ADfTwzkMCzLrzufvCFMs%3D%0A)

### Fin over chat

Deploy [Fin over chat](https://www.intercom.com/help/en/articles/8286630-set-fin-ai-agent-live-over-chat) to greet customers, instantly answer questions, and escalate issues to your team when needed—inside the Messenger and across WhatsApp, SMS, and social.

### Fin over email

Fin is fully optimized for delivering [support via email](https://www.intercom.com/help/en/articles/9356221-set-fin-ai-agent-live-for-email) and can provide instant, accurate answers to customer questions, making sure to filter out phishing attempts, spam, and other threats. Fin will have full context of the email conversation history, and structure every answer specifically for the email channel, making sure to escalate to human support exactly when it needs to.

### Fin over phone

AI phone support, built for real conversations. [Fin Voice](https://www.intercom.com/help/en/articles/10697275-fin-voice-coming-soon) answers calls naturally, handles complex questions, and connects customers to human agents when needed.

### Fin over Slack

Fin delivers instant, accurate answers on [Slack](https://www.intercom.com/help/en/articles/10551073-connect-your-slack-support-channel), scaling AI-first customer service to your busiest communities and threads.

### Fin over Discord

In your [Discord](https://www.intercom.com/help/en/articles/11868746-native-discord-channel-alpha) server, new customer messages trigger Intercom conversations so Fin can respond seamlessly, right from the Intercom Inbox.

### Workflows for Fin

Deploy Fin to power your [Workflows](https://www.intercom.com/help/en/articles/10032299-using-fin-ai-agent-in-workflows)—no extra setup required. Add Fin to your automatons to triage, handle complex customer queries and generate answers when customers take specific actions.

### Human handoff

Configure how and when Fin triages conversations or[hands off](https://www.intercom.com/help/en/articles/12396892-how-to-automatically-escalate-conversations) to your human support team. Fin will always automatically handoff when that is the safest option for the customer.

### Audience targeting

Fin shows up for your customers how and when you decide—by audience, region, channel, and more—helping you stay in control and maintain support availability.

### Usage limits and notifications

Receive notifications or stop Fin delivering AI Answers to customers when a [defined resolution limit](https://www.intercom.com/help/en/articles/8991894-how-to-see-and-manage-your-usage#h_36badc7757) is reached.

## Analyze

Get a complete view across AI and human support to monitor performance, spot issues faster, and optimize Fin with AI-powered suggestions.

[![Image 5](https://downloads.intercomcdn.com/i/o/tx2p130c/1769809427/eb615a0095b6d4b6bd007109577c/CleanShot%2B2025-05-15%2Bat%2B19_13_24-402x.png?expires=1775640600&signature=0f340ae6c6d6a650d40518a192ab1796b5bd0c71ad46e4762664faafb3004230&req=dSchH8F%2BlIVdXvMW1HO4zUnHZRj%2BgFZ4QgMI5%2F3dRa6pZRkQCGhcaP%2BRinLj%0AL9g%2Bdhf1alzVf%2FT54Nw%3D%0A)](https://downloads.intercomcdn.com/i/o/tx2p130c/1769809427/eb615a0095b6d4b6bd007109577c/CleanShot%2B2025-05-15%2Bat%2B19_13_24-402x.png?expires=1775640600&signature=0f340ae6c6d6a650d40518a192ab1796b5bd0c71ad46e4762664faafb3004230&req=dSchH8F%2BlIVdXvMW1HO4zUnHZRj%2BgFZ4QgMI5%2F3dRa6pZRkQCGhcaP%2BRinLj%0AL9g%2Bdhf1alzVf%2FT54Nw%3D%0A)

### Fin Performance report

The [Performance dashboard](https://www.intercom.com/help/en/articles/11390083-check-on-how-fin-is-performing) brings together Fin’s resolution rate, involvement rate, and CX score in one view. It shows where Fin is succeeding and where human support might need to step in.

### Optimize Fin dashboard

The [Optimize dashboard](https://www.intercom.com/help/en/articles/11390088-optimize-fin-instantly-with-the-help-of-ai) flags Fin’s areas for improvement and uses AI to generate actionable suggestions. You can review and approve fixes in seconds, so Fin keeps getting better without slowing your team down.

### Customer Experience (CX) Score

With 5x more coverage than CSAT, the [Customer Experience (CX) Score](https://www.intercom.com/help/en/articles/10495092-customer-experience-cx-score-closed-beta) measures the quality of every conversation—so you can understand how all your customers feel when interacting with Fin and teammates.

### Topics Explorer

[Topics Explorer](https://www.intercom.com/help/en/articles/11390087-use-the-topics-explorer-to-see-what-s-driving-volume) uses AI to automatically group conversations into topics and subtopics. It helps you spot trends, track high-effort issues, and understand what’s driving volume—without manual tagging or hours of analysis.

### Topic trends `coming soon`

Topic Trends highlights the most important weekly shifts in your support topics—like spikes in volume, drops in AI Agent performance, or emerging questions—so you can act early before they impact customer experience.

### Customizable AI Topics `coming soon`

You can now create, merge, delete, and rename Topics and Subtopics—so reports reflect the issues that matter most and align with how your business thinks about customer conversations.

### Conversation monitoring

### Holistic reporting

Get visibility into the overall health of your entire support organization with a [unified view](https://www.intercom.com/help/en/articles/3008200-holistic-overview-report) of AI and human support in one detailed report.

### Fin custom reporting

Build your own Fin performance and quality report using Intercom’s new and improved [custom reporting](https://www.intercom.com/help/en/articles/4549035-create-a-custom-report) tools, including new chart styles, drag and drop chart building and chart drill-in to dive deeper into the root cause of performance.

## Integrations

Fin integrates with any helpdesk. You can choose to set up Fin with your existing helpdesk or as part of the Intercom Customer Service Suite—with support for additional platforms and custom channels.

Fin works seamlessly with platforms like Zendesk, Salesforce, or your custom-built helpdesk:

- Set up in under an hour.

- Uses your current support channels—tickets, email, live chat, and more.

- Follows your existing assignment rules, automations, and reporting.

- Escalates to agents in your preferred inbox.

* * *

💡**Tip**

**Need more help?** Get support from our [Community Forum](https://community.intercom.com/?utm_source=ii-help-center&utm_medium=internal)

Find answers and get help from Intercom Support and Community Experts

* * *

Related Articles

[Fin for platforms explained](https://www.intercom.com/help/en/articles/10118495-fin-for-platforms-explained)[Provide Fin AI Agent with specific guidance](https://www.intercom.com/help/en/articles/10210126-provide-fin-ai-agent-with-specific-guidance)[Fin Guidance best practices](https://www.intercom.com/help/en/articles/10560969-fin-guidance-best-practices)[Manage Fin AI Agent's escalation guidance and rules](https://www.intercom.com/help/en/articles/12396892-manage-fin-ai-agent-s-escalation-guidance-and-rules)[Deploy Fin Ecommerce Agent](https://www.intercom.com/help/en/articles/14420740-deploy-fin-ecommerce-agent)
