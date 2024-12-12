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
   git clone https://github.com/VadimTrubay/expense_manager.git
   cd expense_manager
   ```
2. **Create a virtual environment It's recommended to use a
   virtual environment to isolate project dependencies:**

   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**

   ```bash
   venv\Scripts\activate
   ```

4. **Install dependencies Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ``` 

5. **Apply migrations After configuring the database, apply migrations:**

   ```bash
   python manage.py migrate
   ```

6. **Run the development server Start the local development server:**

   ```bash
   python manage.py runserver
   The server will be available at: http://127.0.0.1:8000
   the swager server will be available at: http://127.0.0.1:8000/api/schema/swagger-ui/
   ```