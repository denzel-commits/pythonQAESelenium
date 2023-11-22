pipeline {
    agent {
        node {
            label 'docker-agent-python'
            }
      }
    triggers {
        pollSCM 'H/5 * * * *'
    }
    stages {
        stage('Build') {
            steps {
                echo "Building..."
                sh '''
                echo "doing build stuff..."
                '''
                sh '''
                python3 -m venv venv
                venv/bin/pip3 install -r requirements.txt
                export PYTHONPATH=${pwd}
                '''
            }
        }
        stage('Test') {
            steps {
                echo "Testing..."
                sh '''
                echo "doing test stuff..."
                '''
            }
        }
        stage('Deliver') {
            steps {
                echo 'Deliver...'
                sh '''
                echo "doing delivery stuff..."
                '''
            }
        }
    }
}