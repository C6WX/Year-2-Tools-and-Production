# Week 6 - Analytics, Databases & Backends

---

## 1. Introduction

To implement a simple automated method to test a tool, store the test result as data that is then queried and translated into a graph using matplotlib, I added to my Jenkins pipeline and had it run a Python script. My Jenkins job already automatically builds the Unreal Engine project periodically to make sure the staging branch is in working order. I chose Jenkins as the tool to work on for this task as it already outputs the majority of it's data to Discord so I know that it is definitely possible to translate those results onto a graph.

Before implementing the automated output graph to the Jenkins pipeline, I first tested completing this task on some data found online on Kaggle (Kaggle: The World’s AI Proving Ground, s.d.) a website that stores and displays data on endless topics. This test was used to learn how to generate structured datat outputs and graphs using Python and matplotlib. The dataset from Kaggle contained information about comic books such as the title, publisher, release year, format and genre.

---

## 2. Implementation
The comic book dataset test was done first to test the process of converting data into a structured format and generating graphs from the data. Firstly, I found myself a data set that I wanted to test on which ended up being data on Marvel comics. The I used AI to create me a prompt that I would give to the antigravity (Google Antigravity, s.d.) claude opus AI which would then generate Python scripts capable of processing the dataset and producing analysis outputs. The script generated from the AI cleaned the dataset by removing any duplicate data, standardising the publishers, genres and format fields and converting release year values to numeric data. This resulted in a clear dataset containing 9871 entries across 25 publishers and 15 genres.  
Several graphs were then generated using matplotlib. These graphs included releases per year, publisher distribution, genre distribution and format trends. These visualisations demonstrated how the dataset could be analysed and interpreted programmatically. 
After the workflow for this task was completed on data stored online, I used a similar approach on my Jenkins pipeline. The Jenkins pipeline was adjusted so that after each automated build, it writes the build number, timestamp, branch name, build result and build duration to a CSV file. A python script that I created then reads this file using pandas and calculates the statistics such as total builds, success rates and average build duration. The script then generates a matplotlib graph showing build duration over time. This approach automates the process of collecting and analysing build performance data.

---

## 3. Outcome 

The final system automatically tests the Jenkins build pipeline and records the results of each run as structured data. Each time Jenkins performs a build, the pipeline logs the outcome to a CSV file and runs the Python analysis script which then produces a graph showing build duration over time and generates a summary file containing the calculated statistics such as success rate and average build duration.

---

## 4. Bibliography

- Kaggle: The World’s AI Proving Ground (s.d.) At: https://www.kaggle.com/ (Accessed  16/03/2026).
- Google Antigravity (s.d.) At: https://antigravity.google/ (Accessed  16/03/2026).

---

## AI Usage Declaration

- Chatgpt was used for paragraph structure and spelling and grammar checking and the process of creating the API.
- ChatGPT (s.d.) At: https://chatgpt.com/ (Accessed  09/02/2026).
---

## Submission Notes & Checklist

> Remove this section once complete — use this as a checklist before submitting

- Total word count: **500 words (±10%)** across Sections 1–3  
- **Figure captions and figure descriptions do NOT count towards the word count**  
- Use **plenty of images, GIFs, videos, screenshots, and short code snippets** where appropriate to demonstrate understanding and functionality  
- All required **source code is included in this repository**  
- Any required **executables or builds are provided via GitHub Releases**, where appropriate  
- Demonstration video link is accessible and clearly shows functionality  
- Bibliography includes all referenced material  
- AI usage is clearly declared (or explicitly stated as not used)  
- Work reflects your own understanding and professional practice  

---
