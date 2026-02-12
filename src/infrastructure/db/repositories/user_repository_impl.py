from sqlalchemy.orm import Session,joinedload
from sqlalchemy import select
from src.infrastructure.db.models.user import User
from src.infrastructure.db.models.user_role import UserRole
from src.infrastructure.db.models.role import Role
from src.domain.repositories.user_repository import UserRepository
import logging

logger = logging.getLogger(__name__)

class UserRepositoryImpl(UserRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_by_email(self, email: str) -> User | None:
        return (
        self.db.query(User)
        .options(
            joinedload(User.roles).joinedload(UserRole.role)
        )
        .filter(User.email == email)
        .first()
    )

    def create(self, user: User):
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
    
    def assign_role(self, user_id: int, role_id: int) -> None:
        user_role = UserRole(user_id=user_id, role_id=role_id)
        self.db.add(user_role)
        self.db.commit()