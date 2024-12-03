from fastapi import APIRouter, HTTPException, Query, status
from fastapi.params import Depends
from sqlalchemy.orm import Session
from utils.utils import commit_constraint_helper

from core.db import get_db
from models.models import Class, Student
from api.authenticate import get_current_user

router = APIRouter(
    prefix="/classes", tags=["classes"], dependencies=[Depends(get_current_user)]
)


@router.post(
    "/",
    summary="Insert a new class.",
    response_model=Class,
    responses={
        200: {"description": "A successful response."},
        400: {"description": "Invalid input."},
        403: {"description": "Class already exists"},
    },
)
def create_class(class_: Class, db: Session = Depends(get_db)):
    existing_class = db.query(Class).filter(Class.class_id == class_.class_id).first()
    if existing_class:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Class already exists"
        )
    db.add(class_)
    commit_constraint_helper(db)
    db.refresh(class_)
    return class_


@router.get(
    "/",
    summary="Get all classes.",
    response_model=list[Class],
    responses={
        200: {"description": "A successful response."},
        404: {"description": "Classes not found"},
    },
)
def read_classes(
    class_id: str | None = None,
    class_name: str | None = None,
    head_teacher: str | None = None,
    page: int | None = 1,
    per_page: int | None = 10,
    db: Session = Depends(get_db),
):
    query = db.query(Class)
    if class_id:
        query = query.filter(Class.class_id == class_id)
    if class_name:
        query = query.filter(Class.class_name.like(f"%{class_name}%"))
    if head_teacher:
        query = query.filter(Class.head_teacher.like(f"%{head_teacher}%"))

    classes = query.offset((page - 1) * per_page).limit(per_page).all()
    if not classes:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Classes not found"
        )

    return classes


@router.get(
    "/{class_id}/students",
    summary="Get all students in a class.",
    response_model=list[Student],
    responses={
        200: {"description": "A successful response."},
        404: {"description": "Classes not found"},
    },
)
def read_students_in_class(
    class_id: str,
    db: Session = Depends(get_db),
):
    students = db.query(Student).filter(Student.class_id == class_id).all()

    return students
