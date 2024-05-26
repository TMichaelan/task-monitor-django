# task-monitor-django

This is a Django project that provides a REST API for monitoring tasks from csv file.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Running Tests](#running-tests)
- [Linting](#linting)

## Installation

### Requirements
* Docker
* docker-compose

### Clone the repository
```sh
git clone https://github.com/TMichaelan/task-monitor-django.git
cd task-monitor-django
```

### Run docker-compose
```sh
docker-compose up --build
```

### Apply Migrations
```sh
docker-compose exec app ./manage.py migrate
```

### Create Superuser
```sh
docker-compose exec app ./manage.py createsuperuser
```

#### Example input (we will use these credentials for Authorization):
```sh
Username: admin
Email address:
Password: admin
Password (again): admin
Superuser created successfully.
```

## Usage

### OpenAPI Documentation

When in DEBUG mode, you can access the API documentation via Swagger and Redoc.

Open your browser and navigate to `http://localhost:8000/api/admin` to login to the admin panel, then navigate to `http://localhost:8000/schema/swagger/` to view the API documentation.



Swagger UI: http://localhost:8000/schema/swagger/

Redoc: http://localhost:8000/schema/redoc/

### Endpoints

#### Example usage via browser

Login to the admin panel: http://localhost:8000/api/admin

```sh
http://localhost:8000/api/checker/task/<task-id>/
```

#### Obtain JWT Token

```sh
curl -X 'POST' \
  'http://localhost:8000/api/token/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'username=admin&password=admin'
```

####  Refresh JWT Token

```sh
curl -X POST 'http://localhost:8000/api/token/refresh/' -d '{
  "refresh": "your-refresh-token"
}'
```

#### Get Task by ID
```sh
curl -H "Authorization: Bearer <your-access-token>" 'http://localhost:8000/api/checker/task/<task-id>/'
```
##### Example usage via CLI
```sh
curl -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE2NzUzMzYyLCJpYXQiOjE3MTY3NDYxNjIsImp0aSI6IjEyZDRhYjkwNmYzMjRhYTM4YjFiOWZjNDc1OGVkYjJkIiwidXNlcl9pZCI6MX0.bbIn8zX4hoTWDW1v6dPwn9IhFaK2-i1cgnvr6q6CQ9k" 'http://localhost:8000/api/checker/task/123/'
```
#### Response example
```json
{
  "id":123,
  "status":"open",
  "answerTime":1440,
  "dateCreated":"2024-05-22T08:30:16",
  "dueDate":"2024-05-23T08:30:16"
}
```

## Running Tests

```sh
docker-compose exec app pytest
```

## Linting

```sh
docker-compose exec app black .
```
```sh
docker-compose exec app pylint **/*.py
```

## Project Structure
```
task-monitor-api/
├── checker/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── task_monitor/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── docker-compose.yml
└── Dockerfile
```