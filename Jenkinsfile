pipeline {
    agent any
    stages {
        stage('Run Tests and Sleep') {
            parallel {
                stage('Test') {
                    steps {
                        sh 'python3 -m pytest test_add.py'
                    }
                }
                stage('Sleep') {
                    steps {
                        sleep(time: 3, unit: 'SECONDS')
                    }
                }
            }
        }
    }
}

