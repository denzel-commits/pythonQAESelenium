pipeline {
    agent {
        node {
            label 'docker-agent-python'
            }
      }
    environment{
        PYTHONPATH = "${WORKSPACE}"
    }
    parameters{
        string(name: 'BASE_URL', defaultValue: 'http://192.168.1.127:8081', description: 'Enter system Base URL')
        string(name: 'EXECUTOR', defaultValue: 'http://192.168.1.127:4444', description: 'Enter remote executor URL')
        choice(name: 'BROWSER', choices: ['chrome', 'firefox', 'edge', 'safari'], description: 'Select browser name')
        choice(name: 'BROWSER_VERSION', choices: ['119.0'], description: 'Select browser version')
        choice(name: 'WORKERS_NUMBER', choices: ['1', '2', '3', '4', '5'], description: 'Select the number of selenium workers')
        choice(name: 'LOG_LEVEL', choices: ['WARNING', 'INFO'], description: 'Log level')
    }
    stages {
        stage('Build') {
            steps {
                echo "Building..."
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                echo "Testing..."
                sh "python3 -m pytest -n=${params.WORKERS_NUMBER} --logging_level=${params.LOG_LEVEL} --base_url=${params.BASE_URL} --executor=${params.EXECUTOR} --browser=${params.BROWSER} --bv=${params.BROWSER_VERSION}"
            }
        }
    }
    post{
        always{
        allure([
                includeProperties: false,
                jdk: '',
                properties: [],
                reportBuildPolicy: 'ALWAYS',
                results: [[path: 'target/allure-results']]
            ])
        }
    }

}