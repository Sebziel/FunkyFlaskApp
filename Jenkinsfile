pipeline {
    agent any

    stages {
        stage('PreReqs') {
            steps {
                // Get some code from a GitHub repository
                git branch: 'Dev1', url: 'https://github.com/Sebziel/FunkyFlaskApp.git'

                // Create Venv
                sh 'python3 -m venv ~/my_environment'

                // activate Venv
                sh '''
                . ~/my_environment/bin/activate
                pip install -r requirements.txt
                JENKINS_NODE_COOKIE=dontKillMe nohup python3 SimpleApp.py > log.txt 2>&1 &
                '''
            }

        }
        stage('Build and run') {
            steps {
                // activate Venv, install dependencies, run application
                sh '''
                . ~/my_environment/bin/activate
                pip install -r requirements.txt
                JENKINS_NODE_COOKIE=dontKillMe nohup python3 SimpleApp.py > log.txt 2>&1 &
                '''
            }

        }
        stage('Tests') {
            steps {
                echo 'Some Test will hopefully be there'
            }
        }
        stage('Post-build') {
            steps {
                echo 'Some postbuild stepst like sending e-mail confrmation will be there'
            }

        }
    }
}
