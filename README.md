Taskflow

Taskflow is a clean, efficient task management web application built with Django. It helps users organize their daily workflows by categorizing tasks, tracking their progress (Pending, In Progress, Completed), and maintaining a focused workspace.

Features

User Authentication: Secure signup and login system using a custom user model.

Task Management: Full Create, Read, Update, and Delete (CRUD) functionality for daily tasks.

Categorization: Group tasks by custom categories to keep your dashboard organized.

Status Tracking: Easily update task status to visualize your progress.

Responsive Design: Built with Bootstrap for a seamless experience on both desktop and mobile.

Tech Stack

Framework: Django (Python)

Frontend: Bootstrap 5, HTML5, CSS3

Database: SQLite3

Project Structure

authApp/: Handles user registration, login, and authentication logic.

taskApp/: The core application containing task and category models, views, and logic.

templates/: Centralized location for HTML structure.

Installation

Clone the repository:

git clone https://github.com/SAshraf2001/Django-TodoApp-Project


Install the required dependencies:

pip install django


Navigate to the project directory and run migrations:

python manage.py makemigrations
python manage.py migrate


Start the development server:

python manage.py runserver


Access the app at: http://127.0.0.1:8000/

Future Roadmap

[ ] Implement Task Priority (High/Medium/Low)

[ ] Add Due Dates and deadline tracking

[ ] Integrate ModelForms for streamlined data entry
