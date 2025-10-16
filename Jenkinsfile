pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        echo 'Building..'
        // sh 'pip install -r requirements.txt'
      }
    }

    stage('Test') {
      steps {
        echo 'Testing..'
        // sh '''pytest tests/unit --junitxml="tests/results/unittest_report.xml"'''
        // sh '''pytest tests/integration --junitxml="tests/results/integrationtest_report.xml"'''
      }
    }

  }
}