pipeline {
  
    agent {
        docker {
            image 'python:3.13.7'
             args '-u root'
        }
    }

  stages {
    stage('Install Dependencies') {

      steps {
          echo '--- Installing dependencies ---'
          sh 'python --version'
          sh '''
          pip install -r requirements.txt
          '''
      }
    }

    stage('Test') {
      steps {
        echo '--- Testing and generating reports ---'
        sh '''pytest tests/unit --junitxml="tests/results/unittest_report.xml"'''
        sh '''pytest tests/integration --junitxml="tests/results/integrationtest_report.xml"'''
        junit 'tests/results/*.xml'
      }
    }   
     
    post {
      always {
        archiveArtifacts artifacts: 'tests/results/*.xml', fingerprint: true
      }
    }
  }
}