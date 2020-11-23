pipeline {
  agent any
  stages {

    stage('Hello') {
      steps {
        script {
          python -c "print('hello world')"
        }
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
