pipeline {
    agent any
    stages {
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
            }
        }

        stage('Deploy') {
            steps {
                //
            }
        }
    }
}
