# Platforms, Hardware & System Administration

---

## 1. Introduction 
The tool I have created to be implemented is a Jenkins automation pipeline. This tool automatically builds the game at a given time and/or date to check if the game is building properly. Once the game has built, it sends a report back with the results and build time. However if the build fails, the output log can be checked and the problem can be promptly fixed. This tool also sends a build to GitHub whenever the game is successfully built, meaning a recent build is always available for download online. So that everyone on the project knows that the tool is running, it can also send messages of the build status to a group chat through Discord.

---

## 2. Technical Stack 

#### Core Automation 
- Jenkins 
  -  Runs the pipeline
  - Schedules builds
  - Executes scripts
  - Manages build history and logs

#### Version Control
- Git
- Github
  - Stores the game project
  - Triggers builds on commit or schedule
  - Hosts successful build outputs

#### Build System
- Unreal Engine or Unity (depending on the project)
  - Compiles the game
  - Packages builds
  - Generates output logs

#### Scripting and pipeline definition
- Groovy
- Shell or batch scripts
  - Define pipeline stages
  - Automate build steps
  - Handle error checking

#### Notification System
- Discord
  - Sends build success or failure messages
  - Uses webhooks for automation

#### CI/CD Integration
- GitHub actions or Jenkins plugins
  - Optional backup automation
  - Handles repository triggers

#### Artifact Storage
- GitHub actions or Jenkins plugins
  - Stores completed builds
  - Allows team downloads



---

## 3. Hardware requirements 

Jenkins requires a dedicated build machine or server to run the build pipeline. The hardware requirements for this machine is completely dependant on the game engine and size of the project being made.

#### Minimum Setup
A minimum setup to test pipelines or to build small projects would be a computer with at least:
- CPU: 4 cores, modern processor
- RAM: 8-16GB
- Storage: 100GB SSD
- Network: Stable broadband connection

#### Recommended Setup
A recommended setup that is best for a standard project with a quicker build time and that can handle larger assets should include at least:
- CPU: 6-12 cores, high clock speed
- RAM: 16-32GB
- Storage: 500GB SSD or NVMe
- GPU: optional, only required for some Unreal Engine tasks
- Network: Fast and stable, low latency

#### High Performance Setup
This setup would be used for large team projects where multiple builds are run daily. This setup should have at least:
- CPU: 12-32 cores
- RAM: 32-64GB
- Storage: 1TB NVMe SSD
- GPU: mid range GPY if lighting or shaders are used
- Network: gigabit connection

---

## 4. Cost 
The cost of the hardware required to run this tool is also completely dependant on the size of the project being created and the game engine used. The following is a rough estimate that was produced when searching for the previous specifications while also keeping in mind different cost brackets.

#### Minimum setup
- PC: £400-£800
- Storage: £50-£100
- Total: £450-£900

#### Recommended setup
- PC: £900-£1500
- Storage: £100-£200
- Total: £1000-£1700

#### High performance setup
- PC: £1500-£2500
- Storage: £200-£400
- Total: £1700-£2900

---

## 5. System Functionality Diagram

```

[Developer]
     │
     │ Push code
     ▼
[GitHub Repository]
     │
     │ Trigger (webhook or schedule)
     ▼
[Jenkins Pipeline]
     │
     ├── Stage 1: Pull Latest Code
     │
     ├── Stage 2: Build Game
     │        │
     │        ├── Success ────────────────┐
     │        │                           │
     │        └── Failure ───────┐        │
     │                           │        │
     ▼                           ▼        ▼
[Build Logs]              [Error Report]  [Packaged Build]
     │                           │        │
     │                           │        ▼
     │                           │   [Upload to GitHub]
     │                           │        │
     │                           │        ▼
     └──────────────► [Discord Notification System]
                              │
                              ▼
                       [Team Receives Status]

```

---

## 6. Connected Systems

This pipeline links multiple systems through automated communication and data flow.

1. Jenkins connects to GitHub using repository access and webhooks

2. Jenkins connects to the game engine build tools

3. Jenkins sends output data after each build

4. Jenkins connects to Discord using webhooks

5. Jenkins pushes successful builds to GitHub

## Bibliography

- Jenkins (s.d.) At: https://www.jenkins.io/https:/www.jenkins.io/ (Accessed  05/04/2026).

---

## AI Usage Declaration

- Chatgpt was used for paragraph structure and spelling and grammar checking and the process of creating the API.
- ChatGPT (s.d.) At: https://chatgpt.com/ (Accessed  09/02/2026). 

---
