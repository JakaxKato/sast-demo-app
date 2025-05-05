pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/JakaxKato/sast-demo-app.git', branch: 'master'
            }
        }

        stage('Setup Virtualenv') {
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
                    bandit -f xml -o bandit-output.xml -r . -x venv,__pycache__ || exit_code=$?; [ $exit_code -le 1 ] || exit $exit_code
                '''
                recordIssues tools: [bandit(pattern: 'bandit-output.xml')]
            }
        }
    }
}
