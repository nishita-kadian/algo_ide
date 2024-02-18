# algo_ide

The project was broken down into 3 major components:
1. User authentication along with database models
2. Integrating code editor allowing users to submit and test code
3. Dockerizing and hosting

Breaking down the tasks further:
1. User authentication
  a. Login, Signup and Logout along with session management
  b. Model definition for code and users
  c. Profile page for editing details and looking at previous submissions along filters on these submissions.
2. Integration code editor
  a. Integration Ace code editor for leveraging syntax highlighting and other cool editor features
  b. Extract code from this editor and using subprocess run this code to test against our correct solution
  c. Give support to users to see testcases and their output along with expected output. Do the same for custom testcase input.
3. Dockerizing and hosting
  a. Dockerize the application
  b. Build and run the docker image
  c. Host this image on EC2, pull code from github using deploy keys, install docker/git on ec2, edit inbound rules to access port 8000.


## Creating migrations for db
`python manage.py makemigrations`

## Executing migrations on db
`python manage.py migrate`

## Running the server
`python manage.py runserver 0.0.0.0:8000`

## To run using docker
### Create docker image
`docker build -f Dockerfile -t algo_ide .`
### Run docker image
`docker run -p 8000:8000 algo_ide`

## Access the website [here](http://ec2-13-201-99-41.ap-south-1.compute.amazonaws.com:8000/login/)

use the following login

username: nk

password: 123

## Shortcomings:

Due to lack of time, following are the shortcomings that I can think of from top of my head
  - Beautification of frontend is major pain point in this project.
  - If the code the user passes has compiliation error, the server crashes, instead it should have been handled gracefully. For this we have to leverage subprocess's error handling.
  - Hiding unnecessary items in the navbar
  - Editing homepage and making it informative and accessible for users

## References:
---------------
  - Learned Django from scratch: https://www.youtube.com/playlist?list=PL-51WBLyFTg2vW-_6XBoUpE7vpmoR3ztO
  - Explored Codemirror6: https://grantjenks.com/docs/django-codemirror6/
  - But used Ace for editor: https://github.com/django-ace/django-ace
  - Cache pip packages to save time on docker builds: https://stackoverflow.com/a/58021389
  - https://docs.github.com/en/authentication/connecting-to-github-with-ssh/managing-deploy-keys
  - https://medium.com/appgambit/part-1-running-docker-on-aws-ec2-cbcf0ec7c3f8
  - https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
  - https://medium.com/backticks-tildes/how-to-dockerize-a-django-application-a42df0cb0a99
  - Learned why and how to edit inbound rules for security groups on AWS EC2
  - Question (: => https://leetcode.com/problems/concatenation-of-array/description/
