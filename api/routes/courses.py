from fastapi import APIRouter, HTTPException, Query, status
from fastapi.params import Depends
from sqlalchemy.orm import Session
from utils.utils import commit_constraint_helper

from core.db import get_db
from models.models import Course
from api.authenticate import get_current_user

router = APIRouter(
    prefix="/courses", tags=["courses"], dependencies=[Depends(get_current_user)]
)


@router.post(
    "/",
    summary="Insert a new course.",
    response_model=Course,
    responses={
        200: {"description": "A successful response."},
        400: {"description": "Invalid input."},
        403: {"description": "Course already exists"},
    },
)
def create_course(course: Course, db: Session = Depends(get_db)):
    existing_course = (
        db.query(Course).filter(Course.course_id == course.course_id).first()
    )
    if existing_course:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Course already exists"
        )
    db.add(course)
    commit_constraint_helper(db)
    db.refresh(course)
    return course


@router.get(
    "/",
    summary="Get all courses.",
    response_model=list[Course],
    responses={
        200: {"description": "A successful response."},
    },
)
def read_courses(
    course_id: str | None = None,
    course_name: str | None = None,
    credit: float | None = Query(None, ge=0),
    course_type: str | None = None,
    page: int | None = 1,
    per_page: int | None = 10,
    db: Session = Depends(get_db),
):
    query = db.query(Course)
    if course_id:
        query = query.filter(Course.course_id == course_id)
    if course_name:
        query = query.filter(Course.course_name.like(f"%{course_name}%"))
    if credit:
        query = query.filter(Course.credit == credit)
    if course_type:
        query = query.filter(Course.course_type == course_type)

    courses = query.limit(per_page).offset((page - 1) * per_page).all()

    if not courses:
        raise HTTPException(status_code=404, detail="Courses not found")

    return courses


@router.get(
    "/{course_id}",
    summary="Get a course by course_id.",
    response_model=Course,
    responses={
        200: {"description": "A successful response."},
        404: {"description": "Course not found"},
    },
)
def read_course(course_id: str, db: Session = Depends(get_db)):
    course = db.query(Course).filter(Course.course_id == course_id).first()
    if not course:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Course not found"
        )
    return course


@router.delete(
    "/{course_id}",
    summary="Delete a course by course_id.",
    status_code=204,
    response_model=None,
    responses={
        204: {"description": "Course deleted."},
        400: {"description": "Bad request."},
        404: {"description": "Course not found."},
    },
)
def delete_course(course_id: str, db: Session = Depends(get_db)):
    course = db.query(Course).filter(Course.course_id == course_id).first()
    if not course:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Course not found"
        )
    db.delete(course)
    db.commit()
    return


@router.put(
    "/",
    summary="Update a course's information by course_id.",
    response_model=Course,
    responses={
        200: {"description": "Course information updated successfully."},
        400: {"description": "Invalid input."},
        404: {"description": "Course not found."},
    },
)
def update_course(updated_course: Course, db: Session = Depends(get_db)):
    if not updated_course.course_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid input."
        )
    course = (
        db.query(Course).filter(Course.course_id == updated_course.course_id).first()
    )
    if not course:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Course not found."
        )
    for key, value in updated_course.model_dump().items():
        setattr(course, key, value)

    commit_constraint_helper(db)
    return updated_course
