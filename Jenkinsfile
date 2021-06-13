pipeline {
    agent any
    environment { 
        DOCKER_PASSWORD = credentials('DOCKER_PASSWORD')
        DOCKER_USERNAME = credentials('DOCKER_USERNAME')

    }
    stages {
        stage('Install Reqs') {
            steps {
                // 
                sh 'bash jenkins/install_reqs.sh'
            }
        }
        stage('Test') {
            steps {
                // pytest with cov reports
                sh 'bash jenkins/test.sh'
            }
        }
        stage('Build') {
            steps {
                // Building the Docker containers
                sh 'docker-compose build'
            }
        }
        stage('Push') {
            steps {
                // Pushing our image to docker hub
                sh 'docker-compose push'
            }
        }
        stage('Config Management') {
            steps {
                // Using Ansible to manage configuration
                sh 'cd ansible && ansible-playbook -i inventory.yaml playbook.yaml '
            }
        }
        stage('Deploy') {
            steps {
                //
                sh 'echo deploy'
            }
        }
    }
}
