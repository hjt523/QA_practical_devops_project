#!/bin/bash

# install Requirements

sudo apt update
sudo apt-get install python3-venv 
sudo apt-get python3-pip

python3 -m venv venv
source venv/bin/activate

pip3 install pytest

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
