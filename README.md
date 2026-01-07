# Django Notes App with CI/CD Pipeline

A full-stack Notes application built with **Django**, containerized using **Docker**, and deployed via an automated **Jenkins CI/CD Pipeline**.

This project demonstrates a complete **DevOps workflow**:

- **Build**: Creates a Docker image from the source code  
- **Push**: Tags and pushes the image to Docker Hub for backup  
- **Deploy**: Uses Docker Compose to deploy the container to an AWS EC2 instance with persistent storage  

---

## 🚀 Features

- **Create, Edit, Delete Notes**: Simple and intuitive UI  
- **Dockerized**: Runs anywhere with a single command  
- **Data Persistence**: Uses Docker Volumes to ensure data is safe even if containers restart  
- **Automated Pipeline**: Jenkinsfile included for "Click-to-Deploy" functionality  
- **Security**: Uses `stdin` for secure Docker login in CI/CD  

---

## 🛠️ Tech Stack

- **Backend**: Python, Django  
- **Containerization**: Docker, Docker Compose  
- **CI/CD**: Jenkins (Declarative Pipeline)  
- **Registry**: Docker Hub  
- **Infrastructure**: AWS EC2 (Ubuntu)  

---

## 🏃‍♂️ How to Run Locally (No Jenkins)

If you just want to run the app on your machine:

### Clone the Repo

```bash
git clone https://github.com/TheMalikFaheem/django-notes-app.git
cd django-notes-app
```

### Run with Docker Compose

```bash
docker compose up -d
```

### Access the App

Open your browser and go to:  
👉 http://localhost:8000

---

## ⚙️ How to Setup the Jenkins Pipeline

To use the included `Jenkinsfile` for automated deployment, follow these steps.

### 1. Configure Jenkins Credentials

Go to **Manage Jenkins → Credentials** and add a new **Username with password** credential:

- **ID**: `docker-hub-cred` *(Must match exactly)*  
- **Username**: Your Docker Hub username  
- **Password**: Your Docker Hub password or access token  

---

### 2. Update the Agent Label

Open `Jenkinsfile` and find the `agent` section at the top.

If you have a specific agent, keep the label:

```groovy
agent { label "malik" }
```

If you want to run on any available node, change it to:

```groovy
agent any
```

---

### 3. Run the Job

Create a **Pipeline Job** in Jenkins, point it to your GitHub repository, and click **Build Now**.

The Pipeline will automatically:

- Checkout code  
- Build the Docker Image  
- Log in securely and push the image to Docker Hub  
- Deploy the app using Docker Compose  
- Run database migrations  
- Clean up unused images to save disk space  

---

## 📂 Project Structure

```plaintext
django-notes-app/
├── Dockerfile
├── Jenkinsfile
├── docker-compose.yml
├── requirements.txt
├── manage.py
├── notes_project/          # Main Project Configuration
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── notes/                  # The App Logic
    ├── __init__.py
    ├── admin.py
    ├── models.py
    ├── urls.py
    ├── views.py
    └── templates/
        └── notes/
            ├── base.html
            ├── note_list.html
            └── note_form.html
```

---

## 👨‍💻 Author

**Malik Faheem Ahmad**  
DevOps & Cloud Engineer

🔗 [Let’s connect:](https://www.linkedin.com/in/imalikfaheem/)
