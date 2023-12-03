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
