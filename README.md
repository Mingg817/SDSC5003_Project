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
