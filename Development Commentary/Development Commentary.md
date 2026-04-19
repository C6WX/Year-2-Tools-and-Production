# Development Commentary

**Unit Name:** Tools and Production

**Student Name:** Callum Wade

**Student ID:** 2404781

**Total Word Count:** \[XXXX]

**API Reference Link:** \[URL]

**User Guide Link:** \[URL]

**Build Link:** \[URL or Embed]

**Video Demonstration Link:** \[URL or Embed]

---

## Abstract *(Approx. 5–10% of word count)* 382 words
This development commentary covers all of my work whilst developing Greedy Piggies. The work covered consists of:
- Jenkins
- GitHub Webhook
- Clickup Webhook
- Creating the game's multiplayer
- Creating the UI for the multiplayer
- Creating the character select screen

Within this project my tasks primarily consisted of creating automation tools to build the game, creating tools to improve workflow, reviewing GitHub pushes and programming the games multiplayer. These tasks weren't my original ones but were altered and adapted off of a RACI chart. My original roles also included design liaison and HR department, however I felt that these roles fell through as there was no need for the HR department within this project and in terms of conversing with the designers, everyone ended up talking to them themselves due to all the small departments that appeared and disappeared throughout the development of the game, meaning communication was easiest without a middle man in the way.

My goals for this project was to release a game on steam that had a working multiplayer system that I helped develop and to improve the games development process with the tools I created and implemented into the development cycle.

I approached this project by first ordering my tasks by level of importance, which lead me to start with the multiplayer menu, then move onto Jenkins to have that building the staging branch of the game. However it did not end up panning out this way as a lot of problems arose from the multiplayer at varied points of the game's development as well as new tool ideas to implement and more things for me to make or improve. For example, I realised that the ClickUp page that was created to keep the developers and designers on track and to allow everyone to see what still needs to be done and what has been done. But due to it's lack of use, I added a webhook to the Discord server to notify people on the progress updates from ClickUp so that people would feel more inclined to use it. 
Something else that threw off my original approach was creating all the original UI and the character select screen, as it was not part of the original plan but was only thought of because of an error with the multiplayer. 

---

## Research *(Approx. 20-30% of word count)*

### What sources or references have you identified as relevant to this task?

#### Jenkins
To be able to implement Jenkins into the project so that it could automatically build the staging branch, I first had to research how to setup Jenkins and how to use it. At first I started off by following a tutorial that covered downloading and installing Jenkins (How To Install Jenkins on Windows 11, 2023). At first I struggled to find the right tutorial for setting this up but this video was able to help me get Jenkins installed and working. During the install process, I did have trouble with finding which version to use and using the setup wizard but after looking into the official documentation, I was able to install the right version and continue following along with the video (Windows, s.d.). 
Once Jenkins was setup, I then went on to researching how I would go about creating a pipeline. I started by watching videos and looking at documentation but they ended up not covering what I was trying to use Jenkins to do. So after that I then went onto asking for help from my lecturer who had used Jenkins before, who then provided me with a base code to use with Jenkins. After tweaking the code a bit, I was able to get Jenkins working on the staging branch.

#### App to Discord Webhooks
I used webhooks three times during this project, one was programmed into the groovy script to link Jenkins to Discord, the second was to link GitHub to Discord and the third was to link ClickUp to Discord.
When linking Jenkins and Discord, I didn't use any sources due to using AI improve my code, however I did research into linking GitHub to Discord. I wanted to create a webhook between the two apps so that ticket reviewers would get updates as soon as anything is changed on GitHub in an easy to read message format. To do this I found the official GitHub documentation (Creating webhooks, s.d.) that covers creating and using webhooks on GitHub. Looking through this documentation and using AI to help with the Discord side of the webhook allowed me to setup a link between the two websites so that whenever a change occurred on GitHub, a message would be sent to a Discord channel with all relevant information.
![GitHub Message](https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Week%202/Images/Github%20Discord%20Message%20Example.png)
<br>

*Figure 1. An example of a message that is sent whenever a change occurs in any GitHub branch.*
<br>

Creating this webhook between these two apps allowed me to easily setup the webhook between ClickUp and Discord without the need of any form of research to help.

#### Gameplay Tags
For the character select screen to work as intended, I had to research into gameplay tags, as I knew that is what I would need to have a working character select, but I did not know anything about how they were used or any of the nodes that are linked to gameplay tags. To find out this information, I turned to the Unreal Engine gameplay tags documentation (Using Gameplay Tags in Unreal Engine | Unreal Engine 5.7 Documentation | Epic Developer Community, s.d.). Using the information gathered from this website, I was able to implement the character select screen using tags so that once a player selects a character, a tag for said character would be added to two different tag containers: one with the player's chosen character and one with all chosen characters. This allowed me to make it so that only one person can choose a character by accessing the chosen characters container and checking if each character has been chosen, and also allowed the archetypes team to access each players character individually to apply character models and voice lines to each player.

