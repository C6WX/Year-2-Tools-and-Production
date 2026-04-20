---
marp: true
title: Greedy Piggies Contribution Presentation
theme: gaia
author: Callum Wade 2404781
transition: cover
style: |
  style: |
  section {
    font-size: 28px;
    position: relative;
  }

  h1 { font-size: 48px; }
  h2 { font-size: 36px; }
  h3 { font-size: 30px; }
  p  { font-size: 28px; }
  li { font-size: 25px; }

  .bottom-right {
    position: absolute;
    bottom: 40px;
    right: 40px;
    width: 150px;
  }

  .bottom-left {
    position: absolute;
    bottom: 40px;
    left: 40px;
    width: 150px;
  }

  .top-right {
    position: absolute;
    top: 40px;
    right: 40px;
    width: 150px;
  }


---

<img width="500" height="300" src="https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Presentation/Images/Greedy%20Piggies%20Title.png"> 

# Greedy Piggies Contribution Presentation <br> 
Created by 
Callum Wade <br> 2404781
<br>

--- 
# Tools 
- Jenkins
- Jenkins Webhook
- GitHub Webhook
- ClickUp Webhook
<img src="https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Presentation/Images/Tools/hammer-icon-6.png" class="bottom-right">

---
# What is Jenkins
- An open-source automation tool that automates repetitive tasks such as building the project
- It builds the game at 10 pm every day
- Whenever the pipeline runs, it:
  - Builds the game
  - Uploads the build to GitHub
  - Uses the Jenkins webhook to send a message to Discord containing a link to the build, the build status  and the build number
  - Updates the data tables that contain the build data
<img src="https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Week%204/Images/Presentation/Jenkins_logo.png" class="bottom-right">

---
# How it works
- Jenkins runs on my home PC and executes a Groovy script on the Greedy Piggies pipeline at 10 pm every day
- This pipeline then accesses the staging branch from GitHub and builds the project through the Unreal Engine build tool.
- After the code runs, it will report either success or failure 
- Success means everything has completed as expected 
- Failure means either a problem with the pipeline or that an issue exists in the project, which I would then resolve by checking the Jenkins output log
<img src="https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Week%204/Images/Presentation/Jenkins%20mechanic.png" class="bottom-right">

---
# How does this help the development
- Jenkins being integrated into the project means that no one needs to manually build the game
- Instead Jenkins does this at a specific time every day without the need for human input, removing the chance of human error
- This also allows errors to be found early, allowing them to be focused on and fixed before development continues, as at the end of the day, the game building is the most important thing
<img src="https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Week%204/Images/Presentation/Cute%20Jenkins.png" class="bottom-right">

---
# Jenkins Webhook
- Allows Jenkins to send a message to the Discord server to notify channel members of the status of the staging branch as well as providing access to the recent build
- This allows the developers to keep track of staging and allows easy access to the most recent builds of the game.
<img src="https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Week%204/Images/Presentation/jenkins-with-plate-basis-256px.png" class="bottom-right">

---
# GitHub Webhook
- Whenever a change is made in the repository, GitHub sends a message to the Discord server
- This message includes:
  - The name of the change
  - Description of the change
  - Who made the change
  - What was changed
  - A link to view the change on GitHub.com
<img src="https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Presentation/Images/Tools/GitHub-logo-3679fed488b30b5824993f62bb9a7a9b.png" class="bottom-right">

---
# How does this help the development
- Allows everyone to easily get notified whenever anyone makes a change in the repository
- Provides easier access to push reviewers as they can just click on a change on the server and will be sent straight to the change on GitHub's website with a more in-depth view of what has been changed
<img src="https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Presentation/Images/Tools/23.png" class="bottom-right">

---
# ClickUp Webhook
- Whenever a task is created or the status of a task is changed on ClickUp, a message is sent to the set Discord channel.
- These messages include:
  - Who created/changed the task
  - Who the task is assigned to
  - The name of the task 
  - The current and previous status of the task
  - Which workspace and section within the workspace the task is in 
  - A link to the workspace and to the task
- This webhook was created for the developers and designers, each with their own separate Discord channel
- The main purpose of this tool was to motivate people to use ClickUp and to also keep people notified on what has been completed or what needs to be completed
<img src="https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Presentation/Images/Tools/logo-color-medium-transparent.png" class="top-right">

---
# How does this help the development
- Keeps people notified of what tasks are still to be completed and of which tasks have been completed
- Reminds people and motivates people to keep using the ClickUp and keeping it up to date
<img src="https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Presentation/Images/Tools/programmerhumor-io-programming-memes-727c78fc25f79f0.png" class="bottom-right">


<!--
---
# My roles within this project
- GitHub Push Reviewer (Responsible)
- Automated Builds (Responsible)
- Design Liaison (Responsible)
- Ticket Reviewing (Accountable)
- ClickUp (Accountable)
- Multiplayer (Accountable) 
<img src="https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Presentation/Images/Roles/Role.png" class="bottom-right">

