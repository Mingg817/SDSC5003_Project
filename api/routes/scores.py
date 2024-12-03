from fastapi import APIRouter, HTTPException, Query, status
from fastapi.params import Depends
from sqlalchemy.orm import Session
from utils.utils import commit_constraint_helper

from core.db import get_db
from models.models import Score
from api.authenticate import get_current_user

router = APIRouter(
    prefix="/scores", tags=["scores"], dependencies=[Depends(get_current_user)]
)


@router.post(
    "/",
    summary="Insert a new score.",
    response_model=Score,
    responses={
        200: {"description": "A successful response."},
        400: {"description": "Invalid input."},
        403: {"description": "Score already exists"},
    },
)
def create_score(score: Score, db: Session = Depends(get_db)):
    existing_score = (
        db.query(Score).filter(Score.student_id == score.student_id).first()
    )
    if existing_score:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Score already exists"
        )
    db.add(score)
    commit_constraint_helper(db)
    db.refresh(score)
    return score


@router.get(
    "/",
    summary="Get all scores.",
    response_model=list[Score],
    responses={
        200: {"description": "A successful response."},
        404: {"description": "Scores not found"},
    },
)
def read_scores(
    student_id: str | None = None,
    course_id: str | None = None,
    score: float | None = Query(
        None,
        ge=0,
        le=100,
        description="Filter by score which is greater than the input value",
    ),
    page: int | None = 1,
    per_page: int | None = 10,
    db: Session = Depends(get_db),
):
    query = db.query(Score)
    if student_id:
        query = query.filter(Score.student_id == student_id)
    if course_id:
        query = query.filter(Score.course_id == course_id)
    if score:
        query = query.filter(Score.score > score)
    scores = query.offset((page - 1) * per_page).limit(per_page).all()
    if not scores:
        raise HTTPException(status_code=404, detail="Scores not found")
    return scores
