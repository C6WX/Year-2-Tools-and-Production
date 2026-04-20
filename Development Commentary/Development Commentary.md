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

## Research *(Approx. 20-30% of word count)* 1564 words

### What sources or references have you identified as relevant to this task? 966

#### Jenkins 203
To be able to implement Jenkins into the project so that it could automatically build the staging branch, I first had to research how to setup Jenkins and how to use it. At first I started off by following a tutorial that covered downloading and installing Jenkins (How To Install Jenkins on Windows 11, 2023). At first I struggled to find the right tutorial for setting this up but this video was able to help me get Jenkins installed and working. During the install process, I did have trouble with finding which version to use and using the setup wizard but after looking into the official documentation, I was able to install the right version and continue following along with the video (Windows, s.d.). 
Once Jenkins was setup, I then went on to researching how I would go about creating a pipeline. I started by watching videos and looking at documentation but they ended up not covering what I was trying to use Jenkins to do. So after that I then went onto asking for help from my lecturer who had used Jenkins before, who then provided me with a base code to use with Jenkins. After tweaking the code a bit, I was able to get Jenkins working on the staging branch.

#### App to Discord Webhooks 187
I used webhooks three times during this project, one was programmed into the groovy script to link Jenkins to Discord, the second was to link GitHub to Discord and the third was to link ClickUp to Discord.
When linking Jenkins and Discord, I didn't use any sources due to using AI improve my code, however I did research into linking GitHub to Discord. I wanted to create a webhook between the two apps so that ticket reviewers would get updates as soon as anything is changed on GitHub in an easy to read message format. To do this I found the official GitHub documentation (Creating webhooks, s.d.) that covers creating and using webhooks on GitHub. Looking through this documentation and using AI to help with the Discord side of the webhook allowed me to setup a link between the two websites so that whenever a change occurred on GitHub, a message would be sent to a Discord channel with all relevant information.
![GitHub Message](https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Week%202/Images/Github%20Discord%20Message%20Example.png)
<br>

*Figure 1. An example of a message that is sent whenever a change occurs in any GitHub branch.*
<br>

Creating this webhook between these two apps allowed me to easily setup the webhook between ClickUp and Discord without the need of any form of research to help.

#### Gameplay Tags 169
For the character select screen to work as intended, I had to research into gameplay tags, as I knew that is what I would need to have a working character select, but I did not know anything about how they were used or any of the nodes that are linked to gameplay tags. To find out this information, I turned to the Unreal Engine gameplay tags documentation (Using Gameplay Tags in Unreal Engine | Unreal Engine 5.7 Documentation | Epic Developer Community, s.d.). Using the information gathered from this website, I was able to implement the character select screen using tags so that once a player selects a character, a tag for said character would be added to two different tag containers: one with the player's chosen character and one with all chosen characters. This allowed me to make it so that only one person can choose a character by accessing the chosen characters container and checking if each character has been chosen, and also allowed the archetypes team to access each players character individually to apply character models and voice lines to each player.

#### Character Select Screen Inspiration 101
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

#### Multiplayer and Audience 306
When working on the multiplayer for Greedy Piggies, I decided to research into player types for the game's target audience. When looking through different peoples' work, I came across a book by Peter Vorderer, Jennings Bryant (Vorderer and Bryant, 2012) which discussed many different player archetypes that I had not previously heard of. Previously, I had research into Bartles Taxonomy (Kumar et al., 2026), which breaks down players into four categories: the achiever, the explorer, the socialiser and the killer. For Greedy Piggies, the player base is likely to be split between the socialiser, as it is a party game, and the killer, since the game is all about beating other players. However after reading Playing Video Games: Motives, Responses, and Consequences, I found myself thinking deeper into what fits the games player base as the book discusses more than four player types. "Some more prominent types are identified as: The Competitor, The Explorer, The Collector, The Achiever, The Joker, The Director, The Storyteller, The Performer, and The Craftsmen." After looking into what is said about each type of player, I feel like the audience of Greedy Piggies fits into four of these categories: the competitor, the achiever, the joker and the director. The reason I believe this is due to the competitor is always focussed on beating others and being the best, and Greedy Piggies is all about competition, the achiever who is want to be the best in rankings and have the most wins, in the game players can track their wins within a group of friends, the joker is all about playing for fun and enjoying the social aspects of the game, which Greedy Piggies is focused on being social and having fun, and the director who always wants to lead a group, which a leader of a friend group would be able to do to organise playing Greedy Piggies together.



