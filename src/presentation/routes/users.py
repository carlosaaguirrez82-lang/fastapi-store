from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.infrastructure.db.session import get_db
from src.application.use_cases.create_user import CreateUserUseCase
from src.infrastructure.db.repositories.user_repository_impl import UserRepositoryImpl

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("")
def create_user(email: str, password: str,id_role:int ,db: Session = Depends(get_db)):
    use_case = CreateUserUseCase(UserRepositoryImpl(db))
    return use_case.execute(email, password,id_role)