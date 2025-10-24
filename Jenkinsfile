pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('naveen-dockerhub')
        DOCKERHUB_REPO = "naveen550/last"
        IMAGE_TAG = "latest"
    }

    stages {
        stage('SCM Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/thor-eng/all.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t naveen550/last:latest .'
            }
        }

        stage('Login to DockerHub') {
            steps {
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
            }
        }

        stage('Push Image') {
            steps {
                sh 'docker push naveen550/last:latest'
            }
        }
    }

    post {
        always {
            sh 'docker logout'
        }
        success {
            echo "✅ Build and push completed successfully!"
        }
        failure {
            echo "❌ Build failed. Please check Jenkins logs."
        }
    }
}
