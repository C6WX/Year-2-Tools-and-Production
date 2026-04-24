# Development Commentary

**Unit Name:** Tools and Production

**Student Name:** Callum Wade

**Student ID:** 2404781

**Total Word Count:** 6,157
<!--
**API Reference Link:** \[URL]
--->
**Tool Guide Link:** https://github.com/C6WX/Year-2-Tools-and-Production/blob/main/Shared%20Documentation/Github%20Tool%20Change%20Guide/GitHub%20Change%20Webhook%20Tool%20Guide.pdf

**Build Link:** https://store.steampowered.com/app/4463930/Greedy_Piggies/

**Task 1:** https://github.com/C6WX/Year-2-Tools-and-Production/blob/main/Week%201/Tool%20Ideation.pdf

**Task 2:** https://github.com/C6WX/Year-2-Tools-and-Production/blob/main/Week%202/Data%20Handling%20%26%20Automation.pdf

**Task 3:** https://github.com/C6WX/Year-2-Tools-and-Production/blob/main/Week%203/Networking%2C%20Multiplayer%20%26%20Compliance.pdf

**Task 4:** https://github.com/C6WX/Year-2-Tools-and-Production/blob/main/Week%205/Web%20Services%20%26%20Online%20Integration.pdf

**Task 5:** https://github.com/C6WX/Year-2-Tools-and-Production/blob/main/Week%206/Analytics%2C%20Databases%20%26%20Backends.pdf

**Task 6:** https://github.com/C6WX/Year-2-Tools-and-Production/blob/main/Week%207/Platforms%2C%20Hardware%20%26%20System%20Administration.pdf

**Presentation File:** https://github.com/C6WX/Year-2-Tools-and-Production/blob/main/Presentation/Greedy%20Piggies%20Contribution%20Presentation.pdf

**Presentation Video:** https://youtu.be/3yIZ7oq24LU | https://ucreative-my.sharepoint.com/personal/2404781_students_ucreative_ac_uk/_layouts/15/stream.aspx?id=%2Fpersonal%2F2404781_students_ucreative_ac_uk%2FDocuments%2FAttachments%2F2026-04-21%2011-26-47%2Emkv&ct=1776979260860&or=OWA-NT-Mail&cid=a9cd5614-f6de-bc19-fefd-cc1aab7af23a&ga=1&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview%2Ebc5decf4-d8c4-411f-b3e0-1f0dbf628ed8

**Personal Repository:** https://github.com/C6WX/Year-2-Tools-and-Production

---

## Abstract *(Approx. 5–10% of word count)* 379 words
This development commentary covers all of my work whilst developing Greedy Piggies. The work covered consists of:
- Jenkins
- GitHub Webhook
- Clickup Webhook
- Creating the game's multiplayer
- Creating the UI for the multiplayer
- Creating the character select screen

Within this project, my tasks primarily consisted of creating automation tools to build the game, creating tools to improve workflow, reviewing GitHub pushes and programming the game's multiplayer. These tasks weren't my original ones but were altered and adapted from a RACI chart. My original roles also included design liaison and HR department, however I felt that these roles fell through as there was no need for the HR department within this project and in terms of conversing with the designers, everyone ended up talking to them themselves due to all the small departments that appeared and disappeared throughout the development of the game, meaning communication was easiest without a middle man in the way.

My goals for this project were to release a game on Steam that had a working multiplayer system that I helped develop, and to improve the game's development process with the tools I created and implemented into the development cycle.

I approached this project by first ordering my tasks by level of importance, which led me to start with the multiplayer menu, then move on to Jenkins to build the staging branch of the game. However, it did not end up panning out this way, as a lot of problems arose from the multiplayer at varied points of the game's development, as well as new tool ideas to implement and more things for me to make or improve. For example, I realised that the ClickUp page was created to keep the developers and designers on track and to allow everyone to see what still needs to be done and what has been done. But due to its lack of use, I added a webhook to the Discord server to notify people of the progress updates from ClickUp so that people would feel more inclined to use it. 

Something else that threw off my original approach was creating all the original UI and the character select screen, as it was not part of the original plan, but was only thought of because of an error with the multiplayer. 

---

## Research *(Approx. 20-30% of word count)* 1564 words

### What sources or references have you identified as relevant to this task? 966

#### Jenkins 206
To be able to implement Jenkins into the project so that it could automatically build the staging branch, I first had to research how to set up Jenkins and how to use it. At first, I started off by following a tutorial that covered downloading and installing Jenkins (How To Install Jenkins on Windows 11, 2023). At first, I struggled to find the right tutorial for setting this up, but this video was able to help me get Jenkins installed and working. During the install process, I did have trouble with finding which version to use and using the setup wizard, but after looking into the official documentation, I was able to install the right version and continue following along with the video (Windows, s.d.). 

Once Jenkins was set up, I then went on to researching how I would go about creating a pipeline. I started by watching videos and looking at documentation, but they ended up not covering what I was trying to use Jenkins to do. So after that, I then went on to ask for help from my lecturer, who had used Jenkins before, who then provided me with a base code to use with Jenkins. After tweaking the code a bit, I was able to get Jenkins working on the staging branch.

#### App to Discord Webhooks 183
I used webhooks three times during this project, one was programmed into the Groovy script to link Jenkins to Discord, the second was to link GitHub to Discord, and the third was to link ClickUp to Discord.

When linking Jenkins and Discord, I didn't use any sources due to using AI to improve my code. I did research into linking GitHub to Discord. I wanted to create a webhook between the two apps so that ticket reviewers would get updates as soon as anything is changed on GitHub in an easy-to-read message format. To do this, I found the official GitHub documentation (Creating webhooks, s.d.) that covers creating and using webhooks on GitHub. Looking through this documentation and using AI to help with the Discord side of the webhook allowed me to set up a link between the two websites so that whenever a change occurred on GitHub, a message would be sent to a Discord channel with all relevant information.
![GitHub Message](https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Week%202/Images/Github%20Discord%20Message%20Example.png)
<br>

*Figure 1. An example of a message that is sent whenever a change occurs in any GitHub branch.*
<br>

Creating this webhook between these two apps allowed me to easily set up the webhook between ClickUp and Discord without the need for any research.

#### Gameplay Tags 168
For the character select screen to work as intended, I had to research gameplay tags, as I knew that was what I would need to have a working character select, but I did not know anything about how they were used or any of the nodes that are linked to gameplay tags. To find out this information, I turned to the Unreal Engine gameplay tags documentation (Using Gameplay Tags in Unreal Engine | Unreal Engine 5.7 Documentation | Epic Developer Community, s.d.). Using the information gathered from this website, I was able to implement the character select screen using tags so that once a player selects a character, a tag for said character would be added to two different tag containers: one with the player's chosen character and one with all chosen characters. This allowed me to make it so that only one person can choose a character by accessing the chosen character's container and checking if each character has been chosen, and also allowed the archetypes team to access each player's character individually to apply character models and voice lines to each player.

#### Character Select Screen Inspiration 101
When creating the base design for the character select screen, I took inspiration from the Move or Die (Move or Die on Steam, s.d.) character select/pre-game lobby screen. I found this game to have such a simple but effective UI layout that I had to take inspiration from it. What I found that made it work especially well is that the game's UI was made for four characters, which fits perfectly with the number of characters in Greedy Piggies. Even though most of my time was spent on programming the menu, my base UI got redesigned, but still kept the same layout that I originally made.
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

*Figure 4. The redesigned character select screen after it was worked on by Lilly.*
<br>

