# Deploying the Credit Card Fraud Detection App

This steps explains how to set up and run the containerized Credit Card Fraud Detection application in a Linux environment (local machine or AWS EC2).

---

### 1️⃣ Prerequisites

Make sure the following are installed:  
- Git – to clone the repository  
- Docker – to build and run the container  

---

### 2️⃣ Manual Deployment Steps

```bash
# Update & upgrade system
sudo apt update && sudo apt upgrade -y

# Install Git and Docker
sudo apt install git docker.io -y

# Enable and start Docker service
sudo systemctl enable docker
sudo systemctl start docker

# Check Docker version
docker --version

# Clone repository
git clone https://github.com/darshan-bs-2005/docker-example.git
cd docker-example

# Build Docker image
docker build -t fraud-detection-app .

# Run Docker container
docker run -d -p 5000:5000 fraud-detection-app

### Access the Application

- **Local Machine:**  
  http://localhost:5000

- **AWS EC2:**  
  http://<EC2_PUBLIC_IP>:5000

> **Note:** Make sure your AWS EC2 security group allows inbound traffic on port 5000.
	
