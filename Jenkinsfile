pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "saraswathi1806/bmi-app"
        KUBECONFIG_PATH = "C:\\Users\\22251\\.kube\\config"
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

        stage('Deploy to Kubernetes') {
            steps {
                withEnv(["KUBECONFIG=${env.KUBECONFIG_PATH}"]) {
                    // Use full path to YAML files in Jenkins workspace
                    bat "kubectl apply -f %WORKSPACE%\\k8s-deployment.yaml"
                    bat "kubectl apply -f %WORKSPACE%\\k8s-service.yaml"
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished.'
        }
    }
}
