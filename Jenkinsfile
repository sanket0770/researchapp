pipeline {
    agent any


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
                     withCredentials([[$class: 'AmazonWebServicesCredentialsBinding', credentialsId: '25c9050a-a97c-46f2-9968-26db13b6e929', accessKeyVariable: 'AKIAX3LNWYOGIVRPHOXY', secretKeyVariable: '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']])
                    {
                        sh 'eb init -p python'
                        bat 'eb use Research-application-env'
                        bat 'eb deploy'
                    }
                }
            }
        }
    }
}
