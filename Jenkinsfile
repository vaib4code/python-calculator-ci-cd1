pipeline {
    agent any

    environment {
        PYTHON = 'C:/Users/vaib0/AppData/Local/Programs/Python/Python314/python.exe'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Verify Python') {
            steps {
                bat '"%PYTHON%" --version'
            }
        }

        stage('Install Robot Framework') {
            steps {
                bat '"%PYTHON%" -m pip install robotframework'
            }
        }

        stage('Run Robot Tests') {
            steps {
                bat '"%PYTHON%" -m robot tests'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'tests/**, log.html, report.html, output.xml', allowEmptyArchive: true
        }
        success {
            echo 'Build passed. Smoke tests completed successfully.'
        }
        failure {
            echo 'Build failed. Check console output and Robot reports.'
        }
    }
}
