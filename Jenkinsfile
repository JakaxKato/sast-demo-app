pipeline {
    agent any

    tools {
        // opsional: jika kamu pakai Python dari Jenkins tool config
        // python 'Python 3.10'
    }

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/JakaxKato/sast-demo-app.git', branch: 'master'
            }
        }

        stage('Setup Python Env') {
            steps {
                sh 'python3 --version'
                sh 'pip3 install --upgrade pip'
                sh 'pip3 install bandit'
                sh 'bandit --version'
            }
        }

        stage('SAST Analysis') {
            steps {
                // Jalankan bandit, jika gagal tetap lanjut
                sh 'bandit -f xml -o bandit-output.xml -r . || true'

                // Cek file-nya ada atau tidak (debug)
                sh 'ls -lah bandit-output.xml || echo "File not found!"'

                // Integrasi ke Jenkins Warning Plugin
                recordIssues tools: [bandit(pattern: 'bandit-output.xml')]
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'bandit-output.xml', allowEmptyArchive: true
        }

        failure {
            echo 'Pipeline gagal, silakan cek error log.'
        }

        success {
            echo 'SAST Analysis selesai dan berhasil.'
        }
    }
}