#### Multiplayer and Audience 305
When working on the multiplayer for Greedy Piggies, I decided to research player types for the game's target audience. When looking through different people's work, I came across a book by Peter Vorderer and Jennings Bryant (Vorderer and Bryant, 2012), which discussed many different player archetypes that I had not previously heard of. Previously, I had researched Bartle's Taxonomy (Kumar et al., 2026), which breaks down players into four categories: the achiever, the explorer, the socialiser and the killer. For Greedy Piggies, the player base is likely to be split between the socialiser, as it is a party game, and the killer, since the game is all about beating other players. However, after reading Playing Video Games: Motives, Responses, and Consequences, I found myself thinking deeper into what fits the game's player base, as the book discusses more than four player types. "Some more prominent types are identified as: The Competitor, The Explorer, The Collector, The Achiever, The Joker, The Director, The Storyteller, The Performer, and The Craftsmen." After looking into what is said about each type of player, I feel like the audience of Greedy Piggies fits into four of these categories: the competitor, the achiever, the joker and the director. The reason I believe this is due to the competitor is always focussed on beating others and being the best, and Greedy Piggies is all about competition, the achiever who is want to be the best in rankings and have the most wins, in the game players can track their wins within a group of friends, the joker is all about playing for fun and enjoying the social aspects of the game, which Greedy Piggies is focused on being social and having fun, and the director who always wants to lead a group, which a leader of a friend group would be able to do to organise playing Greedy Piggies together.



### Sources 598 words

#### Jenkins
##### Jenkins Setup Guide 122
The YouTube tutorial I used for setting up Jenkins (How To Install Jenkins on Windows 11, 2023) was published by ProgrammingKnowledge (• • 1 et al., s.d.), a YouTuber dedicated to creating tutorials and guides for many different tools and programming languages to help people get started. 
From this video, I learned how to:
- How to install Jenkins
- How to set up Jenkins
- How to create a Jenkins account
- How to access Jenkins through a web browser

This tutorial was pretty useful for the most part; however, I ended up having to install Jenkins from a different file type on the website since the file type shown in the video would not work on my computer. This problem then led me to look at the Jenkins install documentation. 

##### Jenkins Documentation 93
The official Jenkins documentation (Windows, s.d.) was created by the official creators of Jenkins.
Reading through the documentation taught me:
- How to set up Jenkins in a more in-depth guide
- Using the Windows file instead of the war file

Without using this website, I would not have been able to set up Jenkins due to the problem I was having with the war file shown on the YouTube tutorial, making this source very helpful. However, I did find that the documentation website was, although laid out neatly, very cluttered with information that could be elsewhere.

#### App to Discord Webhooks
##### GitHub Webhook Documentation 124
The GitHub Webhook documentation was created by GitHub, Inc, the creators of GitHub.
From reading through the documentation, I learnt how to:
- How to add webhooks on GitHub
- How to create and add secret keys
- How to choose what triggers the webhook and what it has access to

Finding this website was crucial to me being able to make the GitHub webhook work with Discord, as I did not know the first thing about webhooks before researching this. I found the website to be very well laid out and easy to find what you need. On the other hand, although the website goes into a lot of detail about different types of webhooks, it does not cover much outside of creating a basic webhook.

#### Gameplay Tags
##### Gameplay Tags Documentation 74
The gameplay tags documentation is created by Epic Games, the creators of Unreal Engine.
From researching gameplay tags through this page, I discovered how to: 
- Create a tag container
- Add tags to a container
- Find if a container contains a specific tag

In my opinion, the information provided was very bulky, making it difficult to find what I needed, but when I did find it, I was able to learn gameplay tags with ease.

#### Character Select Screen Inspiration 84
Move or Die was created by Those Awesome Guys, a small indie studio based in Romania. They are known for creating fast and simple party multiplayer games.
From looking into this game, I took inspiration from their character select screen, as its layout fit perfectly with what I needed the Greedy Piggies screen to look like. The only thing it was missing that I added to the Greedy Piggies UI was a ready-up button that would start the game once every player was ready.

#### Multiplayer and Audience 108
Playing Video Games: Motives, Responses, and Consequences was written by Peter Vorderer and Jennings Bryant, two key figures in media psychology. They study how people interact with media, including games, TV and digital platforms.
From reading their book, I learnt:
- Another version of player taxonomy
- How players interact with different types of games

From what I was able to read of this book online, I felt like it was able to go really in depth about everything to do with player types in an easy-to-understand and read format. However, due to the high number of topics that the book covers, it is difficult to find what you need. 

---

## Implementation *(Approx. 30–40% of word count)*

### What was your development process and how did decisions evolve?

#### Jenkins 401 words
After researching and setting up Jenkins, I was given a base code that I used to set up a test pipeline. This pipeline was used to build a random repository on my GitHub account at 10 pm every day. The reason behind my testing on another repository first was that I did not want to risk making any mistakes on the staging branch of Greedy Piggies. After the pipeline was successful, I then went on to create a pipeline for the staging branch of Greedy Piggies that was once again built at 10 pm every day.

``` Groovy
pipeline {
    agent { label 'windows' }

    options {
        buildDiscarder(logRotator(numToKeepStr: '30'))
        disableConcurrentBuilds()
    }

    environment {
        UE_ROOT      = "C:/Program Files/Epic Games/UE_5.6"
        PROJECT_PATH = "${WORKSPACE}/Santa_Trackers/Santa_Trackers.uproject"
        UE_CONFIG    = "Development"
        BUILD_DIR    = "BuildOutput"
        ZIP_DIR      = "Builds"
        ZIP_NAME     = "Greedy_Piggies_Win64_${BUILD_NUMBER}.zip"
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: '##################',
                    credentialsId: '##########'
            }
        }

        stage('Sanity Check') {
            steps {
                bat """
                if not exist "%UE_ROOT%/Engine/Build/BatchFiles/RunUAT.bat" exit /b 2
                if not exist "%PROJECT_PATH%" exit /b 3
                """
            }
        }

        stage('Build Unreal Project') {
            steps {
                bat """
                "%UE_ROOT%/Engine/Build/BatchFiles/RunUAT.bat" ^
                  BuildCookRun ^
                  -project="%PROJECT_PATH%" ^
                  -noP4 ^
                  -platform=Win64 ^
                  -clientconfig=%UE_CONFIG% ^
                  -build -cook -stage -pak -archive ^
                  -archivedirectory="%WORKSPACE%/%BUILD_DIR%"
                """
            }
        }

    }
}
```
<br>

*Figure 5. The base code that built staging and returned whether it was successful or not.*
<br>

Once I had the basic pipeline working, I looked into having Jenkins send a message to Discord that contained the details on each Jenkins run. I was able to do this by creating a webhook that linked Jenkins and Discord and then adding to the Groovy code within the pipeline so that whenever Jenkins was successful, the message would display: SUCCESS Greedy Piggies Staging (Build Number). Otherwise, if the build were to fail, it would display: FAILED Greedy Piggies Staging (Build Number). 

```Groovy
        success {
            withCredentials([string(credentialsId: 'discord-webhook-greedy-piggies', variable: 'WEBHOOK')]) {
                bat """
                curl -H "Content-Type: application/json" ^
                -X POST ^
                -d "{\\"content\\":\\"SUCCESS: ${env.JOB_NAME} #${env.BUILD_NUMBER} 
                %WEBHOOK%
                """
            }
        }

        failure {
            withCredentials([string(credentialsId: 'discord-webhook-greedy-piggies', variable: 'WEBHOOK')]) {
                bat """
                curl -H "Content-Type: application/json" ^
                -X POST ^
                -d "{\\"content\\":\\"FAILED: ${env.JOB_NAME} #${env.BUILD_NUMBER}\\"}" ^
                %WEBHOOK%
                """
            }
        }
```
<br>

*Figure 6. The code that was added to the pipeline to send GitHub messages of each build status.*
<br>

![Original Jenkins Message](https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Development%20Commentary/Images/Implementation/Jenkins/Orignial%20Jenkins%20Message.png)
<br>

*Figure 7. The message that was sent whenever Jenkins was successful with a build.*
<br>

![Original Jenkins Message](https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Development%20Commentary/Images/Implementation/Jenkins/Original%20Jenkins%20Message%20Fail.png)
<br>

*Figure 8. The message that was sent whenever Jenkins was unsuccessful with a build.*
<br>

After getting feedback on how Jenkins was running, I realised that I needed to have Jenkins upload each of these builds to GitHub so that they can be easily accessed and tested by anyone working on the game. I was able to implement this by updating the pipeline code with a new section that zips the build, archives it and then uploads it as a new GitHub release. Whilst working on this, I decided to add to the GitHub webhook code so that it would link to the new release, making it even more accessible to anyone on the Discord.

