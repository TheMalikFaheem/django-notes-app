pipeline {
    agent { label "malik" }

    stages {
        stage("code") {
            steps {
                echo "Cloning from GitHub..."
                git branch: "main", url: "https://github.com/TheMalikFaheem/django-notes-app.git"
            }
        }

        stage("build") {
            steps {
                echo "Building Docker Image..."
                sh 'docker build -t notes-app-image:latest .'

                echo 'Logging in and Pushing...'
                
                withCredentials([usernamePassword(credentialsId: 'docker-hub-cred', 
                                                  usernameVariable: 'DHuser', 
                                                  passwordVariable: 'DHpass')]) {
                    
                    sh 'echo $DHpass | docker login -u $DHuser --password-stdin'
                    sh "docker tag notes-app-image:latest ${DHuser}/notes-app-image:latest"
                    sh "docker push ${DHuser}/notes-app-image:latest"
                }
            }
        }

        stage("test") {
            steps {
                echo "Testing the Code..."
            }
        }

        stage("deploy") {
            steps {
                echo "Deploying to EC2 instance..."
                sh 'mkdir -p /home/ubuntu/notes_data'
          
                sh 'docker compose down || true'
                
                sh 'docker compose up -d'
                
                sh 'docker exec notes-container python manage.py makemigrations notes'
                sh 'docker exec notes-container python manage.py migrate'
            }
        }
    }
    post {
        always {
            sh 'docker logout'

            sh 'docker system prune -f' 
        }
    }
}
