# Django Library Project

A simple Django web application to manage books and authors.  
This project demonstrates Django models, relationships, templates, forms, and admin integration.

## Features

- List all books with author, price, and publication date
- View detailed information for each book
- Add new books using a form
- Manage books and authors via the Django admin panel
- Responsive Bootstrap-based design

## Models

- **Author**: name, birth date
- **Book**: title, author (ForeignKey), published date, price

## Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Ganna-M19/Django-Project.git
   cd Django-Project
   ```

2. **Create and activate a virtual environment:**
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

3. **Install dependencies:**
   ```powershell
   pip install django
   ```

4. **Apply migrations:**
   ```powershell
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser:**
   ```powershell
   python manage.py createsuperuser
   ```

6. **Run the development server:**
   ```powershell
   python manage.py runserver
   ```

7. **Access the app:**
   - Home: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
   - Admin: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

## License

This project is for educational purposes.