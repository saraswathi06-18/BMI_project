pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "saraswathi1806/bmi-app"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/saraswathi06-18/BMI_project.git', credentialsId: 'github-creds'
            }
        }

        stage('Docker Login') {
            steps {
                withCredentials([string(credentialsId: 'dockerhub-pass', variable: 'DOCKERHUB_PASS')]) {
                    bat """
                    echo %DOCKERHUB_PASS% | docker login -u saraswathi1806 --password-stdin
                    """
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                bat "docker build -t %DOCKER_IMAGE%:latest ."
            }
        }

        stage('Push Docker Image') {
            steps {
                bat "docker push %DOCKER_IMAGE%:latest"
            }
        }

        stage('Run Docker Container') {
            steps {
                bat """
                docker stop bmi-app || echo Container not running
                docker rm bmi-app || echo Container not removed
                docker run -d -p 5000:5000 --name bmi-app %DOCKER_IMAGE%:latest
                """
            }
        }

        // ✅ Final Deployment Stage
        stage('Deployment Complete') {
            steps {
                echo "✅ Application is deployed and running at http://<your-server-ip>:5000"
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished.'
        }
    }
}