```Groovy
stage('Zip Build') {
            steps {
                powershell """
                  \$zipDir  = Join-Path \$env:WORKSPACE \$env:ZIP_DIR
                  \$zipPath = Join-Path \$zipDir \$env:ZIP_NAME
                  \$srcPath = Join-Path \$env:WORKSPACE \$env:BUILD_DIR

                  if (!(Test-Path \$zipDir)) { New-Item -ItemType Directory \$zipDir | Out-Null }
                  if (Test-Path \$zipPath) { Remove-Item -Force \$zipPath }

                  Compress-Archive -Path (Join-Path \$srcPath '*') -DestinationPath \$zipPath
                """
            }
        }

        stage('Archive Build') {
            steps {
                archiveArtifacts artifacts: 'Builds/*.zip', fingerprint: true
            }
        }

        stage('Publish GitHub Release') {
            steps {
                withCredentials([string(credentialsId: 'github-token', variable: 'GITHUB_TOKEN')]) {
                    bat """
                    set GH_TOKEN=%GITHUB_TOKEN%

                    "%GH_EXE%" release create %RELEASE_TAG% ^
                      "%WORKSPACE%\\%ZIP_DIR%\\%ZIP_NAME%" ^
                      --repo %GH_REPO% ^
                      --title "%RELEASE_NAME%" ^
                      --notes "Automated Jenkins build."

                    "%GH_EXE%" release view %RELEASE_TAG% ^
                      --repo %GH_REPO% ^
                      --json url ^
                      --jq ".url" > release_url.txt
                    """
                }

                script {
                    env.RELEASE_URL = readFile('release_url.txt').trim()
                }
            }
        }
```
<br>

*Figure 9. Code that was added to the pipeline to zip the build, archive it locally and then upload it as a GitHub release.*
<br>

``` Groovy
success {
            withCredentials([string(credentialsId: 'discord-webhook-greedy-piggies', variable: 'WEBHOOK')]) {
                bat """
                curl -H "Content-Type: application/json" ^
                -X POST ^
                -d "{\\"content\\":\\"SUCCESS: ${env.JOB_NAME} #${env.BUILD_NUMBER} ^| GitHub Release: ${env.RELEASE_URL}\\"}" ^
                %WEBHOOK%
                """
            }
        }

        failure {
            withCredentials([string(credentialsId: 'discord-webhook-greedy-piggies', variable: 'WEBHOOK')]) {
                bat """
                curl -H "Content-Type: application/json" ^
                -X POST ^
                -d "{\\"content\\":\\"FAILED: ${env.JOB_NAME} #${env.BUILD_NUMBER}\\"}" ^
                %WEBHOOK%
                """
            }
        }
```
<br>

*Figure 10. The updated version of the Discord webhook message code now links to the GitHub release if the build succeeds.*
<br>

![New Jenkins Message Success](https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Development%20Commentary/Images/Implementation/Jenkins/New%20Jenkins%20Success%20Message.png)
<br> 

Later in the project, I learned about CSV files and storing data, and I moved on to implementing data tracking and storing it in my Jenkins pipeline. I was able to do this with a mix of adding to the Groovy script and using Python. The two scripts communicate with each other to create and add to a CSV data table that stores each build's build number, date and time, branch, result and time to complete (in seconds). As well as the CSV data table, the pipeline now creates and adds to a graph PNG that tracks and compares each build's build time and a text document that tracks the number of total builds, successful builds, failed builds, average duration and success rate.

``` Groovy
post {
        always {
            script {
                def buildDate = new Date().format("yyyy-MM-dd HH:mm:ss")
                def buildResult = currentBuild.currentResult ?: "SUCCESS"
                def durationSeconds = (currentBuild.duration / 1000) as long

                bat """
                if not exist "%RESULTS_DIR%" mkdir "%RESULTS_DIR%"

                if not exist "%CSV_FILE%" (
                    echo BuildNumber,DateTime,Branch,Result,DurationSeconds> "%CSV_FILE%"
                )

                echo ${env.BUILD_NUMBER},${buildDate},${env.BRANCH_NAME},${buildResult},${durationSeconds}>> "%CSV_FILE%"
                """

                bat """
                if exist "%PYTHON_FILE%" (
                    "%PYTHON_EXE%" --version
                    "%PYTHON_EXE%" "%PYTHON_FILE%"
                ) else (
                    echo Python analysis script not found
                )
                """

                bat """
                if exist "%RESULTS_DIR%\\build_duration.png" copy /Y "%RESULTS_DIR%\\build_duration.png" "%WORKSPACE%\\build_duration.png"
                if exist "%RESULTS_DIR%\\build_summary.txt" copy /Y "%RESULTS_DIR%\\build_summary.txt" "%WORKSPACE%\\build_summary.txt"
                """

                if (fileExists('build_duration.png')) {
                    archiveArtifacts artifacts: 'build_duration.png', fingerprint: true
                }

                if (fileExists('build_summary.txt')) {
                    archiveArtifacts artifacts: 'build_summary.txt', fingerprint: true
                }
            }
        }
```
<br>

*Figure 11. The new addition to the groovy script to communicate with the Python script and create and update the new data files.*
<br>

```Python
import os
import pandas as pd
import matplotlib.pyplot as plt

results_dir = r"##########"

csv_file = os.path.join(results_dir, "build_results.csv")
duration_graph = os.path.join(results_dir, "build_duration.png")
summary_file = os.path.join(results_dir, "build_summary.txt")

if not os.path.exists(csv_file):
    print("CSV file not found")
    raise SystemExit(1)

df = pd.read_csv(csv_file)

df["BuildNumber"] = pd.to_numeric(df["BuildNumber"], errors="coerce")
df["DurationSeconds"] = pd.to_numeric(df["DurationSeconds"], errors="coerce")
df = df.dropna(subset=["BuildNumber", "DurationSeconds"])

if df.empty:
    print("CSV is empty after cleaning")
    raise SystemExit(1)

total_builds = len(df)
success_count = (df["Result"] == "SUCCESS").sum()
failure_count = (df["Result"] == "FAILURE").sum()
avg_duration = df["DurationSeconds"].mean()
success_rate = (success_count / total_builds) * 100 if total_builds > 0 else 0

with open(summary_file, "w", encoding="utf-8") as f:
    f.write(f"Total builds: {total_builds}\n")
    f.write(f"Successful builds: {success_count}\n")
    f.write(f"Failed builds: {failure_count}\n")
    f.write(f"Average duration: {avg_duration:.2f} seconds\n")
    f.write(f"Success rate: {success_rate:.2f}%\n")

plt.figure(figsize=(8, 5))
plt.plot(df["BuildNumber"], df["DurationSeconds"], marker="o")
plt.xlabel("Build Number")
plt.ylabel("Duration in Seconds")
plt.title("Jenkins Build Duration Over Time")
plt.grid(True)
plt.tight_layout()
plt.savefig(duration_graph)
plt.close()

print("Saved graph to:", duration_graph)
print("Saved summary to:", summary_file)

```
<br>

*Figure 12. The Python script that gathers the data from each build and creates or updates the new data files.*
<br>

