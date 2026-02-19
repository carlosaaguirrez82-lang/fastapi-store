from sqlalchemy.orm import Session, joinedload
from src.infrastructure.db.models.user import User
from src.infrastructure.db.models.user_role import UserRole
from src.domain.repositories.user_repository import UserRepository
import logging

logger = logging.getLogger(__name__)


class UserRepositoryImpl(UserRepository):

    def __init__(self, db: Session):
        self.db = db

    # =========================
    # 🔎 GET BY EMAIL
    # =========================
    def get_by_email(self, email: str) -> User | None:
        return (
            self.db.query(User)
            .options(
                joinedload(User.roles).joinedload(UserRole.role)
            )
            .filter(User.email == email)
            .first()
        )

    # =========================
    # 🔎 GET BY GOOGLE ID
    # =========================
    def get_by_google_id(self, google_id: str) -> User | None:
        return (
            self.db.query(User)
            .options(
                joinedload(User.roles).joinedload(UserRole.role)
            )
            .filter(User.google_id == google_id)
            .first()
        )

    # =========================
    # ➕ CREATE USER (LOCAL)
    # =========================
    def create(self, user: User) -> User:
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    # =========================
    # ➕ CREATE GOOGLE USER
    # =========================
    def create_google_user(self, email: str, google_id: str) -> User:
        user = User(
            email=email,
            google_id=google_id,
            provider="google",
            password=None,
            is_active=True
        )

        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)

        return user

    # =========================
    # 🔄 UPDATE USER
    # =========================
    def update(self, user: User) -> User:
        self.db.commit()
        self.db.refresh(user)
        return user

    # =========================
    # 👤 ASSIGN ROLE
    # =========================
    def assign_role(self, user_id: int, role_id: int) -> None:
        user_role = UserRole(user_id=user_id, role_id=role_id)
        self.db.add(user_role)
        self.db.commit()