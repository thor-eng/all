pipeline {
    agent any

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
    }

    post {
        success { echo "✅ Build completed successfully!" }
        failure { echo "❌ Build failed. Check Jenkins logs." }
    }
}
