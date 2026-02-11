# Tool Ideation Exercise

---

## 1. Introduction (157 words)

A tool that I am proposing is a GitHub webhook for the Discord server to support the production of the game. The proposed tool aims to replace the need for constant communication between the game developers and the GitHub review team. This tool is intended to be used by the GitHub reviewers, Harry and myself, who require notification of any changes, along with quick and easy access to each change made throughout the game's development.
The game development process involves frequent changes to the repository, especially with a large team. Without an automated notification system, reviewers would have to manually check the repository periodically to check for any changes, meaning that some changes may be missed or that the reviewers might have a lot of catching up to do on recent updates. A webhook system would address this issue by sending messages to a shared Discord channel whenever any of the selected events in the repository occurs. 

---

## 2. Problem (110 words)

The current review workflow depends on reviewers manually checking GitHub to see whether changes have occurred since their last visit. With the high number of branches required for this game, reviewers must also identify which branches changes occurred in before reviewing them. This process consumes time that could be spent on other responsibilites within the project, reducing efficiency during high development periods. Developers may also need to notify reviewers about changes, which improves efficiency but increases communication.
As the repository grows, tracking changes becomes more difficult and reviewers require a consistent, automatic method of monitoring GitHub activity. A development environment benefits from an automated communication system that reduces manual effort.

---

## 3. Solution (117 words)

The solution to this problem that I propose is a bot in a Discord channel that uses webhooks to send repository event data directly to Discord. When a selected repository event occurs, GitHub will send data in the form of a JSON payload to a Discord webhook URL. Discord will then display the data as a readable message inside a chosen, dedicated Discord channel. Each message will include the type of event that occurred, the user who caused the event, and a short summary of the change. A direct link will also be attached to take you directly to the change on GitHub. This tool will ensure that reviewers receive instant updates without having to leave Discord.

---


## 4. Technical context (114 words)

This tool will operate across GitHub and Discord and be supported by any platform that can run both applications, including desktop and mobile devices. It will focus on repository actions relevant to what reviewers need to know about during active development. These actions include pushes, pull requests, branch creation, branch deletion, and merges. Other repository actions are not being sent to the reviewers due to a lack of relevance to the reviewing role and the limited value they provide in assessing development progress. Restricting the events that trigger data being sent will remove any unnecessary notifications, reduce distraction within the channel, and keep the review space focused, organised, and easy to monitor during production.  

---


## 5. Justification (40 words)

The proposed tool will improve efficiency by removing the need for manual, periodic repository checks. Reviewers will receive immediate notifications of development activity within an already used communication platform. This tool supports consistent oversight and reduces the likelihood of missed changes. 

---

## 6. Bibliography

- 262588213843476 (s.d.) Simple Github -> Discord webhook. At: https://gist.github.com/jagrosh/5b1761213e33fc5b54ec7f6379034a22 (Accessed  09/02/2026).

---

## 7. AI Usage Declaration
- Chatgpt was used for paragraph structure and spelling and grammar checking.
- ChatGPT (s.d.) At: https://chatgpt.com/ (Accessed  09/02/2026).

---