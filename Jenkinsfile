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
        success {
            emailext (
                subject: "Jenkins: Tests PASSED - ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: "Build Success. Test results attached.\n\n${env.BUILD_URL}",
                to: "${env.CHANGE_AUTHOR_EMAIL ?: 'instructor@example.com'}"
            )
        }
        failure {
            emailext (
                subject: "Jenkins: Tests FAILED - ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: "Build Failed. Please review test results: ${env.BUILD_URL}",
                to: "${env.CHANGE_AUTHOR_EMAIL ?: 'instructor@example.com'}"
            )
        }
    }
}