---
# GitHub Push Reviewer

### How I fulfilled this role:
- Implemented a GitHub webhook to the Discord server for easy access and viewing of new changes and pushes to the repository
- Kept track of changes
- Used Jenkins to fix any pushes that caused errors in any of the primary branches
<img src="https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Presentation/Images/Roles/Github.png" class="bottom-right">

---
# Automated Builds

### How I fulfilled this role:
- Implemented Jenkins into the project to automatically build the game every day
- Added a webhook for Jenkins so everyone knows when the game built and the status of the build
- Further worked on Jenkins to upload the build that is created to GitHub with a new tag so that new and old versions of the build are accessible online
- Added to the pipeline's code so that Jenkins uses Python to create and update data tables that display the time to build and status of each build 

### What I could have done better:
- Implementing Jenkins sooner into the project
- Fixing the issue that caused it to not build automatically some days
<img src="https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Week%204/Images/Presentation/Jenkins%20Trophy.png" class="bottom-right">

---
# Design Liaison

### How I fulfilled this role:
- Provided all the designers with access to the repository and set their permission levels
- Communicated with the designers whenever something needed clarification

### What I could have done better:
- Checking in on the designers more often

### Why I felt this role didn't work:
- Due to the high amount of departments and people working on the project, everyone would just speak to the specific designers themselves if they needed to clear something up as it is much easier than asking a liaison, which makes sense and is why I felt that this role didn't work for this project
<img src="https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Presentation/Images/Roles/Talking-Ben-PNG-Free-Image.png" class="top-right">

---
# Ticket Reviewing

### How I fulfilled this role:
- Contacted and helped anyone who I could that uploaded a ticket that hadn't already been accepted
<img src="https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Presentation/Images/Roles/IT%20meme.jpg" class="bottom-right">

---
# ClickUp

### How I fulfilled this role:
- Created a ClickUp webhook that would notify the departments that used it when a change was made in their own ClickUp workspace
<img src="https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Presentation/Images/Roles/Clickup.png" class="bottom-right">

---
# Multiplayer

### How I fulfilled this role:
- Worked on the original multiplayer and created the server browser to allow players to find and connect to other players through a server list or by joining through Steam friends
<img src="https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Presentation/Images/Roles/multiplayer%20meme.jpg" class="bottom-right">

-->
---
# Contributions to the development of Greedy Piggies
- The majority of my work was focussed on the UI menu screens and the multiplayer of Greedy Piggies as they were tied very closely together
- I started by creating the first version of the multiplayer script that allowed players to connect by LAN in the server browser and create game screens and then I moved onto helping with getting online connections working while also creating more menus and improving existing ones with more game ready features.
<img src="https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Presentation/Images/Development/Game%20dev%20meme.jpg" class="bottom-right">

---
# Menu Screens
- The menus were originally created to test the multiplayer but ended up being used as the basis for the menus to be designed using
- These menus included:
  - Main Menu Prototype
  - Create Game
  - Server Browser
  - Server Browser Item
  - Pause Menu Prototype
  - Character Select Screen
<img src="https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Presentation/Images/Development/pngtree-game-over-text-effect-design-screen-ui-menu-png-image_6008809.png" class="bottom-right">

---
# Main Menu Prototype
- The main menu that I created allows the player to choose between creating a lobby or going to the server browser to search for one
<img width="1000" height="600" src="https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Presentation/Images/Development/Main%20Menu.png"> 

<!--
---
# Difficulties & Research
- There wasn't any coding issues when making the main menu due to it's simplicity, however I did use a Youtube tutorial for the base layout as it was 
-->
---
# Create Game
- The create game menu lets the player decide the maximum number of players that can join their lobby as well as if the lobby is online or LAN
<img width="1000" height="600" src="https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Presentation/Images/Development/Create%20Game.png"> 

---
# Difficulties & Research
- At first the create game section used the build in Unreal Engine session nodes which I followed a YouTube tutorial* to understand how to create online sessions through Unreal Engine
- This worked for creating LAN sessions but after testing found it didn't work with Steam sessions
- Then I looked into advanced Steam session so that the game could run on Steam servers and could be tested online
- To do this, I used the advanced Steam sessions plugin page** and a YouTube tutorial***



*(Hosting, Finding and Joining Sessions | 04 | Multiplayer Battle Royale | Tutorial | Unreal Engine 5, 2023)
**(ItsMeBroYT, 2026)
***(UE5 Steam Multiplayer EP1 – Basic Connection Logic (No UI), 2026)

---
# Server Browser
- The server browser searches for lobbies and displays each found lobby as a server browser item
- Buttons at the top of the menu allow players to search for only LAN lobbies and also refresh the lobby list
<img width="1000" height="600" src="https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Presentation/Images/Development/Server%20Browser.png"> 

