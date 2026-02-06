## Course Material Automation

Beyond the platform development, I've also automated the creation of course materials. Previously, creating homework assignments and course plans required 20-30 minutes of clicking in the admin interface for each course.

I created a Claude agent with skills describing how to interact with the course management platform API. Now I can describe what I want in text format - which homework assignments to create, what deadlines they should have - and the agent makes the POST requests and sends me a URL to review[^4].

This same approach works for creating individual homework assignments. My previous workflow:
1. Write homework in a Markdown document
2. Push to repository
3. Open the platform admin interface
4. Manually enter questions and answers (5-10 minutes)

Now I can tell the agent: "Here's a markdown document with homework, please create the homework form." Done[^5].
