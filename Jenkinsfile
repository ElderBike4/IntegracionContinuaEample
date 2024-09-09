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
                bat 'python ./tests/tests_operations.py'
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
        success {
            echo 'Pipeline completado exitosamente.'
        }
        failure {
            echo 'El pipeline falló.'
        }
        always {
            script {
                // Buscar el ID del contenedor basado en la imagen
                def containerId = bat(script: 'docker ps -a -q --filter "ancestor=operaciones-app"', returnStdout: true).trim()

                if (containerId) {
                    echo "Contenedor encontrado con ID: ${containerId}"

                    // Detener el contenedor
                    bat "docker stop ${containerId}"

                    // Eliminar el contenedor
                    bat "docker rm ${containerId}"
                } else {
                    echo "No se encontró ningún contenedor para la imagen 'operaciones-app'."
                }
            }
        }

    }
}
