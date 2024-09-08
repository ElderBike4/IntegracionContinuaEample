pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                // Clonar el repositorio
                git 'https://github.com/usuario/proyecto-operaciones.git'
            }
        }
        stage('Build') {
            steps {
                // Construir y levantar el servidor
                sh 'docker build -t operaciones-app .'
                sh 'docker run -d -p 8080:80 operaciones-app'
            }
        }
        stage('Test') {
            steps {
                // Ejecutar las pruebas automatizadas
                sh 'python3 -m unittest tests/test_operations.py'
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
            // Limpieza del contenedor
            sh 'docker stop $(docker ps -q)'
        }
        success {
            echo 'Pipeline completado exitosamente.'
        }
        failure {
            echo 'El pipeline falló.'
        }
    }
}
  
