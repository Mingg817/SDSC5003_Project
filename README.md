# SDSC5003 Project

## Compilation and Deployment Documentation

Prerequisites

- Operating System: Linux (recommended), or any OS that supports Docker
- Software: Docker and Docker Compose

Steps

1. Clone the Project Repository

```sh
git clone https://github.com/Mingg817/SDSC5003_Project.git
```

2. Enter the Project Folder

```sh
cd SDSC5003_Project
```

3. Start Docker Compose

```sh
docker compose up
```

4. Access Swagger UI Open your browser and go to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

    The default mysql port is `3306`, refer to `docker-compose.yml`


## Swagger Help

### Accessing Swagger UI

Open Swagger UI Open your browser and go to http://127.0.0.1:8000/docs.

### Default Account

- Username: admin
- Password: admin

### Using API Endpoints

1. Authorize Requests

- Click on the "Authorize" button at the top right of Swagger UI.
- Enter Username and Password
- Click on the "Authorize" button and then "Close".

2. Testing Endpoints

- Select an endpoint you want to test.
- Click on the "Try it out" button.
Fill in the required parameters.
- Click on the "Execute" button to send the request and view the response.
