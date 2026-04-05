# Web Services & Online Integration

---

## 1. Introduction

The tool that I developed for this project is a Jenkins (Jenkins, s.d.) pipeline that is used to automatically build the Unreal Engine (The most powerful real-time 3D creation tool, s.d.) project. The pipeline retrieves the latest version of the project from the staging repository, verifies the build environment, compiles the game and sends the build result to a Discord (Discord - Group Chat That’s All Fun & Games, s.d.) channel. This tool can be made more accessible to other developers working on the project by using a public facing API that can use a Discord bot to trigger builds and retrieve build information. This API will expose the Jenkins build system through a set of operations

![Discord Build Notification Message]()

*Figure 1. This figure shows the message that is send by the Jenkins webhook that includes the build of the game and the result of the build to Discord.*

![Jenkins GitHub Build]()

*Figure 2. This figure shows the build that is pushed to GitHub automatically after each successful build.*

---

## 2. Implementation

The Jenkins build exposes four main calls. The first one is StartBuild which triggers the project to be built. The second one is GetBuildStatus which returns the current state of a build. The third call is GetBuildLogs which retrieves the log output that is generated during the build process and the fourth call is DownloadBuildArtifact which allows the user to download the packaged project once the build is successful. These operations provide full control over the Jenkins automated build process while stopping everyone from accessing the full Jenkins project.
A typical usage example would begin with a developer sending a request to start a build. The request uses the HTTPS POST method and includes the branch and configuration to build.
```
Request
POST /build

{
    "branch": "staging",
    "platform": "Win64",
    "configuration": "Development"
}

Response

{
    "buildId": 1,
    "status": "queued"
}
```
After the request is ran by Jenkins, the build is placed in the queue and begins executing the pipeline. The developers can then check the progress of the build using the build identifier returned in the first response.

```
Request
GET /build/1/status

Response

{
    "buildId": 1,
    "status": "running"
}
```
If the project builds successfully, the response will change the status to success and provides access to the build.

```
Request
GET /build/1/status

Response

{
    "buildId": 1,
    "status": "success"
    "artifact": "/build/42/download"
}
```
The API references define each call in more detail. The StartBuild operation begins the Jenkins pipeline. It uses the branch, platform and configuration parameters to determine which version of the project is compiled and how the build is packaged. The data that it returns includes the build identifier and the status of the current job. Errors that can occur during this call includes invalid parameters, missing authentication to access the pipeline or the Jenkins server being unavailable.

The GetBuildStatus call retrieves the information from a specific build using just the build identifier. The response provided by this call includes the build status - which can be queued, running, success or failed. Errors that can occur during this call includes the build identifier not existing or missing authentication.

The GetBuildLogs call is used to return the log output that is generated during the build process. This call uses just the build identifier again. This call outputs a list of log entries that describe each step of the pipeline. Errors that can occur during this call is if the log isn't available or if the build hasn't yet started.

The final call is DownloadBuildArtifact which allows users to download the final package build produced by Jenkins. The only parameter used is the build identifier. The call outputs a compressed build file generated bt the Unreal packaging process. Errors can occur if the build failed or if the file has not yet been produced.

![Artifact Storage]()

*Figure 3. This figure shows the artifacts being stored under the Jenkins directory for future use.*

---

## 3. Outcome

This API exposes the functionality of the Jenkins pipeline through a simple interface. Developers are able to trigger builds, monitor progress, retrieve logs and download packaged builds without directly accessing the Jenkins interface. This API improves accessibility and automation while keeping the build infrastructure secure and controlled

## Bibliography
- The most powerful real-time 3D creation tool (s.d.) At: https://www.unrealengine.com/en-US (Accessed  23/02/2026).
- Jenkins (s.d.) At: https://www.jenkins.io/https:/www.jenkins.io/ (Accessed  23/02/2026).
- Discord - Group Chat That’s All Fun & Games (s.d.) At: https://discord.com (Accessed  09/03/2026).

## AI Usage Declaration

- Chatgpt was used for paragraph structure and spelling and grammar checking and the process of creating the API.
- ChatGPT (s.d.) At: https://chatgpt.com/ (Accessed  09/02/2026).
---
