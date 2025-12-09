# API Prototype

This is a minimal REST API built with Express.js demonstrating basic CRUD operations.

## Setup Instructions

1. **Initialize the project**:
   npm init -y

2. **Install Dependencies**:
   npm install express

3. **Run the API**:
   node src/index.js

## API Endpoints

| Method | Endpoint     | Description            |
|--------|--------------|------------------------|
| GET    | /items       | Get all items          |
| GET    | /items/:id   | Get item by ID         |
| POST   | /items       | Create a new item      |
| PUT    | /items/:id   | Update an existing item|
| DELETE | /items/:id   | Delete an item         |
