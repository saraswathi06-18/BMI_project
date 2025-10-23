pipeline {
    agent any

    environment {
        // Docker Hub credentials ID in Jenkins
        DOCKERHUB_CREDENTIALS = 'dockerhub-creds'
        // Docker image name with your Docker Hub username
        IMAGE_NAME = 'saraswathi1806/bmi-app:1.0'
    }

    stages {
        // 1️⃣ Clone code from GitHub using PAT
        stage('Clone Repository') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/saraswathi1806/BMI_project.git',
                    credentialsId: 'github-creds'
            }
        }

        // 2️⃣ Build Docker image
        stage('Build Docker Image') {
            steps {
                script {
                    // Run Docker build
                    sh "docker build -t ${IMAGE_NAME} ."
                }
            }
        }

        // 3️⃣ Push Docker image to Docker Hub
        stage('Push Docker Image') {
            steps {
                script {
                    // Login and push
                    withCredentials([usernamePassword(credentialsId: "${DOCKERHUB_CREDENTIALS}", 
                                                     usernameVariable: 'USERNAME', 
                                                     passwordVariable: 'PASSWORD')]) {
                        sh 'echo $PASSWORD | docker login -u $USERNAME --password-stdin'
                        sh "docker push ${IMAGE_NAME}"
                    }
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished!'
        }
        success {
            echo '✅ BMI App Docker image pushed successfully!'
        }
        failure {
            echo '❌ Pipeline failed. Check errors above.'
        }
    }
}
