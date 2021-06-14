## QA_practical_devops_project
Second QA practical project for the DEVOPS course.

# Art Doodle Idea Generator 

This project is designed to display understanding of the DEVops pipeline technologies / Techniques, the app used to demonstrate this is a drawing idea generator. 

My plan is to have service one Display the results idea / maybe take some kind of input to seed the choices for the idea generated?
Service 2 could generate aesthetic, so for one version picking themes like moody, or bright, or geometric etc, then for the second version it could perhaps specify colour? 
Then service 3 could generate an object or scene? So that when passed to service 4 we get a scene with an aesthetic, then perhaps some additional details based randomly upon
the previously generated ideas. 

# Design

So the way I see it the best way to approach the project brief is with a total of 5 GCP instances, 4 Ubuntu VM's and one SQL database. The build  stage of the code should flow as follows:
![image](https://user-images.githubusercontent.com/81659044/121825307-86521e00-cca9-11eb-9d9c-0c6f9a5b1a2c.png)

So as seen Jenkins is launched on the DEV branch, and then the Jenkins pipeline sets up the docker nodes and nginx node on their own VMS, with the already established SQL database there for them to connect to. 

Jenkins then builds and pushes the instances so that they can be retrieved in the deploy stage on each node. With Ansible managing the configuration of the docker swarm for the instances to be deployed on. 

 ## Tools Used:
Kanban Board: Jira
- Jira was used for keeping track of the User stories / planning out which features need to be added, I chose Jira for it's ease of use and familiarity, examples of how it's used shown further on in the documentation.

Version Control: Git
- Git is used as version control as it's very easy to modify the source code from either the site or any of the GCP instances ran if need be. It also allows rolling updates through the use of webhooks, so any changes to the code / any new commits can be immediately picked up by Jenkins and incorporated into the live application without a disruption to service ( assuming the changes are light

CI Server: Jenkins
- Jenkins pipeline is used as the Continuous integration server for this project, it allows the rolling updates from a git hook as previously mentioned, but also allows the pipeline to be defined ( it's steps such as build, test etc) by a file on the Git site, so it's stages themselves can be modified as a rolling update aswell if need be, instead of just the changes to the python code for example. It also allows us to make use of Pytest quite easily by pashing commands through via bash / shell script, which makes the automated testing of our code quite easily, and due to the way it holds onto logs from each pipeline stage we can check the coverage reports through jenkins whilst the application is live, which allows anything not tested to be ammened in a rolling update.
- The overall pipeline configuration is as follows:
![image](https://user-images.githubusercontent.com/81659044/121825930-0037d680-ccad-11eb-9fc1-28d40f47d7ac.png)
So the pipeline / git is gathered in the declarative SCM stage, Requirements like docker, python, pip etc are then installed, the application is tested using pytest to makesure there are no bugs, then the docker images are built and pushed to dockerhub, ansible sets up the swarm / collection of nodes that the application is run across and gets them talking, and finally in the deploy stage the ngninx reverse proxy is established. 

Configuration Management: Ansible
- Ansible allows the automation of setting up the Docker worker / manager nodes, which significantly cuts down deployment time as it doesnt have to be done manually for each node added, instead all thats needed is modifying the Inventory.yaml / playbook.yaml files to include a new host with the name of the machine. It also helps us set up NGINX / anythig else you may want in an application by simply creating a role for it using the ansible-galaxy commands and filling in the tasks / files section. 

Cloud server: GCP virtual machines
- Besides being specified in the brief, GCP is a lot easier to setup firewall wise than amazon is and allows the multiple vm instances to be spin up with less effort.

Containerisation: Docker  and Orchestration Tool: Docker Swarm
- So Docker is used to form the container for each service, a dockerfile containing something along the lines of:
FROM python:latest
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python","app.py"]
- Is included in each service route, this means each service can be built in an automated way along with any requirements for it to be installed that weren't covered in the initial install phase. Docker Swarm is used to form managers and workers than run the docker images / distribute work across a network. 

Reverse Proxy: NGINX
- NGINX is the load-balancer, it distributes site usage amongst the various containers to maintain smooth operation, so for example if multiple users want to access service 2 simultaneously NGINX will send them to different copies of that container to balance the workload, it also allows reverse proxying so the users can access the app ran on any node from one frontent point. 
## This is good for security as you can keep more servers closed to the public / have less vunerability points for hackers.

# Use examples

So upon opening the page you see the last 5 entries to the database below and in the top box a new idea
![image](https://user-images.githubusercontent.com/81659044/121826573-47739680-ccb0-11eb-8ce5-f8a1e637f7c6.png)

And upon hitting the new idea button: 

![image](https://user-images.githubusercontent.com/81659044/121826608-81449d00-ccb0-11eb-96de-717251ef0316.png)

# Pytest Coverage screencaps And Risk Assessment

So below we can see my Risk assessment and Risk assessment matrix, 
![image](https://user-images.githubusercontent.com/81659044/121832140-48f98a80-ccc1-11eb-9d27-52eadfacc11f.png)
![image](https://user-images.githubusercontent.com/81659044/121824936-a680dd80-cca7-11eb-80dd-1deec8bd8490.png)



Below are screenshots showing that each individual service has 100% coverage.
The tests utlisied patched the response codes from the other services into testable values, and all the tests checked to recieve a 200 response code, as shown below i got 100% coverage for each App route so I am fairly confident that my testing was sufficient, the combination of response code checking and testing whether input values appear in the result should reveal all bugs. 

![image](https://user-images.githubusercontent.com/81659044/121696148-ac1dce00-cac3-11eb-8e49-841a1b347937.png)

![image](https://user-images.githubusercontent.com/81659044/121695731-3f0a3880-cac3-11eb-864a-45c56c390594.png)

![image](https://user-images.githubusercontent.com/81659044/121695585-18e49880-cac3-11eb-95c8-c89b60973141.png)

![image](https://user-images.githubusercontent.com/81659044/121695402-edfa4480-cac2-11eb-80f1-be2554f0adc5.png)


And here's the capture from the test stage of the Jenkins pipeline confirming service 4 is 100% in the Jenkins runs:

![image](https://user-images.githubusercontent.com/81659044/121755851-2b38f380-cb10-11eb-8c5f-65a8987ea45a.png)


# Kanban Board

Here's some example use of the Kanban Board showing how it was used to coordinate some of the tasks. 


![image](https://user-images.githubusercontent.com/81659044/121826484-c9af8b00-ccaf-11eb-85f9-66ffcf0bcd6d.png)

![image](https://user-images.githubusercontent.com/81659044/121826459-9d940a00-ccaf-11eb-8921-4bfc3fb83f98.png)

![image](https://user-images.githubusercontent.com/81659044/121756735-0c882c00-cb13-11eb-97e8-d08ce5158a8c.png)

# Setup

To get this App working you need to install jenkins on a ubuntu virtual machine and setup, then clone this git repository into a jenkins pipeline project / set it up to follow the main branch. 
After that create instances and setup firewall permissions for those you intend to use, you'll need to specify the machine names in the ansible playbook yaml in order for them to setup correctly but otherwise building the pipeline should work. 

## Requirements

- python
- flask
- jenkins
- docker
- docker compose
- sql
- sql_alchemy
- github 
- pytest
- pip
- ansible
- ansible-galaxy

