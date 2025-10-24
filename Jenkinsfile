pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/saraswathi06-18/BMI_project.git',
                    credentialsId: 'github-creds'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t bmi-app:1.0 .'
            }
        }

        stage('Push Docker Image') {
            steps {
                sh 'docker tag bmi-app:1.0 saraswathi1806/bmi-app:1.0'
                sh 'docker push saraswathi1806/bmi-app:1.0'
            }
        }
    }

    post {
        failure {
            echo "❌ Pipeline failed. Check errors above."
        }
        success {
            echo "✅ Pipeline executed successfully!"
        }
    }
}
