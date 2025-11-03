pipeline {
    agent any

    environment {
        MINIKUBE = 'C:\\Users\\User\\Desktop\\Fall 25-26\\EECE 430\\miniKube\\minikube.exe'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/ntm088/movieapp-minikube.git'
            }
        }

        stage('Set Docker to use Minikube') {
            steps {
                bat '''
                "%MINIKUBE%" docker-env --shell=cmd > docker_env.bat
                call docker_env.bat
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                bat '''
                docker build -t movieapp:latest .
                docker images
                '''
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                bat '''
                "%MINIKUBE%" kubectl -- apply -f k8s\\deployment.yaml
                "%MINIKUBE%" kubectl -- apply -f k8s\\service.yaml
                "%MINIKUBE%" kubectl -- rollout status deployment/django-deployment
                "%MINIKUBE%" kubectl -- get pods
                '''
            }
        }
    }
}