```CSV
BuildNumber,DateTime,Branch,Result,DurationSeconds
40,16/03/2026 12:58,staging,SUCCESS,50
41,16/03/2026 13:01,staging,SUCCESS,23
42,16/03/2026 13:03,staging,SUCCESS,23
43,16/03/2026 13:09,staging,SUCCESS,163
44,16/03/2026 13:18,staging,SUCCESS,151
45,16/03/2026 13:30,staging,SUCCESS,152
46,2026-03-16 14:17:10,staging,SUCCESS,184
47,2026-03-16 14:24:31,staging,SUCCESS,236
49,2026-03-16 14:30:45,staging,SUCCESS,160
50,2026-03-17 22:17:12,staging,FAILURE,1024
51,2026-03-17 22:19:46,staging,ABORTED,28
52,2026-03-17 22:22:51,staging,SUCCESS,172
53,2026-03-18 22:03:31,staging,SUCCESS,200
54,2026-03-19 22:03:27,staging,SUCCESS,198
55,2026-03-22 22:59:38,staging,SUCCESS,171
56,2026-03-24 22:32:23,staging,SUCCESS,204
57,2026-03-26 18:34:24,staging,FAILURE,90
58,2026-03-26 18:50:41,staging,SUCCESS,292
59,2026-03-28 23:42:51,staging,SUCCESS,206
60,2026-03-31 22:18:31,staging,SUCCESS,214
61,2026-04-06 14:16:07,staging,SUCCESS,227
62,2026-04-11 23:54:15,staging,SUCCESS,244
63,2026-04-13 13:41:47,staging,SUCCESS,237
64,2026-04-13 14:01:30,staging,SUCCESS,225
65,2026-04-13 22:04:46,staging,SUCCESS,275
66,2026-04-14 22:08:28,staging,SUCCESS,501
67,2026-04-15 22:04:56,staging,SUCCESS,286
68,2026-04-17 14:28:17,staging,FAILURE,19
69,2026-04-17 14:33:15,staging,SUCCESS,242
```
<br>

*Figure 13. The CSV file that was output by the Python script.*
<br>

```
Total builds: 29
Successful builds: 25
Failed builds: 3
Average duration: 213.69 seconds
Success rate: 86.21%
```
<br>

*Figure 14. The text file that was output by the Python script. The reason there are more total builds than successful and failed builds combined is that it does not separately track aborted builds.*
<br>

![Build Duration Table](https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Development%20Commentary/Images/Implementation/Jenkins/build_duration.png)
<br>

*Figure 15. The data table that was output by the Python script. The spike in time for build 50 was due to internet connectivity issues.*

```Groovy
pipeline {
    agent { label 'windows' }

    options {
        buildDiscarder(logRotator(numToKeepStr: '30'))
        disableConcurrentBuilds()
    }

    environment {
        UE_ROOT      = "C:\\Program Files\\Epic Games\\UE_5.6"
        PROJECT_PATH = "${WORKSPACE}\\Greedy_Piggies.uproject"
        UE_CONFIG    = "Development"
        BUILD_DIR    = "BuildOutput"
        ZIP_DIR      = "Builds"
        ZIP_NAME     = "Greedy_Piggies_Win64_${BUILD_NUMBER}.zip"

        GH_EXE       = "C:\\Program Files\\GitHub CLI\\gh.exe"
        GH_REPO      = "University-for-the-Creative-Arts/Greedy_Piggies"
        RELEASE_TAG  = "build-${BUILD_NUMBER}"
        RELEASE_NAME = "Build ${BUILD_NUMBER}"

        RESULTS_DIR  = "###"
        CSV_FILE     = "####"
        PYTHON_FILE  = "####"
        PYTHON_EXE   = "####"
        BRANCH_NAME  = "staging"
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: "${env.BRANCH_NAME}",
                    url: 'https://github.com/University-for-the-Creative-Arts/Greedy_Piggies',
                    credentialsId: 'Github'
            }
        }

        stage('Sanity Check') {
            steps {
                bat """
                if not exist "%UE_ROOT%\\Engine\\Build\\BatchFiles\\RunUAT.bat" exit /b 2
                if not exist "%PROJECT_PATH%" exit /b 3
                if not exist "%GH_EXE%" exit /b 4
                if not exist "%PYTHON_EXE%" exit /b 5
                if not exist "%RESULTS_DIR%" mkdir "%RESULTS_DIR%"
                """
            }
        }

        stage('Build Unreal Project') {
            steps {
                bat """
                call "%UE_ROOT%\\Engine\\Build\\BatchFiles\\RunUAT.bat" ^
                  BuildCookRun ^
                  -project="%PROJECT_PATH%" ^
                  -noP4 ^
                  -platform=Win64 ^
                  -clientconfig=%UE_CONFIG% ^
                  -build -cook -stage -pak -archive ^
                  -archivedirectory="%WORKSPACE%\\%BUILD_DIR%"
                """
            }
        }

        stage('Zip Build') {
            steps {
                powershell """
                  \$zipDir  = Join-Path \$env:WORKSPACE \$env:ZIP_DIR
                  \$zipPath = Join-Path \$zipDir \$env:ZIP_NAME
                  \$srcPath = Join-Path \$env:WORKSPACE \$env:BUILD_DIR

                  if (!(Test-Path \$zipDir)) { New-Item -ItemType Directory \$zipDir | Out-Null }
                  if (Test-Path \$zipPath) { Remove-Item -Force \$zipPath }

                  Compress-Archive -Path (Join-Path \$srcPath '*') -DestinationPath \$zipPath
                """
            }
        }

        stage('Archive Build') {
            steps {
                archiveArtifacts artifacts: 'Builds/*.zip', fingerprint: true
            }
        }

        stage('Publish GitHub Release') {
            steps {
                withCredentials([string(credentialsId: 'github-token', variable: 'GITHUB_TOKEN')]) {
                    bat """
                    set GH_TOKEN=%GITHUB_TOKEN%

                    "%GH_EXE%" release create %RELEASE_TAG% ^
                      "%WORKSPACE%\\%ZIP_DIR%\\%ZIP_NAME%" ^
                      --repo %GH_REPO% ^
                      --title "%RELEASE_NAME%" ^
                      --notes "Automated Jenkins build."

                    "%GH_EXE%" release view %RELEASE_TAG% ^
                      --repo %GH_REPO% ^
                      --json url ^
                      --jq ".url" > release_url.txt
                    """
                }

                script {
                    env.RELEASE_URL = readFile('release_url.txt').trim()
                }
            }
        }
    }

    post {
        always {
            script {
                def buildDate = new Date().format("yyyy-MM-dd HH:mm:ss")
                def buildResult = currentBuild.currentResult ?: "SUCCESS"
                def durationSeconds = (currentBuild.duration / 1000) as long

                bat """
                if not exist "%RESULTS_DIR%" mkdir "%RESULTS_DIR%"

                if not exist "%CSV_FILE%" (
                    echo BuildNumber,DateTime,Branch,Result,DurationSeconds> "%CSV_FILE%"
                )

                echo ${env.BUILD_NUMBER},${buildDate},${env.BRANCH_NAME},${buildResult},${durationSeconds}>> "%CSV_FILE%"
                """

                bat """
                if exist "%PYTHON_FILE%" (
                    "%PYTHON_EXE%" --version
                    "%PYTHON_EXE%" "%PYTHON_FILE%"
                ) else (
                    echo Python analysis script not found
                )
                """

                bat """
                if exist "%RESULTS_DIR%\\build_duration.png" copy /Y "%RESULTS_DIR%\\build_duration.png" "%WORKSPACE%\\build_duration.png"
                if exist "%RESULTS_DIR%\\build_summary.txt" copy /Y "%RESULTS_DIR%\\build_summary.txt" "%WORKSPACE%\\build_summary.txt"
                """

                if (fileExists('build_duration.png')) {
                    archiveArtifacts artifacts: 'build_duration.png', fingerprint: true
                }

                if (fileExists('build_summary.txt')) {
                    archiveArtifacts artifacts: 'build_summary.txt', fingerprint: true
                }
            }
        }

        success {
            withCredentials([string(credentialsId: 'discord-webhook-greedy-piggies', variable: 'WEBHOOK')]) {
                bat """
                curl -H "Content-Type: application/json" ^
                -X POST ^
                -d "{\\"content\\":\\"SUCCESS: ${env.JOB_NAME} #${env.BUILD_NUMBER} ^| GitHub Release: ${env.RELEASE_URL}\\"}" ^
                %WEBHOOK%
                """
            }
        }

        failure {
            withCredentials([string(credentialsId: 'discord-webhook-greedy-piggies', variable: 'WEBHOOK')]) {
                bat """
                curl -H "Content-Type: application/json" ^
                -X POST ^
                -d "{\\"content\\":\\"FAILED: ${env.JOB_NAME} #${env.BUILD_NUMBER}\\"}" ^
                %WEBHOOK%
                """
            }
        }
    }
}
```
<br>

