pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                echo 'Cloning repository...'
                git 'https://github.com/JakaxKato/sast-demo-app.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Setting up virtual environment and installing dependencies...'
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt || true
                    pip install bandit
                '''
            }
        }

        stage('Run Bandit Security Scan') {
            steps {
                echo 'Running Bandit scan...'
                sh '''
                    . venv/bin/activate
                    bandit -r . -f xml -o bandit-output.xml || true
                '''
            }
        }
    }

    post {
        always {
            echo 'Archiving Bandit result...'
            archiveArtifacts artifacts: 'bandit-output.xml', allowEmptyArchive: true

            echo 'Pipeline selesai. Periksa hasil scan keamanan jika ada.'
        }

        failure {
            echo 'Pipeline gagal. Periksa error log untuk detailnya.'
        }
    }
}
