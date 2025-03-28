# 📝 Taskify API
A simple Task Management API built using Django REST Framework. This API allows users to **Create, Read, Update, and Delete (CRUD)** tasks.

## 🚀 Features  
- List all tasks  
- Create a new task  
- Retrieve a specific task  
- Update an existing task  
- Delete a task
## 🛠️ Tech Stack
- Python (v3.x)
- Django (v4.x)
- Django REST Framework
- PostgreSQL (for database)
- Docker (optional)
## 🛠️ Installation  

### Clone the Repository  
```bash
git clone git@github.com:PritomKarmokar/taskify.git
cd taskify-api
```
### Copy .env.example to .env
Before running the project, copy the `.env.example` file and update it with your database credentials:
```bash
cp .env.example .env
```
📌 Make sure to update the `.env` file with the correct values! 
```bash
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost

# Database Settings
DB_NAME=todo_db
DB_USER=postgres
DB_PASSWORD=postgres
# Change 'DB_HOST' to 'db' when running docker
DB_HOST=localhost
DB_PORT=5432
```

### Create & Activate a Virtual Environment  
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Install Dependencies 
```bash
pip install -r requirements.txt 
```

### Set Up the Database
```bash
python manage.py migrate
```

### Create a Superuser (Optional)
```bash
python manage.py createsuperuser
```

### Run the Development Server
```bash
python manage.py runserver
```
The API will be available at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## 🏗️ API Endpoints

| Method | Endpoint                        | Description        |
|--------|---------------------------------|--------------------|
| GET    | `/api/tasks/`                   | List all tasks    |
| POST   | `/api/tasks/create/`            | Create a new task |
| GET    | `/api/tasks/retrieve/<task_id>/` | Retrieve a task   |
| PATCH  | `/api/tasks/update/<task_id>/`   | Update a task     |
| DELETE | `/api/tasks/delete/<task_id>/`   | Delete a task     |

## 🐳 Running the Project with Docker

If you want to run this project inside a Docker container, follow these steps:
### Copy .env.example to .env
```bash
cp .env.example .env
```
📌 Update your .env file to set database credentials and any other required variables.

### Build the Docker container:

```bash
docker-compose up --build
```
### Run database migrations:
```bash
docker-compose run django-web python manage.py migrate
```
### Run database migrations:
```bash
docker-compose run django-web python manage.py createsuperuser
```

The API will be available at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## 🧪 Running Tests (Optional)
This project includes unit tests to ensure API functionality.
### Run All Tests
To execute all test cases, run the following command:

```bash
python manage.py test
```

### Run Tests with Docker
If running inside a Docker container, use:
```bash
docker-compose run django-web python manage.py test
```

## 🚀 Feel Free to Play Around!
This project is built to be a fun and practical way to explore Django and its API capabilities. Feel free to clone the repository, experiment with the code, and modify it however you like!