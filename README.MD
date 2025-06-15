# Advance Containers Assignment

This project is a containerized web application built using Python (Flask) and PostgreSQL. It allows users to create and fetch basic user data using simple API endpoints.

## Features

- Simple REST API with Flask
- User data stored in PostgreSQL
- Uses Docker and Docker Compose for containerization
- Persistent database using Docker volumes
- Secure and minimal Docker images
- Custom Docker network for container communication

## Project Structure

```
.
├── app/
│   ├── app.py             # Main Flask application
│   └── requirements.txt   # Python dependencies
├── init.sql               # DB init script to create user table
├── Dockerfile             # Dockerfile for Flask app
├── docker-compose.yml     # Compose file to run everything
└── README.md              # This file
```

## How to Run

### Prerequisites

- Docker Desktop must be installed and running
- Docker Compose support enabled (built-in with Docker Desktop)

### Steps

1. **Clone or download this project folder**

2. **Open terminal inside the folder**  
   (You can shift+right click in the folder → "Open PowerShell window here")

3. **Start the containers**
   ```bash
   docker compose up --build -d
   ```

4. **Check if everything is running**
   ```bash
   docker compose ps
   ```

5. **Test the API**
   - Create a user:
     ```bash
     curl -X POST -H "Content-Type: application/json" ^
     -d "{\"first_name\":\"Jane\",\"last_name\":\"Doe\"}" ^
     http://localhost:8000/user
     ```

   - Get the user by ID:
     ```bash
     curl http://localhost:8000/user/1
     ```

## API Endpoints

- `POST /user` – Create a new user
  ```json
  {
    "first_name": "Jane",
    "last_name": "Doe"
  }
  ```

- `GET /user/<id>` – Get a user by ID

## Volumes and Networking

- PostgreSQL data is saved using a Docker volume named `pgdata`
- A custom Docker network is used so the app and DB can talk securely


## Stopping Everything

To stop and remove containers:

```bash
docker compose down
```


## Author

Suman Kumari Jakhar  
(Advance Containers Assignment)