#### Character Select Screen Inspiration
When creating the base design for the character select screen, I took inspiration for the Move or Die (Move or Die on Steam, s.d.) character select/pre-game lobby screen. I found this game to have such a simple but effective UI layout that I had to take inspiration from it. What I found that made it work especially well is that the game's UI was made for four characters, which fits perfectly with the amount of characters in Greedy Piggies. Even though most of my time was spent on programming the menu, my base UI got redesigned but still kept the same layout that I originally made.
![Move or Die Screen](https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Development%20Commentary/Images/Research/Move%20or%20die%20character%20select.jpg)
<br>

*Figure 2. The character select screen used in Move or Die.*
<br>

![Base Character Select](https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Presentation/Images/Development/Character%20Select.png)
<br>

*Figure 3. The base character select screen I created.*
<br>

![Redesigned Character Select](https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Development%20Commentary/Images/Research/Redesigned%20Character%20Select.png)
<br>

*Figure 4. The redesigned character select screen after it was worked on by designers.*
<br>

#### Multiplayer

#### Steam Sessions 


### Sources

#### Jenkins
##### Jenkins Setup Guide
The YouTube tutorial I used for setting up Jenkins (How To Install Jenkins on Windows 11, 2023) was published by ProgrammingKnowledge (• • 1 et al., s.d.), a YouTuber dedicated to creating tutorials and guides for many different tools and programming languages to help people get started. 
From this video I learned how to:
- How to install Jenkins
- How to setup Jenkins
- How to create a Jenkins account
- How to access Jenkins through a web browser

This tutorial was pretty useful for the most part however I ended up having to install Jenkins from a different file type on the website since the file type shown in the video would not work on my computer. This problem then lead me to looking at the Jenkins install documentation. 

##### Jenkins Documentation
The official Jenkins documentation (Windows, s.d.) was created by the official creators of Jenkins.
Reading through the documentation taught me:
- How to setup Jenkins in a more in depth guide
- Using the windows file instead of the war file

Without using this website, I would not have been able to setup Jenkins due to the problem I was having with the war file shown on the YouTube tutorial, making this source very helpful. However I did find that the documentation website was, although laid out neatly, very cluttered with information that could be elsewhere.

#### App to Discord Webhooks
##### GitHub Webhook Documentation
The Github Webhook documentation was created by GitHub, Inc, the creators of Github.
From reading through the documentation, I learnt how to:
- How to add webhooks on GitHub
- How to create and add secret keys
- How to choose what triggers the webhook and what it has access to

Finding this website was crucial to me being able to make the GitHub webhook work with Discord as I did not know the first thing about webhooks before researching this. I found the website to be very well laid out and easy to find what you need. On the other hand, although the website goes into a lot of detail about different types of webhooks, it did not cover much outside of creating a basic webhook.

#### Gameplay Tags
##### Gameplay Tags Documentation
The gameplay tags documentation is created by Epic Games, the creators of Unreal Engine.
From researching gameplay tags through this page, I discovered how to: 
- Create a tag container
- Add tags to a container
- Find if a container contains a specific tag

In my opinion, the information provided was very bulky, making it difficult to find what I needed, but when I did find it, I was able to learn gameplay tags with ease.

#### Character Select Screen Inspiration
Move or Die was created by Those Awesome Guys, a small indie studio based in Romania. They are known for creating fast and simple party multiplayer games.
From looking into this game, I took inspiration from their character select screen as it's layout fit perfectly with what I needed the Greedy Piggies screen to look like. The only thing it was missing that I added to the Greedy Piggies UI was a ready up button that would start the game once every player was ready.

#### Multiplayer

#### Steam Sessions 



For each source, provide:

1. An **opening paragraph** describing the source's creator/publisher, reputation, and relevance.
2. A **bullet list** of what you analysed or learned from it.
3. A **closing paragraph** evaluating its usefulness or limitations.

You may include both **academic resources** and **industry examples** (e.g. documentation, games, developer talks). You are encouraged to include plenty of images, videos and diagrams.

> You should have at least 1 game source as inspiration, 1 documentation/tutorial source and 1 academic source at a minimum.

---

## Implementation *(Approx. 30–40% of word count)*

### What was your development process and how did decisions evolve?

Describe your technical and creative approach, including:

* Planning, ideation, and iteration
* Feedback received and how it was integrated
* New tools, workflows, or systems explored

#### Example Code Snippet

