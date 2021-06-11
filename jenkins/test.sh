#!/bin/bash

# install Requirements

sudo apt-get update
sudo apt-get install python3-venv -y
sudo apt-get install python3-pip  -y

python3 -m venv venv
source venv/bin/activate

pip3 install pytest
pip3 install pytest-cov

# Includes the stuff for the application(s)
pip3 install -r test_requirements.txt 

# Service1

cd service1
python3 -m pytest --cov=app
cd .. 

# Service2

cd service2
python3 -m pytest --cov=app
cd .. 

# Service3

cd service3
python3 -m pytest --cov=app
cd .. 

# Service4

cd service4
python3 -m pytest --cov=app
cd .. 
