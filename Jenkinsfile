pipeline {
  
    agent {
        docker {
            image 'python:3.10'
        }
    }

  stages {
    stage('Install Dependencies') {

      steps {
          sh 'python --version'
          sh 'ls'
          sh 'python -m pip install --upgrade pip'
          sh 'python -m pip install -r requirements.txt'
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