*Figure 16. The complete Groovy script used by the Jenkins pipeline.*
<br>

#### Webhooks 493
##### GitHub
Not including the Jenkins webhook, the first webhook I created and implemented was a GitHub webhook. The reason for adding this to the Discord webhook was that, being a GitHub reviewer, I realised early on how inconvenient it was to keep checking to see if there had been any changes to the project and then trying to access all the change details. So I looked into having GitHub send the changes straight to a Discord channel for easy access. 

Implementation started with me researching how to create a webhook between the two apps and then creating a Discord webhook, which is simple since it just requires one button press and then selecting the channel it can access.

![Discord Bot Github](https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Development%20Commentary/Images/Implementation/Webhooks/Discord%20bot%20github.png)
<br>

*Figure 17. The webhook created for GitHub to message on Discord.*
<br>
Once the bot was created, I had to finish the rest on GitHub. To start, a Discord URL is needed for GitHub to access the server. Once that is added, all that was left to do was choose what events would trigger the bot to send a message and what sort of content would be sent. The content I selected was an application/JSON, and the triggers I chose were branch creations and deletions, pushes and pull requests.

Now, whenever anyone makes a change on any branch in the Greedy Piggies repository, a message is sent to the GitHub push reviewers channel in Discord. These messages contain the username of who made the change, the branch that the change was made on, the name given to the change and a link to an in-depth version of the change.

![GitHub Webhook Creation](https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Development%20Commentary/Images/Implementation/Webhooks/GitHub%20Webhook%20setup.png)
<br>

*Figure 18. The set up page for the webhook on GitHub.*
<br>

![GitHub Change Message](https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Development%20Commentary/Images/Implementation/Webhooks/Github%20Push.png)
<br>

*Figure 19. The message sent by GitHub whenever a change occurs in the repository.*
<br>


![GitHub Branch Creation Message](https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Development%20Commentary/Images/Implementation/Webhooks/Github%20Branch%20Creation.png)
<br>

*Figure 20. The message sent by GitHub whenever a branch is created/deleted in the repository.*
<br>

##### ClickUp
I was not originally planning on making a webhook bot for ClickUp, as my roles did not have anything to do with that department. However, I realised that the ClickUp department was not very happy with the fact that it was being completely ignored by the designers. So I thought that it would be a good idea to create a webhook that would send messages straight to a designer channel to incentivise the designers to use it more and remind them that it is still a thing that they should be using.

Due to having previously made the GitHub webhook, I found this one much simpler to make; all I needed was to find the webhook section on the ClickUp workspace and get permissions to be able to manage the workspace. 
As soon as I had the correct permissions, I created a ClickUp designer channel on Discord and then located the Discord section of the website and set up the Discord bot by adjusting what channels the bot can message in and what triggers each message. The messages that are sent contain the person who adjusted a task, the name of the task, the status of the task, who the task is assigned to, the location of the task and when the task was changed.

Since creating this webhook was so simple, I also made one for the developers to help us stay on track with the project.

![ClickUp Message](https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Development%20Commentary/Images/Implementation/Webhooks/ClickUp%20message.png)
<br>

*Figure 21. A message that is sent to Discord by ClickUp.*

#### Server Browser 700 words
To start the server browser, I followed along with a tutorial (UE5 Steam Multiplayer EP1 – Basic Connection Logic (No UI), 2026) that had me create a create game menu, a server browser and a server browser item.

##### Create Game
The first menu out of these that was created was the create game menu. This menu allows the player to choose the maximum number of players in their game and whether the session is LAN or not. 

![LAN](https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Development%20Commentary/Images/Implementation/Server%20Browser/Create%20Game/LAN.png)
<br>

*Figure 22. When the LAN check box is ticked, LAN becomes true, which is then plugged into the create session setting to set the sessions as a LAN session.*
<br>

Originally, the max player amount from the tutorial was typed in by the player, but I found this was giving the player too much power and allowed lobbies to be made to have too many players. To avoid this, I implemented buttons that increased and decreased the value of the max player. Another problem was that the maximum number of players could be set to one or above four, which was either too small or too large a number than needed, so I utilised the clamp node so that the value can be controlled by not being able to go below two or above four. When the player presses the create game button, a lobby is created with the details and settings that the player adjusted.

![Max Players](https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Development%20Commentary/Images/Implementation/Server%20Browser/Create%20Game/Max%20Players.png)
<br>

*Figure 23. The top section of this script sets the max player text to the original value of the max players. The lower half increases or decreases the value of max players depending on which arrow button is pressed, and then updates the test displayed on the menu.*
<br>



The original tutorial for this allowed the player to make a LAN session, but did not work with online sessions. To get this working, I looked into advanced sessions and adjusted the script to use the plugin's nodes. After this plugin was implemented and the app ID was changed, the game worked with the Steam sessions.

![Create Game](https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Development%20Commentary/Images/Implementation/Server%20Browser/Create%20Game/Create%20Session.png)
<br>

*Figure 24. When the "Create Game" button is clicked, a session is created using the settings that the player has set, and then the main level is opened.*
<br>

The last feature I added to the create game menu was a back button that would return the player to the main menu.

![Back Button](https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Development%20Commentary/Images/Implementation/Server%20Browser/Create%20Game/Back%20Button.png)
<br>

*Figure 25. The main menu opens back up, and the " create game is removed from the player's display once the back button is pressed.*
<br>

![Create Game Full Script](https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Development%20Commentary/Images/Implementation/Server%20Browser/Create%20Game/Full%20Create%20Game%20Script.png)
<br>

*Figure 26. The complete script used to make the create game screen.*
<br>

![Original Create Game Menu Screen](https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Development%20Commentary/Images/Implementation/Server%20Browser/Create%20Game/Create%20Game%20Original.png)
<br>

*Figure 27. The original create game screen designed and created by me.*
<br>

![Create Game Menu Screen](https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Development%20Commentary/Images/Implementation/Server%20Browser/Create%20Game/Create%20Game%20menu.png)
<br>

*Figure 28. The create game screen after it was designed and updated by Lilly.*
<br>

##### Main Menu
So that the create game menu and the join game menu would be accessible, I created a main menu to allow the two screens to be selectable. The original menu that I created only had the create game and join game buttons, but once it had been worked on by designers, it also had a game manual button and a quit game button, as well as an updated and improved design.

![Create Game Button](https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Development%20Commentary/Images/Implementation/Server%20Browser/Main%20Menu/Create%20Game%20button.png)
<br>

*Figure 29. The button that removes the main menu and opens the create game menu.*
<br>

![Join Game Button](https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Development%20Commentary/Images/Implementation/Server%20Browser/Main%20Menu/Join%20Game%20Button.png)
<br>

*Figure 30.The button that removes the main menu and opens the join game menu.*
<br>

![Original Menu Screen](https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Development%20Commentary/Images/Implementation/Server%20Browser/Main%20Menu/Main%20Menu%20Original.png)
<br>

*Figure 31. A basic main menu that I created for testing purposes to easily access both menus.*
<br>

![Updated Menu Screen](https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Development%20Commentary/Images/Implementation/Server%20Browser/Main%20Menu/Updated%20Main%20Menu.png)
<br>

*Figure 32. The redesigned main menu, created by Lilly that now has a game manual button and a quit game button.*
<br>

##### Server Browser Menu
The original server browser menu was also created using the same tutorial, but once again, it didn't contain all the features needed for Greedy Piggies to work. It was missing online sessions, a back button and the ability to stop fake sessions from being created.

Online sessions were implemented by simply replacing the find sessions node with the find advanced sessions node from the plugin that allowed the game to work with Steam sessions. The menu uses this node to search for available sessions, and once it finds them, it adds a server browser item that displays session details and allows the player to tick the session they want to join.

The script for this menu works by searching for sessions from the game, then for each session found, a server browser item is created and added to a list box. When a player has located the session they want to join, they press the check box next to it and then the join game button. From there, it takes the details of the checked session and sends the player into that session. Before this happens, however, a check is run to make sure that the session isn't full by comparing the current players to the maximum number of players set on the session.

