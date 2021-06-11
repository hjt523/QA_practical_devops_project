pipeline {
    agent any
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
