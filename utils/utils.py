from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session


def commit_constraint_helper(db: Session):
    try:
        db.commit()
    except IntegrityError as e:
        db.rollback()
        rai = HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Please check integrity constraints!",
        )
        try:
            if "Duplicate entry" in e.orig.args[1]:
                rai = HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST, detail=f"{e.orig.args[1]}"
                )

            elif "FOREIGN KEY" in e.orig.args[1]:
                detail = e.orig.args[1].split("FOREIGN KEY (`")[-1].split("`)")[0]
                rai = HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST, detail=f"Invalid {detail}!"
                )
        finally:
            raise rai
    return
