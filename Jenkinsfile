pipeline {
  agent any
  stages {

    stage('Hello') {
      steps {
          sh '''
		python -c "print('hello world')"
		'''

      }
    }

    stage('Get Weather') {
      steps {
        script {
          python3 get_weather.py
        }
      }
    }

  }
}
