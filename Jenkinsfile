pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                // Get some code from a GitHub repository
                git branch: 'Dev1', url: 'https://github.com/Sebziel/FunkyFlaskApp.git'

                // Create Venv
                sh 'python3 -m venv ~/my_environment'

                // activate Venv
                sh '''
                . ~/my_environment/bin/activate
                export FLASK_ENV=development
                echo "set up FLASK_ENV = " $FLASK_ENV
                export FLASK_APP=SimpleApp.py
                echo "set up FLASK_APP = " $FLASK_APP
                pwd
                pip install -r requirements.txt
                flask run --host=0.0.0.0 > /dev/null 2>&1 &
                '''
            }

        }
    }
}
