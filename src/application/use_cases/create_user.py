import bcrypt
from src.domain.repositories.user_repository import UserRepository
from src.infrastructure.db.models.user import User


class CreateUserUseCase:

    def __init__(self, repository: UserRepository):
        self.repository = repository

    def execute(self, email: str, password: str) -> User:
        if self.repository.get_by_email(email):
            raise ValueError("Email already exists")

        password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

        user = User(
            email=email,
            password=password_hash,
            is_active=True
        )

        return self.repository.create(user)