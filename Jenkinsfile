pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                // Get some code from a GitHub repository
                git branch: 'Dev1', url: 'https://github.com/Sebziel/FunkyFlaskApp.git'

                // Create Venv
                sh 'python3 -m venv my_4environment'

                // activate Venv
                sh '. my_4environment/bin/activate'
                
                //set env variables
                sh 'export FLASK_ENV=development'
                sh 'echo "set up FLASK_ENV = " $FLASK_ENV'
                sh 'export FLASK_APP=SimpleApp.py'
                sh 'echo "set up FLASK_APP = " $FLASK_APP'
            }

        }
    }
}
