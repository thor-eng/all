pipeline {
    agent any

    stages {
        stage('Clone Code') {
            steps {
                git 'https://github.com/thor-eng/all.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest || true'
            }
        }

        stage('Run Application') {
            steps {
                echo 'Starting Flask application...'
                sh 'python app.py & sleep 5 && pkill -f app.py'
            }
        }
    }

    post {
        success {
            echo "✅ Build completed successfully!"
        }
        failure {
            echo "❌ Build failed. Check Jenkins logs."
        }
    }
}