### Sources 598 words

#### Jenkins
##### Jenkins Setup Guide 113
The YouTube tutorial I used for setting up Jenkins (How To Install Jenkins on Windows 11, 2023) was published by ProgrammingKnowledge (• • 1 et al., s.d.), a YouTuber dedicated to creating tutorials and guides for many different tools and programming languages to help people get started. 
From this video I learned how to:
- How to install Jenkins
- How to setup Jenkins
- How to create a Jenkins account
- How to access Jenkins through a web browser

This tutorial was pretty useful for the most part however I ended up having to install Jenkins from a different file type on the website since the file type shown in the video would not work on my computer. This problem then lead me to looking at the Jenkins install documentation. 

##### Jenkins Documentation 92
The official Jenkins documentation (Windows, s.d.) was created by the official creators of Jenkins.
Reading through the documentation taught me:
- How to setup Jenkins in a more in depth guide
- Using the windows file instead of the war file

Without using this website, I would not have been able to setup Jenkins due to the problem I was having with the war file shown on the YouTube tutorial, making this source very helpful. However I did find that the documentation website was, although laid out neatly, very cluttered with information that could be elsewhere.

#### App to Discord Webhooks
##### GitHub Webhook Documentation 124
The Github Webhook documentation was created by GitHub, Inc, the creators of Github.
From reading through the documentation, I learnt how to:
- How to add webhooks on GitHub
- How to create and add secret keys
- How to choose what triggers the webhook and what it has access to

Finding this website was crucial to me being able to make the GitHub webhook work with Discord as I did not know the first thing about webhooks before researching this. I found the website to be very well laid out and easy to find what you need. On the other hand, although the website goes into a lot of detail about different types of webhooks, it did not cover much outside of creating a basic webhook.

#### Gameplay Tags
##### Gameplay Tags Documentation 74
The gameplay tags documentation is created by Epic Games, the creators of Unreal Engine.
From researching gameplay tags through this page, I discovered how to: 
- Create a tag container
- Add tags to a container
- Find if a container contains a specific tag

In my opinion, the information provided was very bulky, making it difficult to find what I needed, but when I did find it, I was able to learn gameplay tags with ease.

#### Character Select Screen Inspiration 85
Move or Die was created by Those Awesome Guys, a small indie studio based in Romania. They are known for creating fast and simple party multiplayer games.
From looking into this game, I took inspiration from their character select screen as it's layout fit perfectly with what I needed the Greedy Piggies screen to look like. The only thing it was missing that I added to the Greedy Piggies UI was a ready up button that would start the game once every player was ready.

#### Multiplayer and Audience 110
Playing Video Games: Motives, Responses, and Consequences was wrote by Peter Vorderer and Jennings Bryant, two key figures in media psychology. They study how people interact with media, including games, TV and digital platforms.
From reading their book, I learnt:
- Another version of player taxonomy
- How players interact with different types of games

From what I was able to read of this book online, I felt like it was able to go really in depth about everything to do with player types in an easy to understand and read format. However, due to the high number of topics that the book covers, it is difficult to find what you need. 

---

## Implementation *(Approx. 30–40% of word count)*

### What was your development process and how did decisions evolve?

#### Jenkins 393 words
After researching and setting up Jenkins, I was given a base code that I used to set up a test pipeline. This pipeline was used to build a random repository on my GitHub account at 10 pm everyday. The reason behind me testing on another repository first was because I did not want to risk making any mistakes on the staging branch of Greedy Piggies. After the pipeline was successful, I then went onto creating a pipeline for the staging branch of Greedy Piggies that once again built at 10 pm everyday.

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

*Figure 5. The base code that built staging and returned wether it was successful or not.*
<br>

