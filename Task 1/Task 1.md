# Tool Ideation Exercise

---

## 1. Introduction (≈150 words) 104

A tool that I felt was vital to the production of this game is a GitHub webhook for the Discord server. This tool allows the GitHub reviewers, Harry and myself, to be notified immediately when any push, pull request, branch creation, branch deletion or merge occurs in the repository. Without this tool, reviewers must constantly check for changes and then locate where each change happened. With the webhook, Discord messages show what has changed and include a link to the relevant GitHub page, allowing reviewers to see every update in detail. This improves efficiency and ensures no change is missed during the reviewing process.  

---

## 2. Implementation (≈200 words) 224

The implementation of this task used GitHub and Discord, focusing on GitHub webhooks as the main system. The setup process took place inside the GitHub repository settings and the Discord server settings. The first step involved creating a webhook inside a dedicated Discord channel, which generated a webhook URL linked to that specific channel.

The webhook URL was then added to the GitHub repository webhook settings. Event triggers were then selected to determine which types of events would be sent to the discord channel. The events I selected were branch creation and deletion, pull requests, and pushes. These were the only ones I chose as the others were either irrelevant to what the reviewer team needed to check or unlikely to be triggered. These events send data directly to Discord, in the form of a JSON payload, when triggered, which then displays the information as readable messages from GitHub inside the channel.

Each message displays who triggered the event, what event occurred, and the given title of the change. Each message also includes a link that takes you directly to the change on the GitHub website, allowing easy access for review.

A challenge that occurred during the creation of this tool was an excessive number of notifications from unnecessary events. This issue was fixed by limiting triggers to repository actions relevant to the project. 

---

## 3. Outcome (≈150 words) 206

The final outcome provides automatic Discord messages and notifications for all selected GitHub repository actions, sent directly to the review channel. Each notification contains all relevant information that a reviewer needs to understand each action was for while also providing a link to allow further inspection of the action. This tool removes the need for manual repository checks and reduces the risk of missed changes.

All task requirements were met, as a tool was proposed that is valuable to the production of the game and all other required elements have been previously discussed; the intended user for the tool is the reviewers, the target platform is GitHub and Discord on PC and Mobile devices and the key file used by this tool is a JSON file.

The video below showcases this tool in use. In the video, I create a new branch and show the tool sending a notification about the change. I then make a change within that branch and show the tool sending another message to the Discord channel. Afterwards, I open the attached link to display the detailed view of the change on GitHub. To finish the showcase, I then scroll up the channel to show everything this tool has done so far.


**Demonstration video link:**  
[Tool Showcase](https://youtu.be/bQ7clPsdyZw)

---

## 4. Bibliography

- 262588213843476 (s.d.) Simple Github -> Discord webhook. At: https://gist.github.com/jagrosh/5b1761213e33fc5b54ec7f6379034a22 (Accessed  09/02/2026).


---

## 5. AI Usage Declaration
- Chatgpt was used for paragraph structure and spelling and grammar checking.
- ChatGPT (s.d.) At: https://chatgpt.com/ (Accessed  09/02/2026).

---


## Submission Notes & Checklist

> Remove this section once complete — use this as a checklist before submitting

- Total word count: **500 words (±10%)** across Sections 1–3  
- **Figure captions and figure descriptions do NOT count towards the word count**  
- Use **plenty of images, GIFs, videos, screenshots, and short code snippets** where appropriate to demonstrate understanding and functionality  
- All required **source code is included in this repository**  
- Any required **executables or builds are provided via GitHub Releases**, where appropriate  
- Demonstration video link is accessible and clearly shows functionality  
- Bibliography includes all referenced material  
- AI usage is clearly declared (or explicitly stated as not used)  
- Work reflects your own understanding and professional practice  

---
