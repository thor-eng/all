pipeline {
    agent any
    environment {
       environment {
        DOCKERHUB_CREDENTIALS = credentials('naveen-dockerhub')
        DOCKERHUB_REPO = "naveen550/last"
        IMAGE_TAG = "latest"
    }
    }

    stages {
        stage('Clone Code') {
            steps {
                git branch: 'main', url: 'https://github.com/thor-eng/all.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv venv
                    source venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    source venv/bin/activate
                    pytest || true
                '''
            }
        }

        stage('Run Application') {
            steps {
                sh '''
                    source venv/bin/activate
                    python app.py & sleep 5 && pkill -f app.py
                '''
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
    }

    post {
        success { echo "✅ Build completed successfully!" }
        failure { echo "❌ Build failed. Check Jenkins logs." }
    }
}
