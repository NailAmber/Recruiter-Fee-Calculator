# 🚀 Client Management REST API Documentation

A Flask-based REST API for managing clients and administrators with payment calculation capabilities.

## 📚 Table of Contents
- [Overview](#-overview)
- [Base URL](#-base-url)
- [API Endpoints](#-api-endpoints)
  - [Client Management](#-client-management)
  - [Admin Management](#-admin-management)
- [Error Handling](#%EF%B8%8F-error-handling)
- [Quick Start](#-quick-start)
- [Notes](#-notes)

## 🌐 Overview
![Flask](https://img.shields.io/badge/Framework-Flask-green) ![SQLite](https://img.shields.io/badge/Database-SQLite-blue)

This API provides endpoints for:
- 🧑💼 Client management (CRUD operations)
- 🧮 Payment calculations using custom formulas
- 👨💻 Admin management (Add/Remove/List)

## 🔗 Base URL
```
http://<your-server-ip>:5000/
```

## 📡 API Endpoints

### 📋 Client Management

#### 1. ➕ Add Client
**`POST`** `/add_client`

Adds a new client with a specified formula for payment calculation.

**Request Body:**
```json
{
    "name": "client1",
    "formula": "payment * 0.1"
}
```

**Responses:**
- `201 Created`
  ```json
  {
      "status": "success",
      "message": "Client 'client1' added."
  }
  ```
- `400 Bad Request`
  ```json
  {
      "status": "error",
      "message": "Name and formula are required."
  }
  ```
- `409 Conflict`
  ```json
  {
      "status": "error",
      "message": "Client 'client1' already exists."
  }
  ```

#### 2. 🗑️ Delete Client
**`DELETE`** `/delete_client/<name>`

Deletes an existing client by name.

**Responses:**
- `200 OK`
  ```json
  {
      "status": "success",
      "message": "Client 'client1' deleted."
  }
  ```
- `404 Not Found`
  ```json
  {
      "status": "error",
      "message": "Client 'client1' not found."
  }
  ```

#### 3. 🔄 Update Formula
**`PUT`** `/update_client_formula`

Updates the formula for an existing client.

**Request Body:**
```json
{
    "name": "client1",
    "new_formula": "payment * 0.2"
}
```

**Responses:**
- `200 OK`
  ```json
  {
      "status": "success",
      "message": "Client 'client1' formula updated."
  }
  ```
- `400 Bad Request`
  ```json
  {
      "status": "error",
      "message": "Name and new formula are required."
  }
  ```
- `404 Not Found`

#### 4. 💰 Calculate Payment
**`POST`** `/calculate_payment`

Calculates the payment for a specified client based on their formula.

**Request Body:**
```json
{
    "client_name": "client1",
    "payment": 1000
}
```

**Responses:**
- `200 OK`
  ```json
  {
      "status": "success",
      "payment": 100.0,
      "formula": "payment * 0.1"
  }
  ```
- `400 Bad Request`
  ```json
  {
      "status": "error",
      "message": "Client name and amount are required."
  }
  ```
- `404 Not Found`

#### 5. 📜 List All Clients
**`GET`** `/get_all_clients`

Retrieves a list of all clients.

**Responses:**
- `200 OK`
  ```json
  {
      "status": "success",
      "clients": [
          [1, "client1", "payment * 0.1"],
          [2, "client2", "payment * 0.2"]
      ]
  }
  ```

### 👨💻 Admin Management

#### 6. ➕ Add Admin
**`POST`** `/add_admin`

Adds a new admin.

**Request Body:**
```json
{
    "id": "123123123"
}
```

**Responses:**
- `201 Created`
  ```json
  {
      "status": "success",
      "message": "Admin '123123123' added."
  }
  ```
- `400 Bad Request`
  ```json
  {
      "status": "error",
      "message": "Admin id is required as number."
  }
  ```
- `409 Conflict`

#### 7. 🗑️ Remove Admin
**`DELETE`** `/remove_admin/<id>`

Removes an existing admin.

**Responses:**
- `200 OK`
  ```json
  {
      "status": "success",
      "message": "Admin '123123123' deleted."
  }
  ```
- `400 Bad Request`
- `404 Not Found`

#### 8. 📜 List All Admins  
**`GET`** `/get_all_admins`  

Retrieves a list of all Admins.  

**Responses:**  
- `200 OK`  
  ```json
  {
    "status": "success",
    "admins": [
        [123456789],
        [987654321]
    ]
  }
  ```
- `500 Internal Server Error`  
  ```json
  {
    "status": "error",
    "message": "Internal server error."
  }
  ```

## ⚠️ Error Handling
All errors follow this format:
```json
{
    "status": "error",
    "message": "Detailed error description"
}
```

## 🚦 Quick Start
```
pip install flask
python restapi.py
```

## 📌 Notes
- 🔒 Always use HTTPS in production
- 📁 Database file is automatically created
- 📋 Request/Response examples use JSON format
- 🐍 Requires Python 3.8+ and Flask 2.0+
- 💡 Use Postman or Insomnia for API testing!
