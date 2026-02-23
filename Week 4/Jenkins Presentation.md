---
marp: true
title: Jenkins
theme: gaia
author: Callum Wade 2404781
transition: cover
style: |
  section {
    position: relative;
  }
  .top-right {
    position: absolute;
    top: 500px;
    right: 40px;
    width: 150px;
    z-index: 1;
  }
---
<img width="800" src="https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Week%204/Images/Presentation/Jenkins_logo_with_title.png"> 

Presentation <br> by Callum Wade <br> 2404781
<br>

---

# What is Jenkins

<img class="top-right" src="https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Week%204/Images/Presentation/Jenkins_logo.png">

Jenkins is an open source automation server that can be used to automate repetitive development tasks. 
Jenkins creates pipelines that run a series of steps automatically when triggered by a set trigger (a specific time of day or when a script is run.)
  

---

# How I set Jenkins up

<img class="top-right" src="https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Week%204/Images/Presentation/Jenkins%20mechanic.png">

Jenkins is downloaded and run on my personal PC. To get Jenkins working, I created a script within a pipeline project in the langues Groovy. This script has Jenkins build the game from the staging branch in a separate workspace to check that the game builds properly. I have set up a poll source control manager so that the game is built at 10pm everyday.

---

# How this helps development

<img class="top-right" src="https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Week%204/Images/Presentation/jenkins-with-plate-basis-256px.png">

Jenkins being integrated into the project means that no one is required to manually build the game periodically. Instead Jenkins does this at a specific time everyday without the need for human input, removing the chance of any human error. 
This also allows errors to be found early, allowing them to be focused on and fixed before development continues, as at the end of the day, the game building is the most important thing.

---

# Any security/data issues with the Jenkins

<img class="top-right" src="https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Week%204/Images/Presentation/Jenkins%20Error.png">


---

# How this can be replicated for another project?

<img class="top-right" src="https://raw.githubusercontent.com/C6WX/Year-2-Tools-and-Production/refs/heads/main/Week%204/Images/Presentation/Cute%20Jenkins.png">

This tool is really easy to replicate to work for another project. All that needs to be done to do this is to make sure that your Github key allows access to all repositories or at least the ones Jenkins needs to access. Then all that needs to be done is a new pipeline needs creating and the code will just need to be copied over from the previous pipeline and adjusted to work for the new repository.



--- 
# Bibliography

- Jenkins (s.d.) At: https://www.jenkins.io/https:/www.jenkins.io/ (Accessed  23/02/2026).




