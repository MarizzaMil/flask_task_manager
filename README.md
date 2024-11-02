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

Introduction
Technologies Used
Setup Instructions
Running the Application
Database Schema
API Endpoints
Additional Information

## Table of Contents

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
  
5. Run migrations (if using Flask-Migrate):

```
flask db upgrade
```

## Running the Application




