pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'operaciones-app'
        TEST_IMAGE = 'python:3.12'
        TEST_SCRIPT = './tests/tests_operations.py'
    }

    stages {
        stage('Checkout') {
            steps {
                // Clonar el repositorio
                git credentialsId: 'github-token', url: 'https://github.com/ElderBike4/IntegracionContinuaEample.git', branch: 'main'
            }
        }
        
        stage('Build') {
            steps {
                script {
                    // Construir la imagen de Docker
                    sh 'docker build -t ${DOCKER_IMAGE} .'
                }
            }
        }
        
        stage('Run Tests') {
            steps {
                script {
                    // Ejecutar el contenedor auxiliar para pruebas
                    def appContainer = docker.run("${DOCKER_IMAGE}", '-d -p 8081:80')

                    // Esperar a que la aplicación esté disponible
                    sleep(time: 30, unit: 'SECONDS')

                    // Ejecutar las pruebas en un contenedor de prueba
                    docker.image("${TEST_IMAGE}").inside {
                        sh 'pip install selenium'
                        sh "python ${TEST_SCRIPT}"
                    }

                    // Detener y eliminar el contenedor auxiliar después de las pruebas
                    appContainer.stop()
                    appContainer.remove()
                }
            }
        }
        
        stage('Deploy') {
            when {
                expression { currentBuild.result == 'SUCCESS' }
            }
            steps {
                script {
                    // Desplegar la aplicación en el contenedor oficial (o en el entorno de producción)
                    echo 'Desplegando la aplicación'
                    // Aquí puedes agregar comandos para desplegar la aplicación en el contenedor oficial
                }
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
    }
}
