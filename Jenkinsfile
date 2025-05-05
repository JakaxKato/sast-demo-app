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
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install bandit
                '''
            }
        }

        stage('SAST Analysis') {
            steps {
                sh '''
                    . venv/bin/activate
                    bandit -f xml -o bandit-output.xml -r . || true
                    ls -lah bandit-output.xml || echo "File not found!"
                '''
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
