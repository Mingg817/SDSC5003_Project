from fastapi import FastAPI

import api.main

description = """
- SDSC5003 Backend API

- Implemented by FastAPI.

- Group : `LWYLOY`

- Author: [Yiming Li](https://eming.ing/)

- Project github: [SDSC5003 project](https://github.com/Mingg817/SDSC5003_Project)

- Finished Date: 2024-12-10

Default user and password: `admin` `admin`
"""

app = FastAPI(
    version="1.0",
    title="SDSC5003 project",
    description=description,
    contact={
        "name": "Yiming Li",
        "email": "yli2467-c@my.cityu.edu.hk",
    },
)

app.include_router(api.main.router)
