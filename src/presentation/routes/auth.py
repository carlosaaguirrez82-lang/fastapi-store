from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.presentation.schemas.auth_schema import LoginRequest
from src.infrastructure.db.session import get_db
from src.application.use_cases.login_user import LoginUser
from src.infrastructure.db.repositories.user_repository_impl import UserRepositoryImpl

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/login")
def login(data: LoginRequest, db: Session = Depends(get_db)):

    repo = UserRepositoryImpl(db)
    use_case = LoginUser(repo)

    token = use_case.execute(
        email=data.email,
        password=data.password
    )
    
    
    return {"access_token": token}
    