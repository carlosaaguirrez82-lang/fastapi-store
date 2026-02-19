from google.oauth2 import id_token
from google.auth.transport import requests

from src.core.settings import settings
from src.core.security.security import create_access_token
from src.domain.repositories.user_repository import UserRepository
from src.domain.exceptions.user_exceptions import InvalidGoogleTokenError


class LoginWithGoogle:

    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, token: str):

        # =========================
        # 1️⃣ Verificar token con Google
        # =========================
        try:
            idinfo = id_token.verify_oauth2_token(
                token,
                requests.Request(),
                settings.GOOGLE_CLIENT_ID
            )
        except Exception:
            raise InvalidGoogleTokenError("Invalid Google token")

        email = idinfo.get("email")
        google_id = idinfo.get("sub")

        if not email or not google_id:
            raise InvalidGoogleTokenError("Invalid Google payload")

        # =========================
        # 2️⃣ Buscar usuario por google_id
        # =========================
        user = self.user_repository.get_by_google_id(google_id)

        if not user:

            # =========================
            # 3️⃣ Buscar por email (posible cuenta local)
            # =========================
            user = self.user_repository.get_by_email(email)

            if user:
                # Vincular cuenta existente
                user.google_id = google_id
                user.provider = "google"
                user = self.user_repository.update(user)
            else:
                # Crear nuevo usuario Google
                user = self.user_repository.create_google_user(
                    email=email,
                    google_id=google_id
                )

        # =========================
        # 4️⃣ Generar JWT propio
        # =========================
        access_token = create_access_token(
            data={
                "sub": str(user.id),
                "email": user.email
            }
        )

        return {
            "access_token": access_token,
            "token_type": "bearer"
        }