Once I had the basic pipeline working, I looked into having Jenkins send a message to Discord that contained the details on each Jenkins run. I was able to do this by creating a webhook that linked Jenkins and Discord and then adding to the groovy code within the pipeline so that whenever Jenkins was successful, the message would display: SUCCESS Greedy Piggies Staging (Build Number). Otherwise, if the build was to fail it would display: FAILED Greedy Piggies Staging (Build Number). 

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

*Figure 6. The code that was added to the pipeline to send Github Messages of each build status.*
<br>

![Original Jenkins Message](https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Development%20Commentary/Images/Implementation/Jenkins/Orignial%20Jenkins%20Message.png)
<br>

*Figure 7. The message that was sent whenever Jenkins was successful with a build.*
<br>

![Original Jenkins Message](https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Development%20Commentary/Images/Implementation/Jenkins/Original%20Jenkins%20Message%20Fail.png)
<br>

*Figure 8. The message that was sent whenever Jenkins was unsuccessful with a build.*
<br>

After getting feedback on how Jenkins was running, I realised that I needed to have Jenkins uploading each of these builds to GitHub so that they can be easily accessed and tested by anyone working on the game. I was able to implement this by updating the pipeline code with a new section that zips the build, archives it and then uploads it as a new GitHub release. Whilst working on this, I decided to add to the GitHub webhook code so that it would link the new release, making it even more accessible to anyone on the Discord.

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

*Figure 10. The updated version of the Discord webhook message code, so that it now links the GitHub release if the build succeeds.*
<br>

![New Jenkins Message Success](https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Development%20Commentary/Images/Implementation/Jenkins/New%20Jenkins%20Success%20Message.png)
<br> 

Later into the project I learnt about CSV files and storing data, I moved onto implementing data tracking and storing into my Jenkins pipeline. I was able to do this with a mix of adding to the groovy script and using python. The two scripts communicate with each other to create and add to a CSV data table that stores each build's build number: date and time, branch, result and time to complete (in seconds). As well as the CSV data table, the pipeline now creates and adds to a graph png that tracks and compares each build's build time and a text document that tracks the number of total builds, successful builds, failed builds, average duration and success rate.

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

*Figure 11. The new addition to the groovy script to communicate with the python script and create and update the new data files.*
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

*Figure 12. The python script that gathers the data from each build and creates or updates the new data files.*
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

*Figure 13. The CSV file outputted by the python script.*
<br>

```
Total builds: 29
Successful builds: 25
Failed builds: 3
Average duration: 213.69 seconds
Success rate: 86.21%
```
<br>

*Figure 14. The text file outputted by the python script. The reason there is more total builds then successful and failed builds combined is due to it not separately tracking aborted builds.*
<br>

![Build Duration Table](https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Development%20Commentary/Images/Implementation/Jenkins/build_duration.png)
<br>

*Figure 15. The data table outputted by the python script. The spike in time for build 50 was due to internet connectivity issues.*

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

*Figure 16. The complete groovy script used by the Jenkins pipeline.*
<br>

#### Webhooks


#### Server Browser


#### Character Select Screen



Describe your technical and creative approach, including:

* Planning, ideation, and iteration
* Feedback received and how it was integrated
* New tools, workflows, or systems explored

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
- Vorderer, P. and Bryant, J. (2012) Playing Video Games: Motives, Responses, and Consequences. (s.l.): Routledge.
- Kumar, J., Herger, M. and Dam, R. F. (2026) Bartle’s Player Types for Gamification. At: https://ixdf.org/literature/article/bartle-s-player-types-for-gamification (Accessed  20/04/2026).




### Sources
- • • 1, 080 and Ago, 883 Views 6 Years (s.d.) YouTube. At: https://www.youtube.com/ (Accessed  19/04/2026).

### Declared Assets
- Statzer, J. (MordenTral) (2026) mordentral/AdvancedSessionsPlugin. At: https://github.com/mordentral/AdvancedSessionsPlugin (Accessed  20/04/2026).

---

## Declared Assets

- * `AdvancedSessions.uplugin` - Third party plugin to connect the game to steam session - (Statzer, 2026)
- * `AdvancedSteamSessions.uplugin` - Third party plugin to connect the game to steam session - (Statzer, 2026)

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