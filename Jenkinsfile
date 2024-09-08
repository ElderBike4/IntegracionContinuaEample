pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                // Clonar el repositorio
                git credentialsId: 'github-token', url: 'https://github.com/ElderBike4/IntegracionContinuaEample.git', branch: 'main'
            }
        }
        stage('Build') {
            steps {
                // Construir y levantar el servidor en Windows
                bat 'docker build -t operaciones-app .'
                bat 'docker run -d -p 8081:80 operaciones-app'
            }
        }
        stage('Test') {
            steps {
                // Ejecutar las pruebas automatizadas en Windows
                bat 'python -m unittest discover -s tests -p test_operations.py'
            }
        }
        stage('Deploy') {
            when {
                expression { currentBuild.result == 'SUCCESS' }
            }
            steps {
                // Desplegar la aplicación (puede ser un servidor o contenedor)
                echo 'Desplegando la aplicación'
            }
        }
    }
    post {
        always {
            // Limpieza del contenedor en Windows
            bat 'for /f "tokens=*" %i in ('docker ps -q') do docker stop %i'
        }
        success {
            echo 'Pipeline completado exitosamente.'
        }
        failure {
            echo 'El pipeline falló.'
        }
    }
}
