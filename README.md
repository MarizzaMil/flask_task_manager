# 🐾 Task Tracker

Welcome to Task Tracker! This delightful little app helps you keep your tasks and categories organized in a cheerful way. Whether you're tackling daily chores, work assignments, or fun projects, Task Tracker is here to make your life a bit easier and a lot more colorful! 🌈

### 🌟 What It Does
Task Tracker is a cozy haven for your tasks, allowing you to:

* Create, read, update, and delete tasks with just a few clicks! 📝✨
* Organize tasks into categories so you can find what you need in a jiffy! 🎨
* Mark tasks as completed to celebrate your accomplishments! 🎉

### 🎈 Main Features

* User-Friendly Interface: Designed with you in mind! Navigate through your tasks and categories effortlessly.
* Secure Authentication: Your data is safe with us! Sign up and log in with a simple, secure process. 🔐
* Flexible Task Management: Easily manage tasks with different titles, descriptions, and categories.
* Logging and Error Handling: Keep things running smoothly with built-in logging to catch any bumps along the way. 🛠️
  
Join us in making task management a breeze! Happy tracking! 🥳

## Table of Contents

* Introduction
* Technologies Used
* Setup Instructions
* Running the Application
* Database Schema
* API Endpoints
* Additional Information

## Introduction

This project is a web application built using Flask for the backend, PostgreSQL as the database, and React for the frontend. The application allows users to manage tasks and categories efficiently.

## Technologies Used

* Backend: Flask
* Database: PostgreSQL
* Frontend: React
* ORM: SQLAlchemy
* Authentication: JWT
* Logging: Python's logging module

## Setup Instructions

To set up the project locally, follow these steps:

1. Clone the repositories:
```
git clone https://github.com/MarizzaMil/task-manager
git clone https://github.com/MarizzaMil/flask_task_manager
```



2. Set up a virtual environment (optional but recommended):
```
cd your-repo-name
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3Install dependencies:
```
pip install -r requirements.txt
```

4. Set up PostgreSQL database:

* Create a PostgreSQL database and user.
* Update your .env file or your application configuration with the database connection details.
  
5. Run migrations:

```
flask db upgrade
```

## Running the Application

To flask run the application, execute the following command:

```
flask run
```
The application will be available at http://127.0.0.1:5000.


For the React frontend, navigate to the frontend directory and run:
```
npm install
npm start
```
The frontend will be available at http://localhost:3000.

## Database Schema

The following tables are defined in the database:

###Users Table
* id (Integer, Primary Key): Unique identifier for each user.
* email (String, Unique, Not Null): User's email address.
* password_hash (String, Not Null): Hashed password for user authentication.

###Categories Table
* id (Integer, Primary Key): Unique identifier for each category.
* name (String, Unique, Not Null): Name of the category.
* description (Text): Optional description of the category.


###Tasks Table
* id (Integer, Primary Key): Unique identifier for each task.
* title (String, Not Null): Title of the task.
* description (Text): Optional description of the task.
* completed (Boolean, Default False): Task completion status.
* category_id (Integer, Foreign Key): Associated category ID.

## API Endpoints

### User Authentication

- POST /auth/signup
  - Register a new user.
  - Request Body: { "email": "string", "password": "string" }
  - Response: { "token": "string", "user": { "id": int, "email": "string" } }
    
- POST /auth/signin
  - Authenticate an existing user.
  - Request Body: { "email": "string", "password": "string" }
  - Response: { "token": "string", "user": { "id": int, "email": "string" } }
 
### Categories

- GET /categories/
  - Retrieve all categories.
  - Response: [ { "id": int, "name": "string", "description": "string" } ]

- POST /categories/
  - Create a new category.
  - Request Body: { "name": "string", "description": "string" }
  - Response: { "id": int, "name": "string", "description": "string" }

- PUT /categories/<id>
  - Update an existing category by ID.
  - Request Body: { "name": "string", "description": "string" }
  - Response: { "id": int, "name": "string", "description": "string" }

- DELETE /categories/<id>
  - Delete a category by ID.
  - Response: { "message": "Category deleted successfully" }

### Tasks

- GET /tasks/
  - Retrieve all tasks, optionally filtered by category.
  - Response: [ { "id": int, "title": "string", "description": "string", "completed": bool, "category": { "id": int, "name": "string" } } ]

- POST /tasks/
  - Create a new task.
  - Request Body: { "title": "string", "description": "string", "category": "string" | "category_id": int }
  - Response: { "id": int, "title": "string", "description": "string", "completed": bool }

- PUT /tasks/<id>
  - Update an existing task by ID.
  - Request Body: { "title": "string", "description": "string", "completed": bool, "category": "string" | "category_id": int }
  - Response: { "id": int, "title": "string", "description": "string", "completed": bool }

- DELETE /tasks/<id>
  - Delete a task by ID.
  - Response: { "message": "Task deleted successfully" }

## Additional Information
* Ensure to have PostgreSQL running and accessible during development.
* Check the logs for any errors that might occur while running the application.
* If you encounter issues with JWT, ensure that your secret key is set correctly in your environment variables.

