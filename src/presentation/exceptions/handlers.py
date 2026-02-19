from fastapi import Request
from fastapi.responses import JSONResponse

from src.domain.exceptions.base import DomainError
from src.domain.exceptions.user_exceptions import (
    EmailAlreadyExistsError,
    InvalidCredentialsError,
    InvalidGoogleTokenError,
)


# =========================
# 🔹 Handler general dominio
# =========================
async def domain_error_handler(request: Request, exc: DomainError):
    return JSONResponse(
        status_code=400,
        content={
            "error": exc.__class__.__name__,
            "message": str(exc),
        },
    )


# =========================
# 🔹 Email ya existe
# =========================
async def email_already_exists_handler(
    request: Request, exc: EmailAlreadyExistsError
):
    return JSONResponse(
        status_code=400,
        content={
            "error": "EMAIL_ALREADY_EXISTS",
            "message": str(exc),
        },
    )


# =========================
# 🔹 Credenciales inválidas
# =========================
async def invalid_credentials_handler(
    request: Request, exc: InvalidCredentialsError
):
    return JSONResponse(
        status_code=401,
        content={
            "error": "INVALID_CREDENTIALS",
            "message": "Invalid email or password",
        },
    )


# =========================
# 🔹 Google token inválido
# =========================
async def invalid_google_token_handler(
    request: Request, exc: InvalidGoogleTokenError
):
    return JSONResponse(
        status_code=401,
        content={
            "error": "INVALID_GOOGLE_TOKEN",
            "message": "Invalid Google authentication token",
        },
    )