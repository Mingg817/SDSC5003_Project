from fastapi import APIRouter
from fastapi.security import OAuth2PasswordRequestForm


from api.routes import students, courses, scores, classes,users

from fastapi import Depends, HTTPException
from datetime import timedelta


from core.config import settings
from core.db import SessionLocal, get_db
from models.models import User

import api.authenticate as auth


router = APIRouter(
    prefix="/api",
    # tags=["api"],
    responses={
        200: {},
        401: {"description": "Unauthorized"},
        422: {"description": "Validation Error"},
    },
)
router.include_router(students.router)
router.include_router(courses.router)
router.include_router(scores.router)
router.include_router(classes.router)
router.include_router(auth.router)
router.include_router(users.router)

