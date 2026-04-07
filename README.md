# Task Tracker App

A simple Flask-based task tracker app that lets users create and manage tasks.

## Features

- View tasks
- Create tasks
- Mark tasks as complete
- Store task data in JSON
- Simple HTML and CSS frontend using Flask templates

## Tech Stack

- Python
- Flask
- HTML
- CSS

## Project Structure

```text
Task Tracker App/
├── app.py
├── manager.py
├── models.py
├── data.json
├── requirements.txt
├── README.md
├── .gitignore
├── structure.txt
│
├── static/
│   └── style.css
│
├── templates/
│   ├── base.html
│   ├── create.html
│   └── index.html

```

## Installation & Setup

1. Clone the repository
   ```
   git clone https://github.com/yourusername/task-tracker-app.git
   cd task-tracker-app
   ```
2. Create a virtual environment
   ```
   python -m venv .venv
   ```
3. Activate the virtual environment
   Windows PowerShell
   .venv\Scripts\Activate.ps1
   Windows Command Prompt
   .venv\Scripts\activate
4. Install dependencies
   ```
   pip install -r requirements.txt
   ```
5. Run the application
   python app.py
6. Open in your browser
   http://127.0.0.1:5000/

## How It Works

- The application uses Flask routes to handle requests
- Task data is managed through manager.py
- Tasks are stored in data.json
- HTML templates render dynamic content using Flask’s templating engine

## Application Routes

Route Method Description
/ GET Display all tasks
/create GET, POST Create a new task
/complete/<id> GET Mark a task as complete

## Requirements

- ython 3.x
- pip

## Future Improvements

- Edit tasks
- Delete tasks
- Add due dates
- Add task priority levels
- Replace JSON storage with a database (SQLite/PostgreSQL)
- User authentication (login/signup)
- REST API version of the app

## Notes

This project is a beginner-friendly Flask application designed to demonstrate:

- Backend development with Python
- Web routing and request handling
- Template rendering
- Basic application structure

It can be extended into a full-stack production-ready application.
