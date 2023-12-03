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
                    echo "AWS_ACCESS_KEY_ID: ${AWS_ACCESS_KEY_ID}"
                    echo "AWS_SECRET_ACCESS_KEY: ${AWS_SECRET_ACCESS_KEY}"
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
                    sh 'pip install -r requirements.txt'  // If you have requirements.txt
                    sh "eb deploy ${EB_ENV_NAME}"
                }
            }
        }
    }
}
