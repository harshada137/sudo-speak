
# 📄 `EXECUTION.md`

````md
# Project Execution Guide
Two-Tier Flask Application using Docker & Docker Compose

---

## Prerequisites
- Ubuntu EC2 Instance (AWS)
- Docker installed
- Docker Compose installed
- Git installed
- Open inbound ports:
  - 22 (SSH)
  - 80 (HTTP)

---

## Step 1: Clone the Repository
```bash
git clone https://github.com/harshada137/sudo-speak.git
cd two-tier-flask-app
````

---

## Step 2: Configure Environment Variables

Create a `.env` file in the project root:

```env
MYSQL_HOST=mysql
MYSQL_USER=root
MYSQL_PASSWORD=your_password
MYSQL_DB=tech_confessions
```

---

## Step 3: Verify Docker Compose Configuration

Ensure `docker-compose.yml` defines:

* Flask service
* MySQL service
* Custom network
* Volume mapping for MySQL data

---

## Step 4: Start the Application

```bash
docker-compose up -d
```

This will:

* Pull required images
* Create containers
* Set up networking
* Initialize the database

---

## Step 5: Verify Running Containers

```bash
docker ps
```

Both containers (`flask-app`, `mysql`) should be in **running** state.

---

## Step 6: Access the Application

Open a browser and visit:

```
http://<EC2-PUBLIC-IP>
```

---

## Step 7: Verify Database Persistence

1. Submit data through the UI
2. Stop containers:

```bash
docker-compose down
```

3. Restart containers:

```bash
docker-compose up -d
```

4. Refresh the browser — data should still exist

---

## Step 8: Image Security Scan (Optional but Recommended)

```bash
docker scout cves <image-name>
```

---

## Step 9: Cleanup (Optional)

```bash
docker-compose down
```

To remove volumes:

```bash
rm -rf mysql-data
```

---

## Execution Outcome

* Application deployed successfully on AWS EC2
* Multi-container setup managed via Docker Compose
* Persistent database storage verified
* Secure and scalable deployment achieved

```

---

If you want next, I can:
- ✔ polish this for **college submission**
- ✔ convert this into **resume bullet points**
- ✔ add **Docker Scout output explanation**
- ✔ add **architecture diagram description**

Just tell me 👍
```

