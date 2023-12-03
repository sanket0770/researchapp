pipeline {
    agent any

    environment {
        AWS_REGION = 'eu-west-2'
        AWS_EB_ENVIRONMENT = 'Research-application-env'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Deploy to Elastic Beanstalk') {
            steps {
                script {
                    def elasticBeanstalk = [
                        region: AWS_REGION,
                        credentials: '25c9050a-a97c-46f2-9968-26db13b6e929',
                        applicationName: 'Research-application',
                        environmentName: AWS_EB_ENVIRONMENT,
                        
                    ]

                    awsElasticBeanstalkDeploy(elasticBeanstalk)
                }
            }
        }
    }
}
