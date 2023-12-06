pipeline {
    agent any

    environment {
        AWS_REGION = 'eu-west-2'
        AWS_ACCESS_KEY_ID = credentials('AKIAX3LNWYOGIVRPHOXY')
        AWS_SECRET_ACCESS_KEY = credentials('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')
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    // Checkout the code from GitHub
                    checkout scm
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    // Install Python dependencies
                    bat 'pip install -r requirements.txt'
                }
            }
        }

        stage('Deploy to Elastic Beanstalk') {
            steps {
                script {
                    // Deploy to Elastic Beanstalk
                    bat 'eb deploy MyElasticBeanstalkAppEnv0001112'
                }
            }
        }
    }

    post {
        always {
            // Clean up or additional steps after deployment
        }
    }
}
