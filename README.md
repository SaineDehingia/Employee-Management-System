# Employee Management System API

A backend Employee Management System built using **FastAPI** and **MongoDB Atlas**. The project provides secure JWT authentication, employee management, department management, attendance tracking, leave management, file uploads, dashboard APIs, unit testing, and Docker support.

---

## Features

- JWT Authentication (Register & Login)
- Employee CRUD Operations
- Department CRUD Operations
- Attendance Management
- Leave Management
- Dashboard APIs
- File Upload
- MongoDB Atlas Integration
- Swagger API Documentation
- Unit Testing using Pytest
- Docker & Docker Compose Support

---

## Tech Stack

- Python 3.13
- FastAPI
- MongoDB Atlas
- PyMongo
- JWT Authentication
- Docker
- Swagger UI
- Pytest

---

## Project Structure

```text
Employee-Management-System/
│
├── app/
│   ├── routers/
│   ├── utils/
│   ├── static/
│   ├── templates/
│   ├── database.py
│   ├── models.py
│   └── main.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/SaineDehingia/Employee-Management-System.git
```

Go to the project:

```bash
cd Employee-Management-System
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python -m uvicorn app.main:app --reload
```

---

## Docker

Build the image:

```bash
docker compose build
```

Run the container:

```bash
docker compose up
```

---

## API Documentation

Swagger UI:

```
http://localhost:8000/docs
```

---

## Modules

- Authentication
- Employee
- Department
- Attendance
- Leave
- Dashboard
- Upload

---

## Future Improvements

- Email Notifications
- Role-Based Access Control
- Payroll Management
- Performance Evaluation
- Deployment on AWS

---

## Author

**Saine Dehingia**

M.Tech (Computer Science & Engineering)

Dibrugarh University
