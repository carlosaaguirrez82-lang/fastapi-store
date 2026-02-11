from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.infrastructure.db.session import get_db
from src.application.use_cases.create_user import CreateUserUseCase
from src.infrastructure.db.repositories.user_repository_impl import UserRepositoryImpl
from src.presentation.schemas.user_schema import (
    UserCreateRequest,
    UserResponse
)

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("",response_model=UserResponse)
def create_user(
    request: UserCreateRequest,
    db: Session = Depends(get_db)):
    use_case = CreateUserUseCase(UserRepositoryImpl(db))
    return use_case.execute(
        request.email,
        request.password,
        request.id_role
    )