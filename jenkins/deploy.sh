#!/bin/bash

# Copying yaml to manager
scp -i ~/.ssh/ansible_id_rsa docker-compose.yaml jenkins@manager:/home/jenkins/docker-compose.yaml

# Deploy Stack
ssh -tt -i ~/.ssh/ansible_id_rsa jenkins@manager << EOF
    export DATABASE_URI=${DATABASE_URI}
    docker stack deploy --compose-file docker-compose.yaml doodlestack
EOF
