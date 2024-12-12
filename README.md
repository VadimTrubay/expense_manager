# Expense Manager API

## Description

This is an API for managing expenses, allowing users to create, view, update, and delete expense records. The API is
built with Python using the Django REST Framework.

---

## Requirements

Before starting, ensure you have the following tools installed:

- Python 3.8 or newer
- pip (Python package manager)
- virtualenv (recommended for creating an isolated environment)
- PostgreSQL (if required by the project)

---

## Project Setup

1. **Clone the repository**
   Clone the repository to your local machine:
   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```
2. Create a virtual environment It's recommended to use a
   virtual environment to isolate project dependencies:

bash
Copy code
python -m venv venv
Activate the virtual environment:

On Windows:

   ```bash
  venv\Scripts\activate
   ```

Install dependencies Install the required packages:

bash
Copy code
pip install -r requirements.txt
Set up the database If your project uses a database, perform the following steps:

Create a PostgreSQL database (or another database, if specified in the project).
Configure the database connection in settings.py:
python
Copy code
DATABASES = {
'default': {
'ENGINE': 'django.db.backends.postgresql',
'NAME': '<database_name>',
'USER': '<username>',
'PASSWORD': '<password>',
'HOST': 'localhost',
'PORT': '5432',
}
}
Apply migrations After configuring the database, apply migrations:

bash
Copy code
python manage.py migrate
Run the development server Start the local development server:

bash
Copy code
python manage.py runserver
The server will be available at: http://127.0.0.1:8000