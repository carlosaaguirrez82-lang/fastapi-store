from src.domain.repositories.user_repository import UserRepository
from src.infrastructure.db.models.user import User
from src.domain.exceptions.user_exceptions import EmailAlreadyExistsError
from src.core.security.security import hash_password


class CreateUserUseCase:

    def __init__(self, repository: UserRepository):
        self.repository = repository

    def execute(self, email: str, password: str,id_role:int) -> User:
        if self.repository.get_by_email(email):
            raise EmailAlreadyExistsError("Email already exists")

        password_hash = hash_password(password)

        user = User(
            email=email,
            password=password_hash,           
            is_active=True
        )
        saved_user = self.repository.create(user)
        self.repository.assign_role(saved_user.id, id_role)
        #todo enviar informacion de usuario creado a un servicio de email para enviar un correo de bienvenida

        return saved_user