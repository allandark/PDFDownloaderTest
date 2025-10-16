pipeline {
  
    agent {
        docker {
            image 'python:3.13.7'
        }
    }

  stages {
    stage('Install Dependencies') {

      steps {
          sh 'python --version'
          sh '''
          pip install -r requirements.txt
          '''
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