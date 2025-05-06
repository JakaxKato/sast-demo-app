pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                echo 'Cloning repository...'
                git 'https://github.com/JakaxKato/sast-demo-app.git' // Ganti dengan URL repo kamu
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing dependencies...'
                sh 'pip install -r requirements.txt || true' // agar tetap jalan jika requirements kosong
                sh 'pip install bandit || true' // pastikan Bandit terinstal
            }
        }

        stage('Run Bandit Security Scan') {
            steps {
                echo 'Running Bandit scan...'
                sh 'bandit -r . -f xml -o bandit-output.xml || true'
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
