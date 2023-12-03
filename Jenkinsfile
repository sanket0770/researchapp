pipeline {
    agent any

    environment {
        AWS_ACCESS_KEY_ID     = credentials('AKIAX3LNWYOGIVRPHOXY')
        AWS_SECRET_ACCESS_KEY = credentials('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')
        AWS_REGION            = 'eu-west-2'
        EB_APP_NAME           = 'research-application'
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

        stage('Build and Deploy') {
            steps {
                script {
                    withAWS(credentials: '25c9050a-a97c-46f2-9968-26db13b6e929', region: 'eu-west-2') {
                        bat 'eb init -p your-platform-name ${EB_APP_NAME}'
                        bat 'eb use ${EB_ENV_NAME}'
                        bat 'eb deploy'
                    }
                }
            }
        }
    }
}
