pipeline {
    agent any

    stages {
        stage('Set parameters') {
            steps {
                script{
                    properties([
                        parameters([
                            choice(
                                choices: ['Build and test', 'Build run and Restart the App'],
                                description: '''Restart required if changes have been done in the App''',
                                name: 'ChooseAction')])])
                }
            }
        }
        stage('PreReqs') {
            steps {
                // Get some code from a GitHub repository
                git branch: 'JenkinsLocalDev', url: 'https://github.com/Sebziel/FunkyFlaskApp.git'

                // Create Venv
                sh 'python3 -m venv ~/my_environment'
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
                // Activate Venv, running tests
                sh '''
                . ~/my_environment/bin/activate
                pytest | tee testresults.log
                '''
            }
        }
        stage('Post-build') {
            steps {
                //archiving app logs, requirements used in builiding and test results
                archiveArtifacts artifacts: 'testresults.log', followSymlinks: false
                archiveArtifacts artifacts: 'requirements.txt', followSymlinks: false
                archiveArtifacts artifacts: 'record.log', followSymlinks: false
            }

        }
        stage('Restart the app') {
            when {
                expression {
                    return params.ChooseAction == "Build run and Restart the App"
                }
            }
            steps{
                sh '''
                pkill -f SimpleApp.py
                . ~/my_environment/bin/activate
                JENKINS_NODE_COOKIE=dontKillMe nohup python3 SimpleApp.py > log.txt 2>&1 &
                '''
        }
    }
}
}
