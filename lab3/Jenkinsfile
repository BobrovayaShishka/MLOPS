pipeline {
    agent any

    stages {
        stage('Download Data') {
            steps {
                sh '''
                python3 -m venv ./my_env
                . ./my_env/bin/activate
                pip install -r requirements.txt
                python3 MLOPS/lab3/download.py
                '''
            }
        }

        stage('Train Model') {
            steps {
                sh '''
                . ./my_env/bin/activate
                python3 train_model.py > best_model.txt
                '''
            }
        }

        stage('Deploy Model') {
            steps {
                sh '''
                . ./my_env/bin/activate
                export BUILD_ID=dontKillMe
                export JENKINS_NODE_COOKIE=dontKillMe
                path_model=$(cat best_model.txt | grep -oP 'runs:/\K.*')
                mlflow models serve -m "runs:/${path_model}" -p 5003 --no-conda &
                '''
            }
        }

        stage('Health Check') {
            steps {
                sh '''
                curl -X POST http://localhost:5003/invocations \
                -H 'Content-Type: application/json' \
                --data '{"inputs": [[1, 2, 3, 4, 5, 6, 7, 8]]}'
                '''
            }
        }
    }
}
