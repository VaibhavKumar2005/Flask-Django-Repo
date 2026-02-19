# FlaskAuthApp - Employee Registration System

This project is a Flask-based employee management system featuring robust server-side validation and cloud deployment.

## Features
- **Backend Validation**:
  - Ensures Name, Email, and Password are not empty.
  - Validates that the Email is unique in the database.
  - Enforces a minimum password length of 6 characters.
- **Database**: Uses SQLite for local development and persistent storage.
- **Deployment**: Configured for seamless deployment on Render using Gunicorn.

## Setup and Installation
1. Clone the repository.
2. Navigate to the `FlaskAuthApp` directory.
3. Install dependencies: `pip install -r requirements.txt`.
4. Run the application: `python app.py`.

## Validation Logic
The application implements strict server-side checks in the `/register` route to prevent invalid data entry, even if front-end attributes are bypassed.