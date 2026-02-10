from sqlalchemy.orm import Session
from src.domain.repositories.user_repository import UserRepository
from src.infrastructure.db.models.user import User


class UserRepositoryImpl(UserRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_by_email(self, email: str):
        return self.db.query(User).filter(User.email == email).first()

    def create(self, user: User):
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user