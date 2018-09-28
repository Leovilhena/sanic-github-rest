pipeline {
    agent none
    stages {
        stage(’Testing’) {
            agent { docker { image 'python:3.7'} }
            steps {
                script {
                    stage(‘Pytest testing’) {
			sh 'pip install -r requirements.txt'		
			sh 'python -m pytest tests/ -v --cov=tests -s'
                    }
		    stage(‘Code format testing’){
			sh 'flake8 -v'
		    }
                }
            }
        }
    }
}