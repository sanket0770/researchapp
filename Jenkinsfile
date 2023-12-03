pipeline {
    agent any

    environment {
        AWS_ACCESS_KEY_ID     = credentials('AKIAX3LNWYOGIVRPHOXY')
        AWS_SECRET_ACCESS_KEY = credentials('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')
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
    stages {
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
                    bat "eb deploy ${EB_ENV_NAME}"
                }
            }
        }
    }
}
