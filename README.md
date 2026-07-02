# 🚀 Employee Management System API

![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115-green?style=for-the-badge&logo=fastapi)
![MongoDB](https://img.shields.io/badge/MongoDB-Atlas-brightgreen?style=for-the-badge&logo=mongodb)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue?style=for-the-badge&logo=docker)
![JWT](https://img.shields.io/badge/Auth-JWT-orange?style=for-the-badge)

A production-ready **Employee Management System REST API** built using **FastAPI**, **MongoDB Atlas**, and **JWT Authentication**. The project provides secure authentication, employee management, attendance tracking, leave management, dashboard analytics, file upload support, unit testing, and Dockerized deployment.

---

# ✨ Features

- 🔐 JWT Authentication
- 👨‍💼 Employee Management (CRUD)
- 🏢 Department Management (CRUD)
- 📅 Attendance Management
- 📝 Leave Management
- 📊 Dashboard APIs
- 📂 File Upload
- ☁ MongoDB Atlas
- 🐳 Docker Support
- 📄 Swagger Documentation
- ✅ Unit Testing with Pytest

---

# 🛠 Tech Stack

| Technology | Purpose |
|------------|----------|
| FastAPI | Backend Framework |
| MongoDB Atlas | Cloud Database |
| PyMongo | Database Driver |
| JWT | Authentication |
| Docker | Containerization |
| Swagger | API Testing |
| Pytest | Unit Testing |

---

# 📁 Project Structure

```text
Employee-Management-System
│
├── app
│   ├── routers
│   ├── utils
│   ├── static
│   ├── templates
│   ├── database.py
│   ├── models.py
│   └── main.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/SaineDehingia/Employee-Management-System.git
```

Move into the project

```bash
cd Employee-Management-System
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the project

```bash
python -m uvicorn app.main:app --reload
```

---

# 🐳 Docker

Build

```bash
docker compose build
```

Run

```bash
docker compose up
```

---

# 📚 API Documentation

Swagger UI

```
http://localhost:8000/docs
```

---

# 📌 API Modules

- Authentication
- Employee
- Department
- Attendance
- Leave
- Dashboard
- Upload

---

# 🔮 Future Enhancements

- Role-Based Access Control
- Email Notifications
- Payroll Module
- Performance Evaluation
- AWS Deployment
- CI/CD Pipeline

---

# 👩‍💻 Author

**Saine Dehingia**

M.Tech – Computer Science & Engineering

Dibrugarh University
