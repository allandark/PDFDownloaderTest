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
          sh '''
          python -m venv venv
          . venv/bin/activate
          pip install --upgrade pip
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