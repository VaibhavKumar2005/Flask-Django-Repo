# FlaskAuthApp - Employee Registration System

This project is a Flask-based employee management system featuring robust server-side validation and cloud deployment.

## Features
- **Backend Validation**:
  - [cite_start]Ensures Name, Email, and Password are not empty[cite: 24, 25, 26].
  - [cite_start]Validates that the Email is unique in the database[cite: 27].
  - [cite_start]Enforces a minimum password length of 6 characters[cite: 28].
- **Database**: Uses SQLite for local development and persistent storage.
- [cite_start]**Deployment**: Configured for seamless deployment on Render using Gunicorn[cite: 37, 97].