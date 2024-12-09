from fastapi import APIRouter, HTTPException, status
from fastapi.params import Depends
from sqlalchemy.orm import Session

from core.db import get_db
from models.models import Student, Score
from api.authenticate import get_current_user

router = APIRouter(
    prefix="/students", tags=["student"], dependencies=[Depends(get_current_user)]
)


@router.post(
    "/",
    summary="Insert a new student.",
    response_model=Student,
    responses={
        200: {"description": "A successful response."},
        403: {"description": "Student already exists"},
        404: {"description": "Student not found"},
    },
)
def create_student(student: Student, db: Session = Depends(get_db)):
    # cheak if the student already exists
    check = db.query(Student).filter(Student.student_id == student.student_id).first()
    if check:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Student already exists"
        )
    db.add(student)
    db.commit()
    db.refresh(student)
    return student


@router.get(
    "/",
    summary="Get all students. Can be paginated.",
    response_model=list[Student],
    responses={
        200: {
            "description": "A successful response.",
            "content": {
                "application/json": {
                    "example": [
                        {
                            "name": "John Doe",
                            "student_id": "S001",
                            "gender": "M",
                            "birth_date": "2005-02-14",
                            "class_id": "C001",
                        },
                        {
                            "name": "Jane Smith",
                            "student_id": "S002",
                            "gender": "F",
                            "birth_date": "2006-08-22",
                            "class_id": "C002",
                        },
                        {
                            "name": "Chris Taylor",
                            "student_id": "S003",
                            "gender": "M",
                            "birth_date": "2007-03-21",
                            "class_id": "C003",
                        },
                    ]
                }
            },
        },
        404: {"description": "Student not found"},
    },
)
def read_students(
    name: str = None,
    gender: str = None,
    class_id: str = None,
    page: int | None = 1,
    per_page: int | None = 10,
    db: Session = Depends(get_db),
):
    query = db.query(Student)

    # Apply optional filters
    if name:
        query = query.filter(Student.name.ilike(f"%{name}%"))
    if gender:
        query = query.filter(Student.gender == gender)
    if class_id:
        query = query.filter(Student.class_id == class_id)

    # Pagination

    students = query.offset((page - 1) * per_page).limit(per_page).all()

    if not students:
        raise HTTPException(status_code=404, detail="Students not found")

    return students


@router.get(
    "/{student_id}",
    summary="Get a student by student_id.",
    response_model=Student,
    responses={
        200: {"description": "A successful response."},
        404: {"description": "Student not found"},
    },
)
def read_student(student_id: str, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.student_id == student_id).first()
    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Student not found"
        )
    return student


@router.delete(
    "/{student_id}",
    summary="Delete a student by student_id.",
    status_code=204,
    response_model=None,
    responses={
        200: {},
        204: {"description": "Student deleted."},
        404: {"description": "Student not found."},
    },
)
def delete_student(student_id: str, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.student_id == student_id).first()
    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Student not found"
        )
    db.delete(student)
    db.commit()
    return


@router.put(
    "/",
    summary="Update a student's information by student_id.",
    response_model=Student,
    responses={
        200: {"description": "Student information updated successfully."},
        404: {"description": "Student not found."},
        400: {"description": "Invalid input."},
    },
)
def update_student(updated_student: Student, db: Session = Depends(get_db)):
    if not updated_student.student_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid input."
        )
    # 查找学生记录
    student = (
        db.query(Student)
        .filter(Student.student_id == updated_student.student_id)
        .first()
    )
    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Student not found"
        )

    # 更新学生信息
    student.name = updated_student.name
    student.gender = updated_student.gender
    student.birth_date = updated_student.birth_date
    student.class_id = updated_student.class_id

    db.commit()
    db.refresh(student)
    return student


# @router.get(
#     "/{student_id}/scores",
#     summary="Insert a new score for a student.",
#     responses={
#         404: {"description": "Student not found."}
#     },
# ):
