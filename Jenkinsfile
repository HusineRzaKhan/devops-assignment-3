pipeline {
    agent any

    environment {
        IMAGE = "devops-assignment-3-test:${env.BUILD_NUMBER}"
        TARGET_URL = "https://factaccount.blog"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    // Build docker image on Jenkins agent
                    sh "docker build -t ${IMAGE} ."
                }
            }
        }
        stage('Run Tests in Container') {
            steps {
                script {
                    sh '''
                    mkdir -p $(pwd)/results
                    docker run --rm \
                        -e TARGET_URL=${TARGET_URL} \
                        -v $(pwd)/results:/opt/tests/results \
                        ${IMAGE}
                    '''
                }
            }
            post {
                always {
                    // copy results out in case container wrote them elsewhere
                    sh 'ls -la results || true'
                }
            }
        }
        stage('Archive Results') {
            steps {
                junit 'results/junit.xml'
                publishHTML (target: [
                  allowMissing: true,
                  alwaysLinkToLastBuild: true,
                  keepAll: true,
                  reportDir: 'results',
                  reportFiles: 'report.html',
                  reportName: 'Selenium HTML Report'
                ])
                archiveArtifacts artifacts: 'results/**', fingerprint: true
            }
        }
    }

    post {
        always {
            emailext(
                subject: "Jenkins Build #${BUILD_NUMBER}: ${currentBuild.currentResult}",
                body: "Build Result: ${currentBuild.currentResult}\n\nCheck console output at: ${BUILD_URL}",
                recipientProviders: [[$class: 'DevelopersRecipientProvider']]
            )
        }
    }
}