# Noventra CRM – Client Lead Management System

## Future Interns – Full Stack Web Development Internship

**Task:** Task 2 – Client Lead Management System (Mini CRM)
**Repository:** `FUTURE_FS_02`

## Live Demo

[Open Noventra CRM](https://noventra-crm.onrender.com/dashboard/)

## Project Overview

Noventra CRM is a web-based Client Lead Management System developed as part of the Future Interns Full Stack Web Development Internship.

The application helps businesses manage client leads efficiently by allowing users to add, view, update, search, filter, and track leads throughout the sales process.

## Key Features

* User authentication and login
* Dashboard with lead statistics
* Add new leads
* View complete lead information
* Edit existing leads
* Delete leads
* Search leads
* Filter leads by status
* Track lead sources
* Track lead status
* Assign leads to users
* Add follow-up information
* Import leads from Excel
* Responsive web interface
* PostgreSQL database integration
* Deployment using Render

## Technologies Used

### Frontend

* HTML5
* CSS3
* JavaScript
* Bootstrap

### Backend

* Python
* Django

### Database

* PostgreSQL

### Other Tools

* Git
* GitHub
* Render
* Gunicorn
* WhiteNoise

## How the Application Works

The application follows Django's MVT architecture.

1. The user logs into the CRM.
2. The dashboard displays important lead statistics.
3. Users can create and manage client leads.
4. Lead information is stored in the PostgreSQL database.
5. Users can search and filter leads based on different criteria.
6. Follow-up information can be added to individual leads.
7. The application processes requests through Django views.
8. Django models communicate with the database.
9. HTML templates display the information to the user.
10. The complete application is deployed online using Render.

## Project Structure

```text
FUTURE_FS_02/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── leads/
│   ├── migrations/
│   ├── management/
│   ├── templates/
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── manage.py
├── requirements.txt
├── runtime.txt
└── README.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/joycemary05/FUTURE_FS_02.git
cd FUTURE_FS_02
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure environment variables

Create a `.env` file or configure the required environment variables for the project.

Do not upload secret keys, passwords, or other sensitive information to GitHub.

### 6. Run migrations

```bash
python manage.py migrate
```

### 7. Start the development server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

## Learning Outcomes

Through this project, I gained practical experience in:

* Django web application development
* MVT architecture
* Database design and migrations
* CRUD operations
* Form handling
* User authentication
* Search and filtering
* Backend and frontend integration
* PostgreSQL database integration
* Git and GitHub
* Deployment using Render
* Managing environment variables securely

## Challenges Solved

During development, I worked on solving challenges related to:

* Django project configuration
* Database migration
* Connecting Django with PostgreSQL
* Managing environment variables
* Implementing lead management functionality
* Deploying the application to Render
* Configuring the production server

## Future Improvements

Possible future improvements include:

* Email notifications
* Advanced analytics
* Role-based permissions
* Automated follow-up reminders
* Exporting lead reports
* Improved dashboard analytics

## Internship

This project was developed as part of the **Future Interns Full Stack Web Development Internship**.

**Track:** Full Stack Web Development
**Track Code:** FS
**Task:** 02

## Author

**Joycemary**

B.Tech Information Technology
