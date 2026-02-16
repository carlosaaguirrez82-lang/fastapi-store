from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from src.infrastructure.db.session import get_db
from src.application.use_cases.login_user import LoginUser
from src.infrastructure.db.repositories.user_repository_impl import UserRepositoryImpl

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    repo = UserRepositoryImpl(db)
    use_case = LoginUser(repo)

    token = use_case.execute(
        email=form_data.username,   # 👈 OAuth2 usa username
        password=form_data.password
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }
    