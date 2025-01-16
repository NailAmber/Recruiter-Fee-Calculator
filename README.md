# REST API Documentation for Client Management System

## Overview
This API allows for managing clients, including adding, deleting, updating client formulas, calculating payments based on client-specific formulas, and retrieving a list of all clients. The API is built using Flask and uses SQLite for data storage.

## Base URL
```
http://<your-server-ip>:5000/
```

## Endpoints

### 1. Add Client
**POST** `/add_client`

Adds a new client with a specified formula for payment calculation.

#### Request Body
- `name` (string, required): The name of the client.
- `formula` (string, required): The formula used to calculate payments for the client.

#### Example
```json
{
    "name": "client1",
    "formula": "payment * 0.1"
}
```

#### Responses
- `201 Created`: Client added successfully.
  ```json
  {
      "status": "success",
      "message": "Client 'client1' added."
  }
  ```
- `400 Bad Request`: Missing required parameters.
  ```json
  {
      "status": "error",
      "message": "Name and formula are required."
  }
  ```
- `409 Conflict`: Client already exists.
  ```json
  {
      "status": "error",
      "message": "Client 'client1' already exists."
  }
  ```
- `500 Internal Server Error`: Server error.

### 2. Delete Client
**DELETE** `/delete_client/<name>`

Deletes an existing client by name.

#### URL Parameter
- `name` (string, required): The name of the client to be deleted.

#### Responses
- `200 OK`: Client deleted successfully.
  ```json
  {
      "status": "success",
      "message": "Client 'client1' deleted."
  }
  ```
- `404 Not Found`: Client not found.
  ```json
  {
      "status": "error",
      "message": "Client 'client1' not found."
  }
  ```
- `500 Internal Server Error`: Server error.

### 3. Update Client Formula
**PUT** `/update_client_formula`

Updates the formula for an existing client.

#### Request Body
- `name` (string, required): The name of the client.
- `new_formula` (string, required): The new formula for the client.

#### Example
```json
{
    "name": "client1",
    "new_formula": "payment * 0.2"
}
```

#### Responses
- `200 OK`: Formula updated successfully.
  ```json
  {
      "status": "success",
      "message": "Client 'client1' formula updated."
  }
  ```
- `400 Bad Request`: Missing parameters or incorrect formula.
  ```json
  {
      "status": "error",
      "message": "Name and new formula are required."
  }
  ```
  ```json
  {
      "status": "error",
      "message": "Formula is not correct."
  }
  ```
- `404 Not Found`: Client not found.
- `500 Internal Server Error`: Server error.

### 4. Calculate Payment
**POST** `/calculate_payment`

Calculates the payment for a specified client based on their formula.

#### Request Body
- `client_name` (string, required): The name of the client.
- `payment` (float, required): The amount to be used in the calculation.

#### Example
```json
{
    "client_name": "client1",
    "amount": 1000
}
```

#### Responses
- `200 OK`: Calculation successful.
  ```json
  {
      "status": "success",
      "payment": 100.0,
      "formula": "payment * 0.1"
  }
  ```
- `400 Bad Request`: Missing parameters.
  ```json
  {
      "status": "error",
      "message": "Client name and amount are required."
  }
  ```
- `404 Not Found`: Client not found.
- `500 Internal Server Error`: Server error.

### 5. Get All Clients
**GET** `/get_all_clients`

Retrieves a list of all clients.

#### Responses
- `200 OK`: List of clients retrieved successfully.
  ```json
  {
      "status": "success",
      "clients": [
          [1, "client1", "payment * 0.1"],
          [2, "client2", "payment * 0.2"]
      ]
  }
  ```
- `500 Internal Server Error`: Server error.

### 6. Add Admin
**POST** `/add_admin`

Adds a new Admin.

#### Request Body
- `id` (string\int, required): telegram id of the new Admin.

#### Example
```json
{
    "id": "123123123"
}
```

#### Responses
- `201 Created`: Admin added successfully.
  ```json
  {
      "status": "success",
      "message": "Admin '123213213' added."
  }
  ```
- `400 Bad Request`: Missing required parameters or id is not a number.
  ```json
  {
      "status": "error",
      "message": "Admin id is required as number."
  }
  ```
- `409 Conflict`: Admin already exists.
  ```json
  {
      "status": "error",
      "message": "Admin '123213213' already exists."
  }
  ```
- `500 Internal Server Error`: Server error.

### 7. Remove Admin
**DELETE** `/remove_admin/<id>`

Removes an existing Admin by id.

#### URL Parameter
- `id` (string\int, required): The telegram id of the Admin to be deleted.

#### Responses
- `200 OK`: Admin removed successfully.
  ```json
  {
      "status": "success",
      "message": "Admin '123213123' deleted."
  }
  ```
- `400 Bad Request`: Missing required parameters or id is not a number.
  ```json
  {
      "status": "error",
      "message": "Admin id is required as number."
  }
  ```
- `404 Not Found`: Admin not found.
  ```json
  {
      "status": "error",
      "message": "Admin '123213213' not found."
  }
  ```
- `500 Internal Server Error`: Server error.

### 8. Get All Admins
**GET** `/get_all_admins`

Retrieves a list of all Admins.

#### Responses
- `200 OK`: List of Admins retrieved successfully.
  ```json
  {
      "status": "success",
      "admins": [
          [123123123],
          [213213232]
      ]
  }
  ```
- `500 Internal Server Error`: Server error.

## Error Handling
All error responses include a `status` field indicating "error" and a `message` field providing more details about the error.

## Notes
- Ensure the API server is running before making any requests.
- Use appropriate headers (`Content-Type: application/json`) for requests with a body.
- Handle possible server errors and invalid inputs gracefully in your client application.

