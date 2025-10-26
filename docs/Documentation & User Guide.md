# 📚 PeerConnect Documentation & User Guide

**Project:** PeerConnect  
**Author:** Mahdi  
**Date:** 26-Oct-2025  

---

## 1️⃣ Project Overview
**PeerConnect** is a platform for university students to connect with classmates for study sessions, group projects, or peer tutoring. The app is designed for usability and simplicity and currently includes:

- User registration  
- User login  

Future features include:

- Searching for peers by course or topic  
- Creating or joining study sessions  
- Sending messages within groups  
- Viewing peer skill levels  

---

## 2️⃣ Application Structure

### 2.1 Main Components

- **`app/main.py`**  
  The entry point of the application. Initializes the FastAPI app and includes routers for authentication.  

- **`app/auth/controller.py`**  
  Contains API endpoints for authentication:  
  - `/auth/register` → Register new users  
  - `/auth/login` → Log in existing users  

- **`app/auth/service.py`**  
  Contains the business logic for authentication, including:  
  - Registering users in the in-memory store  
  - Hashing and verifying passwords  
  - Login validation  

- **`app/auth/models.py`**  
  Defines data models for requests and responses using Pydantic:  
  - `RegisterRequest` / `RegisterResponse`  
  - `LoginRequest` / `LoginResponse`  

- **`tests/`**  
  Contains unit and integration tests for the app:  
  - `test_service.py` → Tests the logic in `service.py`  
  - `test_controller.py` → Tests API endpoints  

---

## 3️⃣ API Overview

### 3.1 Register User
- **Endpoint:** `/auth/register`  
- **Function:** Allows a new user to create an account  
- **Input:** Name, Email, Password  
- **Output:** Success message or error if email exists  

### 3.2 Login User
- **Endpoint:** `/auth/login`  
- **Function:** Allows an existing user to log in  
- **Input:** Email, Password  
- **Output:** Success message with optional token or error if credentials are invalid  

---

## 4️⃣ User Guide – How to Use PeerConnect

### Register
1. Navigate to `/auth/register`  
2. Provide:
   - Name  
   - Email  
   - Password  
3. Submit request  
4. Successful registration returns a confirmation message.  
5. If the email is already registered, an error message is returned.  

### Login
1. Navigate to `/auth/login`  
2. Provide:
   - Email  
   - Password  
3. Submit request  
4. Successful login returns a confirmation message and token.  
5. Invalid credentials return an error message.  

> ✅ After logging in, future features like searching peers, creating sessions, and messaging will be accessible.

---

## 5️⃣ Notes on Implementation

- Passwords are securely hashed using PBKDF2-HMAC-SHA256  
- The app uses an in-memory user store for testing and demonstration purposes  
- All endpoints return standardized JSON responses  
- Code follows modular design for maintainability and future expansion  

---

## 6️⃣ Future Enhancements

- Persistent database storage for users and sessions  
- JWT-based authentication  
- Peer search and skill-level display  
- Real-time messaging and session notifications  
- Web and mobile UI improvements for better usability  

---

## 7️⃣ Summary
This document serves as both **developer documentation** and a **user guide**. It explains the structure of the application, the functionality of each component, and how a user can interact with the current features (registration and login). Future updates will expand these instructions as new features are implemented.
