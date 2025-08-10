# 🛒 E-Commerce API (Django + DRF)

A modern e-commerce backend built with **Django REST Framework**, **JWT Authentication**, and **Swagger Documentation**.  
It supports user authentication, product management, orders, and customers — with Redis caching and Celery for async tasks.

## 🚀 Features

- **User Authentication** (JWT)
- **Product & Category CRUD** (with pagination)
- **Customer Management**
- **Order & OrderItem Models**
- **Swagger / OpenAPI Docs**
- **Redis Caching** for products & categories
- **Celery** for async tasks (e.g., sending emails)
- **Dockerized Deployment**
- **GitHub Actions** for CI/CD

## 📂 Project Structure

```
eccommerce_backend/
│
├── users/          # Authentication & user management
├── catalog/        # Products & categories
├── order/          # Orders & order items
├── customer/       # Customer profiles
├── eccommerce_backend/  # Project settings & urls
└── requirements.txt
```

## 🛠 Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/yourusername/ecommerce-backend.git
cd ecommerce-backend
```

### 2️⃣ Create a virtual environment & install dependencies
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3️⃣ Run migrations
```bash
python manage.py migrate
```

### 4️⃣ Create a superuser
```bash
python manage.py createsuperuser
```

### 5️⃣ Start the development server
```bash
python manage.py runserver
```

## 🔑 Authentication Flow

1. **Register**
```bash
curl -X POST http://127.0.0.1:8000/api/users/register/      -H "Content-Type: application/json"      -d '{"email": "test@example.com", "password": "123456"}'
```

2. **Login**
```bash
curl -X POST http://127.0.0.1:8000/api/users/login/      -H "Content-Type: application/json"      -d '{"email": "test@example.com", "password": "123456"}'
```

3. **Use token in requests**
```bash
curl -X GET http://127.0.0.1:8000/api/catalog/categories/      -H "Authorization: Bearer <access_token>"
```

## 📖 API Documentation

Swagger UI available at:
```
http://127.0.0.1:8000/swagger/
```

Redoc UI available at:
```
http://127.0.0.1:8000/redoc/
```

## ⚙ Environment Variables

| Variable                | Description                  |
|-------------------------|------------------------------|
| SECRET_KEY              | Django secret key            |
| DEBUG                   | True/False                   |
| DATABASE_URL            | PostgreSQL database URL      |
| REDIS_URL               | Redis connection string      |

## 🐳 Docker Setup

```bash
docker-compose up --build
```

## 📌 Roadmap

- [x] User & Auth APIs
- [x] Product & Category CRUD
- [x] Orders & Customers APIs
- [x] Swagger Docs
- [ ] Redis caching
- [ ] Celery async tasks
- [ ] GitHub Actions CI/CD

## 📜 License

MIT License
