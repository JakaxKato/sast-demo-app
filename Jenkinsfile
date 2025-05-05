pipeline {
    agent any

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
                sh 'bandit -f xml -o bandit-output.xml -r . || true'
                sh 'ls -lah bandit-output.xml || echo "File not found!"'
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