---
# Difficulties & Research
- When creating the server browser, I had the same problem as before where advanced sessions where required to use Steam sessions to play and test the game
- A major problem that I was fixing for a while was fake sessions appearing in the server browser
- I attempted to fix this by getting the session details and if there wasn't any actual players, a connection signal or a session name, however this didn't fix the problem as some sessions thought they had all those things
- Once the game was working on Steam, I was able to fix this problem by using the Steam sessions plugin to get players' Steam names so that any sessions without a Steam ID wouldn't be able to show in the server browser.

<img width="1000" height="600" src="https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Presentation/Images/Development/Fake%20Sessions.png"> 

---

# Server Browser Item
- The server browser item appears in the server browser once for each lobby found and displays the lobby name, the amount of players in the lobby, the connection/ping and a check box to choose that lobby
<img width="1000" height="600" src="https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Presentation/Images/Development/Server%20Browser%20Item.png"> 

---

# Difficulties & Research
- The same advanced sessions tutorial was used for the server browser item
- However this tutorial didn't have everything that was needed for this server browser so after testing the use of tick boxes and session details, I was able to create a script that would allow the player to tick a session they want to join and then press join game, which would get the ticked session details, set it as the selected session variable and then send them into the selected session.
- Another thing I added to the tutorial's server item was a player count that used shapes instead of text, to do this I used the set color and opacity node and then used the player count session detail to set the circles pink for each player in that session

---

# Pause Menu Prototype
- The pause menu has buttons that resume the game, leave the current session and quit the whole game
<img width="1000" height="600" src="https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Presentation/Images/Development/Pause%20Menu.png"> 

---
# Difficulties & Research
- The leave session button wasn't easy to test until the game was put onto steam due to the code used but even on Steam it still doesn't work as intended
- I have been researching how to leave a session but they all keep coming back with the exact same thing that I am currently doing
- This button will continue to be worked on but may need to be removed from the menu for the release if a solution can't be found
---

# Character Select Screen
- The character select screen is used as a pre-game lobby to allow players to pick their characters
- Once players have picked their character, they can ready up. Once all players are ready, they are sent into the main game
- This menu was originally created as just a basic pre-game lobby as a possible solution to fix a problem with players not seeing each other in the game but ended up turning into a working character select screen
<img width="1000" height="300" src="https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Presentation/Images/Development/Character%20Select.png"> 

---
# Difficulties & Research
- The main difficulties with this UI came with the buttons and getting it working for online sessions
- To make the base UI and code, I used a tutorial*. The reason I didn't stick with this code was due to it being basic and not fully covering everything that I need it to.
- To develop the character select screen, I researched into tags** and used them to set a selected character variable and taken character variable to store the chosen characters
- This worked for the most part until it was tested in online sessions, which I then found out that the events need to be called over the server to save the variables as the same tags for each player

*(Make a Multiplayer Game in Unreal Engine 5 - Character Selection - Unreal Beginner Tutorial # 16, 2022)
**(Using Gameplay Tags in Unreal Engine | Unreal Engine 5.7 Documentation | Epic Developer Community, s.d.)

---
# Difficulties & Research
- Once a player selects a character, the character's image would black out and no longer allow anyone to click it
- A difficult problem occurred when getting this to work as the characters you couldn't select wasn't the same for each player
- I managed to resolve this issue by changing the blueprint that handled the variable so that all players were using the same variable with the same value.
<br>
- This exact same problem occurred when making the ready up button as players all had variables that weren't being shared properly so no one could see if everyone was ready or not
- This ended up having the same solution as the character buttons where it needed to be handled by a different blueprint

---
# Bibliography
- Hosting, Finding and Joining Sessions | 04 | Multiplayer Battle Royale | Tutorial | Unreal Engine 5 (2023) Directed by Kekdot. At: https://www.youtube.com/watch?v=YUPZ1j_9Vzw (Accessed  18/02/2026).
- ItsMeBroYT (2026) ItsMeBroYT/IMB_SteamSessionTutorial. At: https://github.com/ItsMeBroYT/IMB_SteamSessionTutorial (Accessed  25/03/2026).
- UE5 Steam Multiplayer EP1 – Basic Connection Logic (No UI) (2026) Directed by It’s Me Bro. At: https://www.youtube.com/watch?v=KNeRVpPvl-w (Accessed  25/03/2026).
- Make a Multiplayer Game in Unreal Engine 5 - Character Selection - Unreal Beginner Tutorial # 16 (2022) Directed by GameDevRaw. At: https://www.youtube.com/watch?v=9f-feH2gP-o (Accessed  13/03/2026).
- Using Gameplay Tags in Unreal Engine | Unreal Engine 5.7 Documentation | Epic Developer Community (s.d.) At: https://dev.epicgames.com/documentation/unreal-engine/using-gameplay-tags-in-unreal-engine (Accessed  17/04/2026).






