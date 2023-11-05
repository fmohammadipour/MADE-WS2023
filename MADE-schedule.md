# Main site for getting updates
https://made.uni1.de

## General Info
Data engineering: Development stack of your choice

Data exploration: Python notebook 

Data analysis: Python notebook

The goal of the project is to create a report that answers an interesting question based on at least two data sources

## Project Work 1
Create a public GitHub repository for the module by forking https://github.com/jvalue/made-template

Answer Google Form with a link to your repository 

(optional) Set up Python / Jayvee / Jupyter Notebook environment

## Project Work 2
- Submit project plan
  submitted in : https://github.com/fmohammadipour/MADE-WS2023/blob/main/project/Project-Plan.md

Create coarse-grained issues that layout the working packages you will work on during the semester and link them in section “Work Packages” in the project plan. This plan is allowed to be enhanced and changed over the course of the semester. Please keep it up-to-date.

- Watch and get familiar with Jayvee basics using the following resources:
- Core concepts video: 	https://www.youtube.com/watch?v=X8fOK8JIBZA
- Core concept docs: 	https://jvalue.github.io/jayvee/docs/user/core-concepts
- Tutorial examples: 	https://jvalue.github.io/jayvee/docs/category/jayvee-examples


+ Prepare for Project Work 3
  Explore your chosen datasets
  What data is available? What errors are there?
  What limitations present themselves, is data missing and representative?
  What data types are relevant, do you need to research anything?
  You can use a Python notebook to load and explore your data (see the example in your repository)
  You do not need to make a submission for this part of the Project Work, it is just for you to get more familiar with your data


## Project Work 3
- Follow your project plan to build an automated data pipeline for your project
- Write a script (for example in Python or Jayvee) that pulls the data sets you chose from the internet, transforms it and fixes errors, and finally stores your data in the /data directory
- Place the script in the /project directory
  The output of the script should be: datasets in your /data directory (e.g., as SQLite databases)
  Do NOT check in your data sets, just your script
  You can use .gitignore to avoid checking in files on git
  Update the issues and project plan if necessary



## Project Work 4
- Add automated tests for your project
- Add a /project/tests.sh file that executes your tests
- There should be at least one test case on the system-test level
- Executes your data pipeline
- Validates that the output file(s) are there
- Continue working on your project
- If you are not finished, continue the exploratory data analysis you started in Project Work 2,
- Update your issues if necessary

## Project Work 5
- Continue working on your project
- Start working on your final report (for an example, see /examples in your template repository)
- CI for your project
- Use GitHub Actions
- There should be at least test execution on every push
- Executes the test.sh (from project work 4)
- Update the issues if necessary


## Project Work 6
- Final report
  Your final report should be a standalone file that can be read by someone unfamiliar with your project, to give you more options you can submit your notebook   or export it as either pdf or html
- If you submit as ipynb, make sure GitHub preview renders your report correctly
- Commit and push one of the following files containing your final report to GitHub
  /project/report.ipynb
  /project/report.pdf
  /project/report.html


## Project Work 7
- Make your repository presentable
- Choose an appropriate open-source license (like CC BY 4.0) and add it to your repository (see GitHub documentation)
- Polish the README and documentation, e.g., add the title of your project, a short description, embed your presentation slides/video (see below), and link the final report
- Optionally, proudly share your repository with the world with the hashtag #JValueMADE
- Optional: Project presentation
  If you would like to get a chance to present your project, submit these additional files
  Submitting a presentation will increase your final grade
  We will randomly select some submissions to be presented live in class
  Your presentation submission should include slides and a video of yourself presenting your slides
  Presentations should last a maximum of 10 minutes
  You should decide the focus of your presentation yourself, you can cover your data science question, which data sets you selected and why, how you implemented your data pipelines and results of your report
  The video can be a voiceover without showing your face
  Presentations must be in English
  We will choose a random sample of presentations to be held live in week 12/13
  We will announce the selection in StudOn and the Q&A in week 11
  In class presentations are done via Zoom, you share your screen and must have a microphone
  Commit and push the following files containing your project presentation slides and video to GitHub
  /project/slides.pdf
  /project/slides-video.<video file format>
  Optional: Blogpost about your project
  If you agree with us posting about your project on our blog (similar to existing posts here https://oss.cs.fau.de/tag/made-projects/), please fill out this form: To Be Announced


## Project Work 8
- Fill out the Course Exit survey to let us know about your learning progress and optionally allow us to blog about your project
- To Be Announced

# Exercises
## Info about exercises
- Place all exercise submissions into the folder named “exercises” in your GitHub repository

- Name exercise submissions either “exercise<number>.jv” or “exercise<number>.py”

  For example, if you are in the group using Jayvee for exercise 1, you must submit the following file: /exercises/exercise1.jv, if you have to use Python, submit /exercises/exercise1.py

We will grade the version of the exercise that is in your public GitHub repository at the deadline (!)

