# 🛒 E-commerce REST API (Django)

## 📌 Description

A scalable and modular RESTful API for an E-commerce platform built using **Django** and **Django REST Framework**.
The API supports authentication, product management, cart operations, and order processing with a clean and maintainable architecture.

---

## 🌐 Live Demo

🔗 https://ecommerce-api-django.onrender.com/

---

## 🚀 Features

* 🔐 User Login Authentication (JWT-based)
* 🛍️ Product CRUD APIs
* 🗂️ Category Management
* 🛒 Cart Functionality
* 📦 Order Processing System
* 🧩 Modular Django Architecture (separate apps)
* 📄 API Documentation using Swagger

---

## 🛠️ Tech Stack

* Python
* Django
* Django REST Framework
* SQLite (default database)
* Gunicorn (for production server)
* Render (for deployment)

---

## 📁 Project Structure

```
ecommerce-api-django/
│
├── cart/        # Cart functionality
├── ecommerce/  # Main project settings
├── orders/     # Order management
├── products/   # Product APIs
├── users/      # Authentication
│
├── manage.py
├── requirements.txt
├── Procfile
└── .gitignore
```

---

## 🔗 API Endpoints

### 🔐 Authentication

* `POST /api/login/` → User login
* `POST /api/refresh/` → Refresh token

---

### 🛍️ Products

* `GET /api/products/` → List all products
* `POST /api/products/` → Create product
* `GET /api/products/{id}/` → Get product details
* `PUT /api/products/{id}/` → Update product
* `DELETE /api/products/{id}/` → Delete product

---

### 🛒 Cart

* `GET /api/cart/` → View cart
* `POST /api/cart/add/` → Add item to cart

---

### 📦 Orders

* `POST /api/order/` → Create order
* `GET /api/orders/` → Get all orders
* `GET /api/orders/history/` → Order history

---

### ⚙️ Admin Panel

* `/admin/`

---

### 📄 API Documentation

* `/swagger/`

---

## ⚙️ Setup Instructions

### 1. Clone Repository

```
git clone https://github.com/akif-ansari12/ecommerce-api-django.git
cd ecommerce-api-django
```

### 2. Create Virtual Environment

```
python -m venv myenv
```

### 3. Activate Environment

**Windows**

```
myenv\Scripts\activate
```

**Mac/Linux**

```
source myenv/bin/activate
```

### 4. Install Dependencies

```
pip install -r requirements.txt
```

### 5. Apply Migrations

```
python manage.py migrate
```

### 6. Run Server

```
python manage.py runserver
```

---

## 🧪 Testing

You can test the APIs using:

* Postman
* Swagger UI (`/swagger/`)

---

## 👨‍💻 Author

**Akif Ansari**

* GitHub: https://github.com/akif-ansari12
* LinkedIn: https://www.linkedin.com/in/akifansari12/

---

## ⭐ Note

* This project currently supports **login-based authentication only** (no user registration).
* Root URL (`/`) returns 404 — use `/api/...` endpoints.

---

## 💡 Future Improvements

* User Registration System
* Payment Gateway Integration
* PostgreSQL Database
* Docker Deployment
* Frontend Integration (React)

---

