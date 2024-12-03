from fastapi import FastAPI

import api.main

app = FastAPI(version="0.1", title="SDSC5003 project")

app.include_router(api.main.router)
