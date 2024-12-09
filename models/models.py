from typing import List
from datetime import date
from sqlmodel import Field, SQLModel, Relationship

class Class(SQLModel, table=True):
    __tablename__ = "Classes"
    class_id: str = Field(primary_key=True, max_length=10)
    class_name: str
    head_teacher: str


    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "class_id": "C001",
                    "class_name": "Math Class",
                    "head_teacher": "Mr. Smith"
                }
            ]
        }
    }

class Teacher(SQLModel, table=True):
    __tablename__ = "Teachers"
    teacher_id: str = Field(primary_key=True, max_length=10)
    name: str
    gender: str = Field(max_length=1)
    birth_date: date
    title: str


    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "teacher_id": "T001",
                    "name": "John Doe",
                    "gender": "M",
                    "birth_date": "1980-01-01",
                    "title": "Professor"
                }
            ]
        }
    }

class Student(SQLModel, table=True):
    __tablename__ = "Students"
    student_id: str = Field(primary_key=True, max_length=10)
    name: str
    gender: str = Field(max_length=1)
    birth_date: date
    class_id: str = Field(foreign_key="Classes.class_id")



    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                "birth_date": "2000-01-01",
                "class_id": "C001",
                "gender": "M",
                "name": "Michael",
                "student_id": "S005"
                }
            ]
        }
    }

class Course(SQLModel, table=True):
    __tablename__ = "Courses"
    course_id: str = Field(primary_key=True, max_length=10)
    course_name: str
    credit: float
    course_type: str
    teacher_id: str = Field(foreign_key="Teachers.teacher_id")

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "course_id": "CS101",
                    "course_name": "Computer Science",
                    "credit": 3.0,
                    "course_type": "Core",
                    "teacher_id": "T001"
                }
            ]
        }
    }

class User(SQLModel, table=True):
    __tablename__ = "Users"
    username: str = Field(primary_key=True, max_length=50)
    password: str
    role: str
    student_id: str | None = Field(default=None, foreign_key="Students.student_id")
    teacher_id: str | None = Field(default=None, foreign_key="Teachers.teacher_id")


    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "username": "alice123",
                    "password": "hashedpassword",
                    "role": "student",
                    "student_id": "S001",
                    "teacher_id": None
                }
            ]
        }
    }

class Score(SQLModel, table=True):
    __tablename__ = "Scores"
    score_id: int | None = Field(default=None, primary_key=True)
    student_id: str = Field(foreign_key="Students.student_id")
    course_id: str = Field(foreign_key="Courses.course_id")
    score: float

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "score_id": 1,
                    "student_id": "S001",
                    "course_id": "C101",
                    "score": 95.0
                }
            ]
        }
    }