pipeline {
    agent any

    environment {
        AWS_REGION            = 'eu-est-2'
        AWS_CREDENTIALS_ID    = '25c9050a-a97c-46f2-9968-26db13b6e929'
        EB_APP_NAME           = 'Research-application'
        EB_ENV_NAME           = 'Research-application-env'
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    // Checkout code from GitHub
                    git credentialsId: '3ee2d6a3-1048-4e36-9916-2997af2165fc', url: 'https://github.com/sanket0770/researchapp.git'
                }
            }
        }

        stage('Build and Deploy') {
            steps {
                script {
                    // Deploy to AWS Elastic Beanstalk
                    withAWS(credentials: "${AWS_CREDENTIALS_ID}", region: "${AWS_REGION}") {
                        sh "eb init -p Python ${EB_APP_NAME} --region ${AWS_REGION}"
                        sh "eb use ${EB_ENV_NAME}"
                        sh "eb deploy"
                    }
                }
            }
        }
    }
}
