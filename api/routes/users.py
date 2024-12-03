from fastapi import APIRouter, HTTPException, status
from fastapi.params import Depends
from sqlalchemy.orm import Session

from core.db import get_db
from models.models import User
from api.authenticate import get_current_user, get_password_hash

from enum import Enum

from utils.utils import commit_constraint_helper

router = APIRouter(
    prefix="/users", tags=["authenticate"], dependencies=[Depends(get_current_user)]
)


class Role(str, Enum):
    Teacher = "Teacher"
    Student = "Student"


@router.post(
    "/",
    summary="Insert a new user.",
    response_model=None,
    responses={
        200: {
            "description": "A successful response.",
            "content": {"application/json": {"example": {"result": "success"}}},
        },
        403: {"description": "User already exists"},
        404: {"description": "User not found"},
    },
)
def create_user(
    username: str,
    role: Role,
    password: str,
    role_id: str | None = None,
    db: Session = Depends(get_db),
):
    # cheak if the user already exists
    user = db.query(User).filter(User.username == username).first()
    if user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="User already exists"
        )
    if role == Role.Teacher:
        user = User(
            username=username,
            role=role,
            teacher_id=role_id,
            password=get_password_hash(password),
        )
    else:
        user = User(
            username=username,
            role=role,
            student_id=role_id,
            password=get_password_hash(password),
        )
    db.add(user)
    commit_constraint_helper(db)
    db.refresh(user)
    return {"result": "success"}
