pipeline {
    agent any
    stages {
        stage('Download Data') {
            steps {
                sh 'python scripts/download_data.py'
            }
        }
        stage('Preprocess Data') {
            steps {
                sh 'python scripts/preprocess_data.py'
            }
        }
        stage('Train Model') {
            steps {
                sh 'python scripts/train_model.py'
            }
        }
        stage('Deploy Model') {
            steps {
                sh 'python scripts/deploy_model.py &'
            }
        }
        stage('Test Model') {
            steps {
                sh 'curl -X POST http://localhost:5000/predict -H "Content-Type: application/json" -d \'{"MedInc": 8.3252, "HouseAge": 41, "AveRooms": 6.984, "AveBedrms": 1.0238, "Population": 322, "AveOccup": 2.555, "Latitude": 37.88, "Longitude": -122.23}\''
            }
        }
    }
}
