pipeline {
    agent any

    environment {
  
        EB_REGION             = 'eu-west-2'
        EB_APP_NAME           = 'Research-application'
        EB_ENV_NAME           = 'Research-application-env'
    }

    stages {
        stage('Debug Information') {
            steps {
                script {

                    echo "EB_REGION: ${EB_REGION}"
                    echo "EB_APP_NAME: ${EB_APP_NAME}"
                    echo "EB_ENV_NAME: ${EB_ENV_NAME}"
                }
            }
        }

        stage('Checkout') {
            steps {
                script {
                    checkout scm
                }
            }
        }

        stage('Deploy to Elastic Beanstalk') {
            steps {
                script {
                    bat 'pip install -r requirements.txt'  // If you have requirements.txt
                    bat "C:\\Windows\\System32\\eb deploy ${EB_ENV_NAME}"
                }
            }
        }
    }
}
