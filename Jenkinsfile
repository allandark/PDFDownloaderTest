pipeline {
  
    agent any


  stages {
  

    stage('Install Dependencies') {
      steps {
        echo 'Installing dependencies..'
        sh '''
        sudo apt update
        sudo apt install python3 -y
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