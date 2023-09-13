pipeline {
    agent any
    stages {
    parallel {
            stage('test') {
                steps {
                    sh 'python3 -m pytest test_add.py'
                }
            }
            stage('sleep') {
                steps {
                    sleep(time: 3, unit: 'SECONDS')
                }
            }
        }
    }
}
