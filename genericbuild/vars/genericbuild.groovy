def call() {

    stages{
        stage('Stage1'){
            echo 'echoing from stage 1' 
        }
        stage('stage2'){
            echo 'echoing from stage 2' 
        }
    }
}
