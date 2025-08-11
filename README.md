Deploying the Credit Card Fraud Detection App

This guide explains how to set up and run the containerized Credit Card Fraud Detection application in a Linux environment (local machine or AWS EC2).

⸻

1) Prerequisites

Make sure the following are installed:
	•	Git – to clone the repository
	•	Docker – to build and run the container

2) Install Git & Docker:

sudo apt update && sudo apt upgrade -y
sudo apt install git docker.io -y
sudo systemctl enable docker
sudo systemctl start docker
docker --version

3) Clone the Repository:
git clone https://github.com/darshan-bs-2005/docker-example.git
cd docker-example

4) Build the Docker Image:
docker build -t fraud-detection-app .

5) Run the Docker Container
docker run -d -p 5000:5000 fraud-detection-app

6) Access the Application
	•	Local Machine → http://localhost:5000
	•	AWS EC2 → http://<EC2_PUBLIC_IP>:5000

Make sure AWS EC2 security group allows inbound traffic on port 5000.



