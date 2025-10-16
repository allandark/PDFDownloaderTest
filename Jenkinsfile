pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh 'pip install -r requirements.txt'
      }
    }

    stage('Test') {
      steps {
        sh '''pytest tests/unit --junitxml="tests/results/unittest_report.xml"'''
        sh '''pytest tests/integration --junitxml="tests/results/integrationtest_report.xml"'''
      }
    }

  }
}