```csharp
using UnityEngine;

public class HelloWorld : MonoBehaviour 
{
    public void Start() 
    {
        Debug.Log("Hello World!");
    }
}
```

*Figure 2: Example code snippet using Unity's `Start()` method.*

#### Example Image

![Example](https://beforesandafters.com/wp-content/uploads/2021/05/Welcome-to-Unreal-Engine-5-Early-Access-11-16-screenshot.png)
*Figure 3: Unreal packaging menu interface.*

### What creative or technical methods did you try?

Were any methods unfamiliar or experimental? Did they succeed? Did they change your approach?

### Did you experience any technical challenges?

How did you address problems, bugs, or limitations?

---

## Testing *(Approx. 10–15% of word count)*

### What testing methods did you use?

* Did you conduct internal testing, peer testing, or user testing?
* What were your key goals in testing?
* What did you observe or learn from testing?
* How did testing influence the final result?

You may include screenshots, graphs, tables, or embedded videos to demonstrate tests and results.

| Tester | Platform | Device Specs           | Test Type      | Bugs Found | Avg. FPS | Severity (1–5) | Repro Steps Provided | Feedback Summary                                                       |
| ------ | -------- | ---------------------- | -------------- | ---------- | -------- | -------------- | -------------------- | ---------------------------------------------------------------------- |
| User A | Chrome   | i7, GTX 1060, 16GB RAM | Internal (Dev) | 3          | 60       | 2, 3, 4        | Yes                  | “Controls are responsive. Minor stutter near large particle emitters.” |
| User B | Firefox  | Ryzen 5, 8GB RAM       | Peer Playtest  | 2          | 58       | 1, 2           | No                   | “Menu system works well, but level loading feels slow.”                |
| User C | Edge     | i5, Intel UHD 620      | External User  | 5          | 45       | 2, 3, 4, 3, 2  | Yes                  | “Performance drops during explosions; some UI overlaps text.”          |
| User D | Chrome   | M1 MacBook Air         | Guided Test    | 1          | 62       | 2              | Yes                  | “Tutorial is clear. Suggested adding a visual checkpoint marker.”      |
| User E | Safari   | iPhone 12 Safari       | Blind Test     | 4          | 50       | 2, 3, 3, 4     | Partial              | “Enjoyed art style. Unclear level goals; needed more on-screen hints.” |

*Figure 4: User Testing Data.*

---

## Critical Reflection *(Approx. 10–15% of word count)*

### What went well?

* What strengths or successes stood out in the final piece?
* Did anything exceed expectations?

### What could be improved or done differently next time?

* Were there things that didn’t work? Why?
* What would you try differently with more time or resources?

---

## Bibliography
### Research
- How To Install Jenkins on Windows 11 (2023) Directed by ProgrammingKnowledge. At: https://www.youtube.com/watch?v=Zdxko2bPAAw (Accessed  11/02/2026).
- Windows (s.d.) At: https://www.jenkins.io/doc/book/installing/windows/ (Accessed  11/02/2026).
- Creating webhooks (s.d.) At: https://docs-internal.github.com/en/webhooks/using-webhooks/creating-webhooks (Accessed  19/03/2026).
- Using Gameplay Tags in Unreal Engine | Unreal Engine 5.7 Documentation | Epic Developer Community (s.d.) At: https://dev.epicgames.com/documentation/unreal-engine/using-gameplay-tags-in-unreal-engine (Accessed  01/04/2026).
- Move or Die on Steam (s.d.) At: https://store.steampowered.com/app/323850/Move_or_Die/ (Accessed  19/04/2026).


### Sources
- • • 1, 080 and Ago, 883 Views 6 Years (s.d.) YouTube. At: https://www.youtube.com/ (Accessed  19/04/2026).



---

## Declared Assets

You must declare any content that was **not entirely created by you**, or was **modified with the aid of AI tools**. This includes:

* Third-party 3D models, audio, textures, or code
* Code snippets from tutorials or forums
* AI-generated or AI-assisted assets (e.g. ChatGPT, GitHub Copilot, DALL·E)

List these clearly, with context where needed.

Example:

> The following assets were created or modified with the use of GPT-4o:
>
> * `Test.cs` – generated structure with manual revision
> * `UIAudioManager.cs` – refactored with Copilot suggestions
> * `DevelopmentJournal.html` – generated layout and headings

---

## Tips for Success

* Use plenty of **images, code snippets, drawn diagrams, tables and embedded media** to support your writing.
* Use **inline citations** for everything that influenced your work, including software and games. Include as many **hyperlinks** as possible for easier navigation to external sources.
* Reference **documentation, tutorials**, and **games** just like academic sources.
* Word count is a guideline – ±10% is allowed.
* You are allowed to use AI tools, but you **must declare** them under *Declared Assets*.