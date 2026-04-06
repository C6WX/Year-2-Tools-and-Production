---
marp: true
title: Greedy Piggies Contribution Presentation
theme: gaia
author: Callum Wade 2404781
transition: cover
style: |
  section {
    font-size: 28px;
  }

  h1 {
    font-size: 48px;
  }

  h2 {
    font-size: 36px;
  }

  h3 {
    font-size: 30px;
  }

  p {
    font-size: 28px;
  }

  li {
    font-size: 25px;
  }

---

<img width="800" src=""> 

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

---
# What is Jenkins
- An open source automation tool that automates repetitive tasks such as building the project
- It builds the game at 10pm every day
- Whenever the pipeline is run it:
  - Builds the game
  - Uploads the build to GitHub
  - Uses the Jenkins webhook to send a message to Discord that contains a link to the build, the status of the build and the build number
  - Updates the data tables that contain the build data

---
# How it works
- Jenkins runs on my home PC and runs a groovy script on the Greedy Piggies pipeline at 10pm everyday
- This pipeline then accesses the staging branch from GitHub and builds the project through the Unreal Engine build tool.
- After the code is run, it will either say success or failed 
- Success means it has done everything it is supposed to do, as stated in the previous slide
- Failed means that there is either a problem with the pipeline or that something is wrong with the project, which by that point I would resolve the problem by looking through the Jenkins output log

---
# How does this help the development
- Jenkins being integrated into the project means that no one is required to manually build the game periodically.
- Instead Jenkins does this at a specific time every day without the need for human input, removing the chance of any human error. 
- This also allows errors to be found early, allowing them to be focused on and fixed before development continues, as at the end of the day, the game building is the most important thing.
---
# Jenkins Webhook
- Allows Jenkins to send a message to the Discord server to notify channel members the status of the staging branch as well as providing access to the recent build
- This allows the developers to keep track of staging and allows easy access to the most recent builds of the game.
---
# GitHub Webhook
- Whenever a change is completed anywhere in the repository, GitHub sends a message to the Discord server
- This message includes:
  - The name of the change
  - Description of the change
  - Who made the change
  - What was changed
  - A link to view the change on GitHub.com
---
# How does this help the development
- Allows everyone to easily get notified whenever anyone makes a change in the repository
- Provides easier access to push reviewers as they can just click on a change on the server and will be sent straight to the change on GitHub's website with a more in-depth view of what has been changed
---
# ClickUp Webhook
- Whenever a task is created or the status of a task is changed on ClickUp, a message is sent on the set Discord channel.
- These messages include:
  - Who created/changed the task
  - Who the task is assigned to
  - The name of the task 
  - The current and previous status of the task
  - Which workspace and section within the workspace the task is in 
  - A link to the workspace and to the task
- This webhook was created for the developers and designers, each with their own separate Discord channel
- The main purpose of this tool was to motivate people to use the ClickUp and to also keep people notified on what has been completed or what needs to be completed

---
# How does this help the development
- Keeps people notified of what tasks are still to be completed and of which tasks have been completed
- Reminds people and motivates people to keep using the ClickUp and keeping it up to date
---
# My roles within this project
- GitHub Push Reviewer (Responsible)
- Automated Builds (Responsible)
- Design Liaison (Responsible)
- Ticket Reviewing (Accountable)
- Clickup (Accountable)
- Multiplayer (Accountable) 
---
# GitHub Push Reviewer

### How I fulfilled this role:
- Implemented a GitHub webhook to the Discord server to easy access and viewing of new changes and pushes to the repository
- Kept track of changes
- Used Jenkins to fix any pushes that caused errors to any of the primary branches
---
# Automated Builds

### How I fulfilled this role:
- Implemented Jenkins into the project to automatically build the game every day
- Added a webhook for Jenkins so that everyone would know when the game built and the status of the build
- Further worked on Jenkins to upload the build that is created to GitHub with a new tag so that new and old versions of the build are accessible online
- Added to the pipelines code so that Jenkins uses Python to create and update data tables that display the time to build and status of each build 

### What I could have done better:
- Implementing Jenkins sooner into the project
- Fixing the issue that cause it to not build automatically some days

---
# Design Liaison

### How I fulfilled this role:
- Provided all the designers with access to the repository and set their permission levels
- Communicated with the designers whenever something needed clearing up

### What I could have done better:
- Checking in on the designers more often

### Why I felt this role didn't work:
- Due to the high amount of departments and people working on the project, everyone would just speak to the specific designers themselves if they needed to clear something up as it is much easier then asking a liaison, which makes sense and is why I felt that this role didn't work for this project
---
# Ticket Reviewing

### How I fulfilled this role:
- Contacted and helped anyone who I could that uploaded a ticket that hadn't already been accepted
---
# Clickup

### How I fulfilled this role:
- Created a ClickUp webhook that would notify the departments that used it when a change was made in their own ClickUp workspace
---
# Multiplayer

### How I fulfilled this role:
- Worked on the original multiplayer and created the server browser to allow players to find and connect to other players through a server list or by joining through Steam friends
---
# Contributions to the development of Greedy Piggies

---
# Prototype Menus

---
# Server Browser

---
# Character Select Screen

---

