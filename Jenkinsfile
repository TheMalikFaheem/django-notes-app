pipeline {
    // -------------------------------------------------------------------------
    // 🔴 SETUP INSTRUCTION:
    // Replace "malik" with the Label of your own Jenkins Agent/Node.
    // If you are running on the master node, you can use "any" or "built-in".
    // -------------------------------------------------------------------------
    agent { label "malik" }

    stages {
        stage("1. Get Code") {
            steps {
                echo "Cloning from GitHub..."
                // 🔴 SETUP INSTRUCTION:
                // Replace the URL below with your own GitHub Repository URL
                git branch: "main", url: "https://github.com/TheMalikFaheem/django-notes-app.git"
            }
        }

        stage("2. Build & Push") {
            steps {
                echo "Building Docker Image..."
                // This builds the image locally. You can keep this name or change it.
                sh 'docker build -t notes-app-image:latest .'

                echo 'Logging in and Pushing to Docker Hub...'
                
                // ---------------------------------------------------------------------
                // 🔴 SETUP INSTRUCTION:
                // You must go to Jenkins Dashboard -> Manage Jenkins -> Credentials
                // and create a "Username with Password" credential.
                // 
                // ID: 'docker-hub-cred' (Or change the name below to match yours)
                // Username: Your Docker Hub Username
                // Password: Your Docker Hub Password/Access Token
                // ---------------------------------------------------------------------
                withCredentials([usernamePassword(credentialsId: 'docker-hub-cred', 
                                                  usernameVariable: 'DHuser', 
                                                  passwordVariable: 'DHpass')]) {
                    
                    // 1. Secure Login 
                    // (We use --password-stdin to keep the password hidden from logs)
                    sh 'echo $DHpass | docker login -u $DHuser --password-stdin'

                    // 2. Tag the image
                    // This dynamically adds your Docker Hub username to the image tag
                    sh "docker tag notes-app-image:latest ${DHuser}/notes-app-image:latest"

                    // 3. Push the image
                    sh "docker push ${DHuser}/notes-app-image:latest"
                }
            }
        }

        stage("3. Test") {
            steps {
                echo "Testing the Code..."
                // Add your test commands here (e.g., pytest, python manage.py test)
            }
        }

        stage("4. Deploy") {
            steps {
                echo "Deploying to EC2 instance..."
                
                // Ensure the database persistence folder exists on the server
                sh 'mkdir -p /home/ubuntu/notes_data'
                
                // Stop any existing containers to prevent port conflicts
                sh 'docker compose down || true'
                
                // Start the application using the local image we just built
                sh 'docker compose up -d'
                
                // Run database migrations
                sh 'docker exec notes-container python manage.py makemigrations notes'
                sh 'docker exec notes-container python manage.py migrate'
            }
        }
    }

    post {
        always {
            // Security Best Practice: Logout to protect credentials
            sh 'docker logout'
            
            // Maintenance: Clean up unused Docker objects to save disk space
            sh 'docker system prune -f' 
        }
    }
}
