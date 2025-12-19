# Two-Tier Flask Application – Dockerized Deployment **SUDO SPEAK**

## Project Overview
This project demonstrates the containerization of a **two-tier web application** using **Docker** and **Docker Compose**, following industry-standard DevOps practices.  
The application consists of:

- **Frontend + Backend:** Flask-based web application
- **Database:** MySQL relational database

The project focuses on **container orchestration**, **networking between containers**, **data persistence using volumes**, and **security awareness through image scanning**.

---

## Project Guide
**Shubham Londhe**

---

## Architecture Overview
- The Flask application serves a dynamic frontend and handles backend logic.
- MySQL is used to store application data persistently.
- Docker Compose manages multi-container deployment.
- Containers communicate over a custom Docker network.
- Docker volumes ensure database data persists beyond container lifecycle.

---

## Functionalities

### 1. Web Application (Flask)
- Displays user-submitted content dynamically.
- Allows users to submit new entries via the frontend.
- Supports interaction features (e.g., upvotes).
- Fetches and stores data in the MySQL database.

### 2. Database Layer (MySQL)
- Stores application data in structured tables.
- Initializes schema automatically at container startup.
- Persists data using Docker volumes.

### 3. Containerization
- Each component runs in an isolated Docker container.
- Environment variables are used for configuration.
- Lightweight and portable deployment.

### 4. Orchestration with Docker Compose
- Single command deployment for the entire application stack.
- Automatic service dependency handling.
- Custom Docker network for secure inter-container communication.

### 5. Data Persistence
- MySQL data is stored on the host machine using volumes.
- Data remains intact even after containers are stopped or removed.

### 6. Security Awareness
- Docker images can be scanned using **Docker Scout** to identify vulnerabilities.
- Encourages secure image usage and best practices.

---

## Repository & Image References

### Original GitHub Repository (Project Source)
👉 **https://github.com/LondheShubham153/two-tier-flask-apP**

### Docker Hub Repository (Your Image)
👉 **https://hub.docker.com/repositories/harshaa137**

---

## Key Learnings
- Practical understanding of Docker and Docker Compose
- Two-tier application architecture
- Container networking and volume management
- Secure and scalable application deployment
- Real-world DevOps workflow implementation

---

## Use Case
This project is suitable for:
- DevOps learning and practice
- Resume and portfolio demonstration
- Interview discussions on Docker-based deployments
