# 🛒 E-commerce API (Django REST Framework)

## 📌 Description
This is a modular RESTful API for an E-commerce platform built using Django and Django REST Framework.  
It handles login-based authentication, product management, cart system, and order processing.

---

## 🚀 Features
- User Login Authentication
- Product CRUD APIs
- Category Management
- Cart Functionality
- Order Processing
- Modular Django architecture (separate apps)

---

## 🛠️ Tech Stack
- Python
- Django
- Django REST Framework
- SQLite (default)

---

## 📁 Project Structure

ecommerce-api-django/
- cart/ →      Cart functionality
- ecommerce/ →   Main project settings
- orders/ →    Order management
- products/ →  Product APIs
- users/ →     Login authentication
- manage.py
- requirements.txt
- .gitignore

---

## 📂 API Endpoints

### Authentication
POST /api/login/

### Products
GET /api/products/  
POST /api/products/  
GET /api/products/{id}/  
PUT /api/products/{id}/  
DELETE /api/products/{id}/  

### Cart
GET /api/cart/  
POST /api/cart/add/  

### Orders
POST /api/orders/  
GET /api/orders/  

---

## ⚙️ Setup Instructions

https://github.com/akif-ansari12/ecommerce-api-django.git  
cd ecommerce-api-django  

python -m venv myenv  

# Activate:
# Windows
myenv\Scripts\activate  

# Mac/Linux
source myenv/bin/activate  

pip install -r requirements.txt  
python manage.py migrate  
python manage.py runserver  

---

## 🧪 Testing
Use Postman/swagger to test API endpoints/.

---

## 👨‍💻 Author
Akif Ansari  
GitHub: https://github.com/akif-ansari12   
LinkedIn: https://www.linkedin.com/in/akifansari12/ 

---

## ⭐ Note
This project currently supports login-only authentication (no registration).

