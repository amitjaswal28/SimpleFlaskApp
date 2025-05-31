🚀 Flask Application CI/CD Pipelines
This project demonstrates two approaches to implement CI/CD pipelines for a Python Flask application:

Jenkins CI/CD Pipeline

GitHub Actions CI/CD Pipeline

📦 Requirements
Python 3.8+

pip, venv, pytest

requirements.txt file

GitHub repository with main and staging branches

🧪 Jenkins CI/CD Pipeline for Flask Application
✅ Overview
This Jenkins pipeline automates the following stages:

Checkout Source Code

Setup Python Environment

Install Dependencies

Run Tests

Deploy to Staging or Production

Send Email Notification

🛠️ Prerequisites
Jenkins installed (locally or cloud-based like Jenkins Blue Ocean)

Git plugin installed

Email notification configured (optional)

GitHub repository configured with a Jenkinsfile

![image](https://github.com/user-attachments/assets/7dabf3d0-9e74-4830-bddb-d9ce24d93128)
![image](https://github.com/user-attachments/assets/c6b7f2d1-b6b2-4f67-a07e-2fbf59592a8c)



⚙️ GitHub Actions CI/CD Pipeline for Flask App
✅ Overview
This GitHub Actions workflow automates:

Installing Python dependencies

Running tests

Deploying to Staging (on staging branch)

Deploying to Production (on release tag)
