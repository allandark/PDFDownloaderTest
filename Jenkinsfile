pipeline {
  
    agent {
        docker {
            image 'python:3.10'
        }
    }


  
  // environment {
  //     GITHUB_CREDENTIALS = credentials('github-personal-token')
  // }

  stages {
  

    stage('Install Dependencies') {
      steps {
        echo 'Installing dependencies..'
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