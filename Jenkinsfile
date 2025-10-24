pipeline {
    agent any

    environment {
        DOCKERHUB_REPO = 'saraswathi1806/bmi-app'
    }

    stages {
        stage('Checkout SCM') {
            steps {
                git(
                    url: 'https://github.com/saraswathi06-18/BMI_project.git',
                    branch: 'main',
                    credentialsId: 'github-creds'
                )
            }
        }

        stage('Build Docker Image') {
            steps {
                bat "docker build -t ${DOCKERHUB_REPO} ."
            }
        }

        stage('Login to DockerHub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'DOCKERHUB_CREDENTIALS', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                    bat 'docker login -u %USERNAME% -p %PASSWORD%'
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                bat "docker push ${DOCKERHUB_REPO}"
            }
        }
    }

    post {
        success {
            echo "Docker image pushed successfully!"
        }
        failure {
            echo "Pipeline failed. Check errors above."
        }
    }
}
