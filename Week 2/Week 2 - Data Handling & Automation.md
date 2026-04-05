# Data Handling & Automation

---

## 1. Introduction

This essay explains the GitHub webhook tool I created for the Discord server. This tool sends notifications for selected repository actions and helps the GitHub reviewers stay on top of changes during development. There are frequent updates to the repository, like pushes, pull requests and branch changes. Without a system like this, reviewers would have to check the repository manually, which takes time and risks missing updates.
The tool uses built-in features from GitHub and Discord. It doesn't need any external software, which makes setup simple and reliable. It works on any platform that can run GitHub and Discord, including PC and mobile. Using these features also makes the tool easy to maintain as the project progresses. It provides a clear, real-time way for reviewers to see what changes have been made, who made them and where they happened in the repository.

---

## 2. Implementation

The implementation of this task used GitHub and Discord, focusing on GitHub webhooks as the main system. The setup process took place inside the GitHub repository settings and the Discord server settings. The first step involved creating a webhook inside a dedicated Discord channel, which generated a webhook URL linked to that specific channel.
<br>

![Discord Webhook](https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Task%201/Images/Discord%20Webhook%20Setup.png)
*Figure 1. The webhook that was setup on Discord that GitHub would use to send messages.*

<br>
The webhook URL was then added to the GitHub repository webhook settings. Event triggers were then selected to determine which types of events would be sent to the Discord channel. The events I selected were branch creation and deletion, pull requests and pushes. These were the only ones I chose as the others were either irrelevant to what the reviewer team needed to check or unlikely to be triggered. These events send data directly to Discord in the form of a JSON payload when triggered, which then displays the information as readable messages from GitHub inside the channel.
<br>

![GitHub Webhook](https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Task%201/Images/GitHub%20Webhook%20setup.png)
*Figure 2. The Webhook settings used to create this took on Github.*

<br>
Each message displays who triggered the event, what event occurred and the title of the change. Each message also includes a link that takes you directly to the change on the GitHub website, allowing easy access for review.
<br>

![GitHub Message Example](https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Task%201/Images/Github%20Message%20Example%202.png)
*Figure 3. An example of a message created by this tool.*

<br>
<br>

![In Depth Push](https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Task%201/Images/In%20Depth%20Push%20Example.png)
*Figure 4. The in depth version of the change, found by clicking the link attached to each change.*

<br>
A challenge that occurred during the creation of this tool was an excessive number of notifications from unnecessary events. This issue was fixed by limiting the triggers to repository actions relevant to the project. 


---

## 3. Outcome

The final tool delivers automatic Discord notifications for all selected GitHub repository actions. Reviewers no longer have to rely on manual repository checks to stay informed of any changes being made. Each relevant change appears instantly inside the review channel with a direct link to the GitHub website for a more in-depth inspection. The messages let reviewers quickly see what changed, who caused it, and where it happened without leaving Discord.
The notifications give a clear record of all activity in the repository. Reviewers can track progress, spot issues quickly, and check changes in detail with minimal effort. The tool reduces extra messages from developers and keeps communication focused. It saves time, improves review accuracy and makes it easier to manage changes. Overall, it keeps the review process organised and ensures nothing is missed during development.


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
