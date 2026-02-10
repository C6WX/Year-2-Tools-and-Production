# Tool Ideation Exercise

---

## 1. Introduction (157 words)

A tool that I am proposing is a GitHub webhook for the Discord server to support the production of the game. The proposed tool aims to replace the need for constant communication between the game developers and the GitHub review team. This tool is intended to be used by the GitHub reviewers, Harry and myself, who require notifying of any change along with quick and easy access to each change made throughout the game's development.
The game development process involves frequent changes to the repository, especially with a large team. Without an automated notification system, reviewers would have to manually check the repository periodically to check for any changes, meaning that some changes may be missed or that the reviewers might have a lot of catching up to do on recent updates. A webhook system would address this issue by sending messages to a shared Discord channel whenever any of the selected events in the repository occurs. 

---

## 2. Problem (156 words)

The current review workflow depends on the reviewers manyally checking GitHub to make sure there have or haven't been any changes since they last checked. As well as this, with the high amount of branches required to be created to make this game, reviwers would also need to locate which branches these changes have taken place on before they can review the change. This process consumes time that could be spent on other responsibilites within the project, reducing efficiency, especially during periods of high development. Developers might also need to notify reviewers about their changes, which would increase the efficiency of the review process but also would result in overly high amounts of communication.
As the repository grows, tracking changes will become more difficult and reviewers will need a consistent and automatic method of monitoring activity on GitHub. A development environment will benefit from an automatic communication system that reduces need for manual input and effort.

---

## 3. Solution

The solution to this problem that I propose is bot in a Discord channel that uses webhooks to send repository event data directly to Discord. When a selected repository event occurs, GitHub will send data in the form of a JSON payload to a Discord webhook URL. Discord will then display the data as a readable message inside of a chosen, dedicated Discord channel. Each message will include the type of event that occured, the user who cause the event, and a short summary of the change. A direct link will also be attached to take you directly to the change on GitHub.

---


## 4. Scope and technical context


---


## 5. Justification


---

## 6. Bibliography

- 262588213843476 (s.d.) Simple Github -> Discord webhook. At: https://gist.github.com/jagrosh/5b1761213e33fc5b54ec7f6379034a22 (Accessed  09/02/2026).

---

## 7. AI Usage Declaration
- Chatgpt was used for paragraph structure and spelling and grammar checking.
- ChatGPT (s.d.) At: https://chatgpt.com/ (Accessed  09/02/2026).

---