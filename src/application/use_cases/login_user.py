from src.domain.repositories.user_repository import UserRepository
from src.core.security.security import verify_password, create_access_token
import logging

logger = logging.getLogger(__name__)

class LoginUser:

    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, email: str, password: str):

        user = self.user_repository.get_by_email(email)

        if not user:
            logger.warning(f"Login failed: user not found ({email})")
            raise Exception("Invalid credentials")

        if not verify_password(password, user.password):
            logger.warning(f"Login failed: invalid password ({email})")
            raise Exception("Invalid credentials")

        # 🔹 Extraer nombres de roles
        role_names = user.roles[0].role.name

        logger.info(f"Login successful: {email}")

        token = create_access_token(
            {
                "sub": str(user.id),
                "email": user.email,
                "roles": role_names,  # 👈 ahora sí
            }
        )

        return token