![Refresh Button](https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Development%20Commentary/Images/Implementation/Server%20Browser/Join%20Game/Refresh%20Button.png)
<br>

*Figure 33. When the UI is constructed or the refresh button is pressed, sessions are searched for, and a server browser item is displayed for each one found.*
<br>

![Join Game](https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Development%20Commentary/Images/Implementation/Server%20Browser/Join%20Game/Join%20Game.png)
<br>

*Figure 34. When the join game button is pressed, the selected server information is given to the join session node and the player is sent into the session.*
<br>

A refresh button and a search for LAN button are also working on the menu, so that the player can run the session search again, and so that the player only searches for LAN sessions. A back button is also on the menu to send the player back to the main menu.

![LAN](https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Development%20Commentary/Images/Implementation/Server%20Browser/Join%20Game/LAN.png)
<br>

*Figure 35. If the LAN button is pressed, LAN is changed to either true or false.*
<br>

![Back Button](https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Development%20Commentary/Images/Implementation/Server%20Browser/Join%20Game/Back%20Button.png)
<br>

*Figure 36. This allows the button to take the player back to the main menu.*
<br>

![Full Script](https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Development%20Commentary/Images/Implementation/Server%20Browser/Join%20Game/Full%20Script.png)
<br>

*Figure 37. The full script to allow the join game/server browser to work.*
<br>

![Original Server Browser](https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Development%20Commentary/Images/Implementation/Server%20Browser/Join%20Game/Server%20Browser.png)
<br>

*Figure 38. A basic server browser that I created.*
<br>

![Updated Server Browser](https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Development%20Commentary/Images/Implementation/Server%20Browser/Join%20Game/Updated%20Server%20Browser.png)
<br>

*Figure 39. The updated server browser, redesigned by Lilly.*
<br>

##### Server Browser Item
The server browser item is what is displayed for each session that the server browser is able to find. The original version of this UI was also created while following the same tutorial. I adjusted a few things.
The original menu from the video displayed the player count in numbers, the ping of the session and a button to select the session. I added to this some code that displayed the name of the session's host and four white circles that each turned pink based on the number of players present in the session.

![Construct](https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Development%20Commentary/Images/Implementation/Server%20Browser/Server%20Browser%20Item/Construct.png)
<br>

*Figure 40. When the item is created on the server browser, all the details are gathered and set on what they need to allow the item to display the session details.*
<br>

![Player Count](https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Development%20Commentary/Images/Implementation/Server%20Browser/Server%20Browser%20Item/Player%20Count.png)
<br>

*Figure 41. For each player who is in the session, one of the circles turns pink.*
<br>

![Check Box](https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Development%20Commentary/Images/Implementation/Server%20Browser/Server%20Browser%20Item/Check%20Box.png)
<br>

*Figure 42. The session details of the checked session are set to the current session variable for the server browser to load.*
<br>

![Full Script](https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Development%20Commentary/Images/Implementation/Server%20Browser/Server%20Browser%20Item/Full%20Script.png)
<br>

*Figure 43. The full script for the server browser item to work.*
<br>

![Original UI](https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Development%20Commentary/Images/Implementation/Server%20Browser/Server%20Browser%20Item/Original%20Server%20Browser%20Item.png)
<br>

*Figure 44. The original design I created for the server browser item.*
<br>

![Updated UI](https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Development%20Commentary/Images/Implementation/Server%20Browser/Server%20Browser%20Item/Updated%20Server%20Browser%20Item.png)
<br>

*Figure 45. The redesigned and updated version of the server browser item was done by Lilly*
<br>


#### Server Browser Videos

