pipeline {
  agent any

  
  environment {
      GITHUB_CREDENTIALS = credentials('github-personal-token')
  }

  stages {
  
    stage('Clone Repo') {
        steps {
            git url: 'https://github.com/allandark/PDFDownloaderTest',
                credentialsId: 'github-personal-token'
        }
    }

    stage('Build') {
      steps {
        echo 'Building..'
        echo "Using GitHub username: ${env.GITHUB_CREDENTIALS_USR}"
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