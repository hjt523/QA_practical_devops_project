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
                // pytest
                // run for each service
                // produce cov reports
                sh 'bash jenkins/test.sh'
            }
        }
        stage('Build') {
            steps {
                //
                sh 'docker-compose build'
            }
        }
        stage('Push') {
            steps {
                //
                sh 'docker-compose push'
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