**[Game Host Perspective](https://youtu.be/FDixecL6ufU)**

**[Game Player Perspective](https://youtu.be/gAgglTWZ7JA)**


#### Character Select Screen 579 words
The character select screen was originally created as a way to fix a bug that would cause players to not see or interact with players who joined after them. We thought that if the players were to get together in a pre-game lobby, they would be sent to the main game together, and this would fix the issue. However, whilst the character select screen was in development, this issue was fixed with another solution. But since a character select screen was still required for the archetypes system to function, its development continued, and it was implemented into the final game. 

Before starting the development of this UI, I attempted to find tutorials that would help with the creation of the menu. However, I was unable to find one that had what Greedy Piggies required. The closest video I found (Make a Multiplayer Game in Unreal Engine 5 - Character Selection - Unreal Beginner Tutorial # 16, 2022) was able to teach me the basics of making a character selection screen, but none of the code ended up being used in the game. 

The original version of the character select screen used tags to give the player the tag based on the button they selected; this allowed multiple players to select the same characters. So another tag collection was created to store every character that is selected. This was used on each character button so that if the nepo piggy was selected, the nepo piggy button would check if that character tag is present in the collection. If it is, then the button would become deactivated for all players.

![Character Button Pressed](https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Development%20Commentary/Images/Implementation/Server%20Browser/Character%20Select/The%20Nobody%20Clicked.png)
<br>

*Figure 46. When the nobody button is clicked, the game checks that the player hasn't already picked a character, then the chosen character is added to the player's selected character tag container, and the character clicked script runs based on the character clicked.*
<br>

![Character Button Deactivating](https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Development%20Commentary/Images/Implementation/Server%20Browser/Character%20Select/The%20Nobody%20Button%20Deactivation.png)
<br>

*Figure 47. The taken characters container is checked to see if the nobody character tag is in it. If it is, then the button is deactivated, so nobody else can pick that character. This function is copied and altered for each of the four character buttons.*
<br>

![Set Characters As Taken](https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Development%20Commentary/Images/Implementation/Server%20Browser/Character%20Select/Set%20Character%20Taken.png)
<br>

*Figure 48. Based on the character selected, the server clicked function is run within the player controller blueprint.*
<br>

![Character Clicked Function](https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Development%20Commentary/Images/Implementation/Server%20Browser/Character%20Select/Character%20Clicked%20Function.png)
<br>

*Figure 49. The character that the player has chosen has its tag added to the taken characters container.*
<br>


The majority of the time that was spent on this screen was used fixing a problem that stopped players from seeing each other's selected characters. For example, player two can pick a character, and then player one can overwrite their character selection, and the only character that would become selected would be player one's choice. Also, the players who joined before another player were unable to see the choices of later joining players. This issue was fixed by using server events and having the script that sets the selected character tags for the collection moved into the player controller.

Once this problem was fixed, the rest of the time spent on this UI was spent on the ready-up button. The original script for this was simple: when the number of players who have pressed ready equals the number of players within the session, the players would be sent into the main game. However, this ended up being too simple and came with issues. For example, players were unable to unready, a player could enter a game by themselves, and players could join a game without selecting a character. To resolve these issues, code was added that allowed players to unready and changed the buttons text accordingly, as well as the number of ready players having to equal the number of current players, another and pin was added to make sure that the players ready is more than one and finally the player's selected character tag collection would be checked to make sure that they have a character tag before ready up can be pressed.

![Ready Up](https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Development%20Commentary/Images/Implementation/Server%20Browser/Character%20Select/Ready%20Up.png)
<br>

*Figure 50. When ready up is clicked, first it checks if the player has chosen a character, to avoid players entering the game without a character tag. Then a flip-flop node is used to change the player between being ready and unready whilst also matching the button's text.*
<br>

![Server Set Ready/Unready](https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Development%20Commentary/Images/Implementation/Server%20Browser/Character%20Select/Set%20ReadyUnready.png)
<br>

*Figure 51. The functions that run after the ready-up script either set the player as ready or unready and then run the check all players ready script.*
<br>

![Check All Players Ready](https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Development%20Commentary/Images/Implementation/Server%20Browser/Character%20Select/Check%20All%20Players%20Are%20Ready.png)
<br>

*Figure 52. First off, the player count is obtained from the game state's player array. Then, for each player, their ready boolean is checked to see if it's true. If it is true, then variables are ran through an and node to check if there are enough players in the session, if the players ready is equal to the player count and if there is more than one player ready, to avoid players entering the game by themselves. If all these come back true, then the start game script is run, and the UI is removed from the screen.*
<br>

Originally, this menu was in its own level within Unreal Engine; however, due to a problem with the archetype system and saving the tag collection data between levels, I changed some nodes so that the players were sent to the main game instead of the character select level and also the menu would disappear, and the game would become playable once all players were ready.

![Start Game](https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Development%20Commentary/Images/Implementation/Server%20Browser/Character%20Select/Start%20Game.png)
<br>

*Figure 53. After the character select screen is removed from player screens, each player is checked for authority to see if they are the host and then the game is started.*
<br>

![Remove UI](https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Development%20Commentary/Images/Implementation/Server%20Browser/Character%20Select/Remove%20UI.png)
<br>

*Figure 54. The UI is removed from each player's screens.*
<br>

![Full Character Select Script](https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Development%20Commentary/Images/Implementation/Server%20Browser/Character%20Select/Full%20Character%20Select%20Script.png)
<br>

*Figure 55. The full script for the character select widget blueprint.*
<br>


![Original Character Select](https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Development%20Commentary/Images/Implementation/Server%20Browser/Character%20Select/Original%20Character%20Select.png)
<br>

*Figure 56. The original character select screen I made.*
<br>

![Updated Character Select Screen](https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Development%20Commentary/Images/Implementation/Server%20Browser/Character%20Select/Redesigned%20Character%20Select.png)
<br>

*Figure 57. The updated character select screen redesigned by Lilly.*
<br>


#### Late Fixes 521 words
During the last few days of the game, I worked with Cameron, Lilly and Anna to try and get the game ready for release. Although by the end of our sessions together, the gameplay wasn't ready for release, I was able to get a handful of the features working and ready for release. 

During this process, I was uploading the game to Steam so that tests could be constantly run to make sure the fixes being made were working properly, leading to a lot of builds on Steamworks.

![Steamwork Builds](https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Development%20Commentary/Images/Implementation/Late%20Fixes/Steamworks.png)
<br>

*Figure 58. The list of game builds on Steamworks.*
<br>

Due to problems with the artists' assets not getting into the final game, I prioritised locating and preparing a scene that contained a good handful of their assets. To do this, I worked on locating and adding the artist's textures that the designers struggled to locate and added them to the scene. Unfortunately, it seemed that a mix between the asset bot and GitHub resulted in assets and textures going missing, so some assets from the scene needed to be deleted or re-textured. I was able to get the scene together and transferred game blueprints and spawns over to the new scene and replaced any references, meaning the scene with the artist's work is now the main scene in the game.

![Original Final Scene](https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Development%20Commentary/Images/Implementation/Late%20Fixes/Original%20Final%20Scene.png)
<br>

*Figure 59. The blockout scene that would've been the main game scene in the final release without this change.*
<br>

![Final Scene With Assets](https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Development%20Commentary/Images/Implementation/Late%20Fixes/Scene%20with%20assets.png)
<br>

*Figure 60. The new final scene that contains the work from the artists. This is the new main scene on the current game release.*
<br>

As well as this, I fixed input bugs caused by the gamepad. Whenever a button was pressed to change the current card, around five cards would be skipped, meaning it was accepting the button input too many times. To fix this issue, I adjusted the node connection so that the input was accepted once the player let go of the arrow key.

![Input Fix](https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Development%20Commentary/Images/Implementation/Late%20Fixes/Gamepad%20Issue%20Fix.png)
<br>

*Figure 61. Previously, the connection was coming out of triggered, but to fix the issue, it is now connected to completed.*
<br>

I was also able to fix the game starting. Until I changed it, the game would only start once the player pressed G on the keyboard, which obviously couldn't make it to the final game. So I altered this so that the game would start just after the character select screen was removed from view. The adjusted script can be seen in Figure 53.

It took me a while to figure out what was wrong with it, but during this fixing stage, I was able to fix a problem with my own server browser, where the session name wouldn't display the host's username. After some trial and error and testing, I was able to fix this issue by using advanced session nodes to access the player's nickname and set it as the session name text. Unfortunately, after further testing, we had a test where the session name was displayed as "unknown". This happened when someone tried to join my session who had never played with me before and didn't have me as a friend. I did not end up looking into this due to a lack of time, but also because some players may prefer not having their username visible to random players.

An error also occurred when merging the UI design branch into staging, which did not successfully bring over an addition to my ready-up script to change the text on the ready-up. I quickly remade this script so that players knew if they were readied up or not.

### What creative or technical methods did you try? 256 words

#### Tools
As I have never used Jenkins or Groovy before, it was all new to me. After researching Jenkins and looking into its capabilities, however. I found it simple to update the pipeline for whatever I needed. I went from having Jenkins check if staging works to having it message Discord with the job status, upload a build of the game to GitHub releases and link it in the message and use Python to create and update a CSV file, a data graph and a build status text file.

#### Development
The whole of the multiplayer programming was completely unfamiliar to me seeing as I had never made an online game before Greedy Piggies. The whole time I was working on the multiplayer, I was researching or asking for peer feedback due to the difficulty of it. Many errors were occurring due to a lack of knowledge of how multiplayer is handled. I originally thought every player would see the same thing and some variables would be shared between players automatically since the session has one host hosting the game and the players are all playing the same game. However it turns out it doesn't work like that. I needed to ask for help and was taught by Bradley about server events existing. After experimenting with different server event settings and the blueprints that different codes were handled in, as some blueprints are shared between players and some aren't, I was able to solve these issues and get the server browser and the character select screen working as intended.  

<!--
Were any methods unfamiliar or experimental? Did they succeed? Did they change your approach?


### Did you experience any technical challenges?

How did you address problems, bugs, or limitations?

-->

---

## Testing *(Approx. 10–15% of word count)*

### Server Browser 376
To check that the server browser worked, I had to upload the game build to Steam to run tests. From the first test, I discovered that fake sessions were being found and added to the server browser. When I attempted to join them, it said that there were either too many players in the sessions, while displaying that there was only one player in the session on the player count, or it would say the session didn't exist. Also, this test allowed me to realise that the session names were not working either. Instead of having the host's username as the session name, it just said session name.

![Fake Sessions](https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Development%20Commentary/Images/Testing/Fake%20Sessions.png)
<br>

*Figure 62. An example of the fake sessions issue. This session said that I could not join because the session doesn't exist.*
<br>

I started by dealing with the fake session problem first. My thought process whilst working out how to solve this issue was that if these sessions don't exist, then they shouldn't have any players and shouldn't have a proper connection signal. So I added branches into the code so that the sessions would only appear if the session has at least one player and a valid signal.

![Fake Sessions fix attempt](https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Development%20Commentary/Images/Testing/Fake%20Sessions%20First%20Attempt%20Fix.png)
<br>

*Figure 63. The first fix I attempted for the fake sessions issue.*
<br>

However, after running another Steam test, it turned out that this solution did not fix the issue. I decided to put this problem on hold for now and attempt to fix the other issue with the session name. After looking further into the nodes that are included with the advanced sessions plugin, I found a unique net ID to string node. After setting this as the session name string and testing, the same issue was still present; it still just said "session name". So I went back to looking into more nodes, leading me to find the get player nickname node. So I replaced the unique net ID with a string and tested the server browser again, resulting in the issue being fixed.

![Session Name Fix](https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Development%20Commentary/Images/Testing/Session%20Name%20Fix.png)
<br>

*Figure 64. The solution for the session name problem. The session name text is set as the host's nickname(username).*
<br>

![Session Name Working](https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Development%20Commentary/Images/Testing/Sessions%20names%20working.png)
<br>

*Figure 65. The session name is now displaying the host's username instead of saying "session name".*
<br>

Being able to solve this problem allowed me to fix the first issue that I left to fix this one. If the sessions did not have a host player, then there is no valid net ID within the session. This idea resulted in me deleting the branches from before and replacing them with a single branch that checked if there is a unique net ID within the session. After one final Steam test, the fake sessions stopped appearing. 

![Fake Sessions Fix](https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Development%20Commentary/Images/Testing/Fake%20Sessions%20Final%20Fix.png)
<br>

*Figure 66. The fix for the fake sessions appearing. As the fake sessions should not have a host, a check is run to make sure a host is present before a session is found and listed.*
<br>

![Steamworks Test Builds](https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Development%20Commentary/Images/Testing/Server%20test%20builds.png)
<br>

*Figure 67. The Steam builds that were used to test the server browser issues.*
<br>

### Jenkins 217
Before running the staging pipeline, I tested the original code on a test pipeline. The test pipeline was set up to test a random repository that I hadn't used in a while. I did this instead of just working straight on the staging branch of the project because I had never used Jenkins before, so I did not want to risk any problems occurring in the project because of setting up Jenkins.

After running the pipeline to test the code, I had many failed builds, with each one further expanding my knowledge of how Jenkins works and what is needed to automate the Unreal Engine build. My first few failed builds were occurring due to file paths being wrong and not existing, resulting in me fixing them and checking through the code further for any other incorrect paths. After that failure, the next one failed due to a lack of access to the repository. To fix this problem, I had to look into access levels and keys so that I could give Jenkins a GitHub access key with permissions to access and edit the repository. The final error ended up being due to a missing bracket in the code. After these tests, the original code worked and was ready for me to set up for Greedy Piggies.

![Jenkins Pipelines](https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Development%20Commentary/Images/Testing/Jenkins%20Pipelines.png)
<br>

*Figure 68. All three of the pipelines I have created, including the main pipeline, a test pipeline for getting an API for Jenkins working, and the original test branch for testing the original code.*
<br>

![Jenkins Test Results](https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Development%20Commentary/Images/Testing/Jenkins%20Test%20Pipeline%20Results.png)
<br>

*Figure 69. The results of each run of the test pipeline.*
<br>

### Character Select 95
The majority of my testing occurred whilst working on the character select screen due to all the errors that I have previously discussed. After each test, I noted down my observations in a data table to keep track of my progress and each error that occurred during its development. When I managed to fix the problems, it was not added to the table because I moved straight back to the server browser to fix an issue.

![Character Select Test Table](https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Development%20Commentary/Images/Testing/Character%20Select%20Test%20Table.png)
<br>

*Figure 70. The table with the test that I ran whilst working on the character select screen.*
<br>

Whilst working on the character select screen, I took a few images from some of the tests I did.

![Taken Character Array In Player State P1](https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Development%20Commentary/Images/Testing/Taken%20character%20array%20in%20player%20state%20P1.png)
<br>

*Figure 71. The tag error from the perspective of player 1. The server would only see player one's choice, whereas the client would see both choices.*
<br>

![Taken Character Array In Player State P2](https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Development%20Commentary/Images/Testing/Taken%20character%20array%20in%20player%20state%20P2.png)
<br>

*Figure 72.The tag error from the perspective of player 2. The server would only see player one's choice. whereas the client would see both choices.*
<br>

### Late Fixes 81
Throughout the whole process of trying to get the game ready to be released, Lilly and I were running constant tests to make sure everything we were trying to fix worked. Due to the lack of time we had whilst working on the project at this stage and my need to still get this commentary done, I did not end up recording the results from each of these builds, just developing and attempting to fix the problem straight after the test.

![All Steam Builds](https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Development%20Commentary/Images/Testing/Steam%20Build%20List.png)
<br>

*Figure 73. All the Steam builds that were used to test the late fixes.*
<br>

<!--
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
-->

---

## Critical Reflection *(Approx. 10–15% of word count)*

### What went well? 171
I was very proud of how well the server browser and character select screen work, especially as it is my first time working with multiplayer on Unreal Engine. Even though both of them had countless errors and problems, I never gave up and kept testing, researching and altering their code until they both worked. 

When it comes to Jenkins, I was very proud of the end result and how far I have developed the code, from just checking if the game builds to uploading it to GitHub release, messaging the results to Discord and then using Python to create and update data files on the results of each build.

Although I wasn't the happiest in being left to fix the game basically by myself near the end, I was glad that I did it and happy with the progress I was able to make over those two days, especially with the fact that I was able to fix issues with scripts that I had never worked on or seen before then. 

### What could be improved or done differently next time? 320
I felt like the main problem throughout this project was a lack of communication. This affected the whole project throughout the whole ten weeks, from code needing to be cut or added but was not communicated properly, to me having to put assets in and change up the scene last minute, as I heard that the assets weren't in the game or any scenes yet, even though it took me a minute to find all of them.

Personally, I felt like I could have got Jenkins set up much sooner than I did. I did not set it up late into the project, but I feel like if it had been done a little bit sooner, I could have possibly helped with other bits that did not end up making it into the game, like the shop cards, instead of working on the server browser and character select screen till as late as I did.

I also felt that some things were focused on more than they should've been by other developers and designers, either by having a person focus on one small thing for the whole of the ten weeks, or having a large group working on something that does not require that many people. If people were spread out between tasks in a more resourceful way, I feel like there would not have had to be as much cut from the final game as there was.

If I were to do this again, I would get Jenkins set up within the first day of the project and then get straight to working on the server browser, as this ended up taking up most of my time, as I did not realise how long a task this was going to be to develop. I would have also set up the ClickUp webhook sooner than I did, as that would have got people using it more as well as sooner.


<!--
### What went well?

* What strengths or successes stood out in the final piece?
* Did anything exceed expectations?

### What could be improved or done differently next time?

* Were there things that didn’t work? Why?
* What would you try differently with more time or resources?
-->

---

## Bibliography
### Research
- Creating webhooks (s.d.) At: https://docs-internal.github.com/en/webhooks/using-webhooks/creating-webhooks (Accessed  19/03/2026).
- How To Install Jenkins on Windows 11 (2023) Directed by ProgrammingKnowledge. At: https://www.youtube.com/watch?v=Zdxko2bPAAw (Accessed  11/02/2026).
- Move or Die on Steam (s.d.) At: https://store.steampowered.com/app/323850/Move_or_Die/ (Accessed  19/04/2026).
- Kumar, J., Herger, M. and Dam, R. F. (2026) Bartle’s Player Types for Gamification. At: https://ixdf.org/literature/article/bartle-s-player-types-for-gamification (Accessed  20/04/2026).
- Using Gameplay Tags in Unreal Engine | Unreal Engine 5.7 Documentation | Epic Developer Community (s.d.) At: https://dev.epicgames.com/documentation/unreal-engine/using-gameplay-tags-in-unreal-engine (Accessed  01/04/2026).
- Vorderer, P. and Bryant, J. (2012) Playing Video Games: Motives, Responses, and Consequences. (s.l.): Routledge.
- Windows (s.d.) At: https://www.jenkins.io/doc/book/installing/windows/ (Accessed  11/02/2026).


### Sources
- • • 1, 080 and Ago, 883 Views 6 Years (s.d.) YouTube. At: https://www.youtube.com/ (Accessed  19/04/2026).

### Implementation
- Make a Multiplayer Game in Unreal Engine 5 - Character Selection - Unreal Beginner Tutorial # 16 (2022) Directed by GameDevRaw. At: https://www.youtube.com/watch?v=9f-feH2gP-o (Accessed  17/04/2026).
- UE5 Steam Multiplayer EP1 – Basic Connection Logic (No UI) (2026) Directed by It’s Me Bro. At: https://www.youtube.com/watch?v=KNeRVpPvl-w (Accessed  17/04/2026).

### Declared Assets
- Grammarly (s.d.) At: https://app.grammarly.com/ (Accessed  24/04/2026).
- Statzer, J. (MordenTral) (2026) mordentral/AdvancedSessionsPlugin. At: https://github.com/mordentral/AdvancedSessionsPlugin (Accessed  20/04/2026).


---

## Declared Assets

- * `AdvancedSessions.uplugin` - Third party plugin to connect the game to steam session - (Statzer, 2026)
- * `AdvancedSteamSessions.uplugin` - Third party plugin to connect the game to steam session - (Statzer, 2026)
- * `Grammerly` - Used for spelling, punctuation and grammar checking - (Grammarly, s.d.)
<!--
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
-->
---
