pipeline {
  
    agent any


  stages {
  

    stage('Install Dependencies') {
      steps {
        echo 'Installing dependencies..'
        sh '''
        apt update
        apt install -y python3 python3-pip
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