from src.domain.repositories.user_repository import UserRepository
from src.infrastructure.db.models.user import User
from src.core.security import hash_password


class CreateUserUseCase:

    def __init__(self, repository: UserRepository):
        self.repository = repository

    def execute(self, email: str, password: str,id_role:int) -> User:
        if self.repository.get_by_email(email):
            raise ValueError("Email already exists")

        password_hash = hash_password(password)

        user = User(
            email=email,
            password=password_hash,           
            is_active=True
        )
        saved_user = self.repository.create(user)
        self.repository.assign_role(saved_user.id, id_role)

        return saved_user