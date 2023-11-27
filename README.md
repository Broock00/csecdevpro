# csecdevpro

# CSEC Development Division - Django Web Application

This Django web application is designed for the CSEC Development Division. It includes user authentication, event management, and more.

## Features

- **User Management:**
  - User registration and login functionality.
  - User deletion.

- **Events:**
  - Displaying events ordered by date and time.
  - Adding and deleting events.

- **Dashboard:**
  - Displaying a list of all users.

## Setup

To run this project locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/Broock00/csecdevpro.git



How to run...
#Apply Migrations
    python manage.py migrate
    python manage.py makemirations

#Create a superuser for admin access:
    python manage.py createsuperuser

#Run the development server:
    python manage.py runserver

'''Access the application at http://localhost:8000.'''


#Usage

Create a new user through the registration page.
Log in using valid credentials on the login page.

Navigate through the different sections:
    Home
    Events
    About
    Dashboard (admin access required)
    Add and delete events through the respective pages.
