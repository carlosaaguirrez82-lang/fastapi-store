from fastapi import Request
from fastapi.responses import JSONResponse
from src.domain.exceptions.base import DomainError
from src.domain.exceptions.user_exceptions import EmailAlreadyExistsError,InvalidCredentialsError


async def domain_exception_handler(request: Request, exc: DomainError):
    return JSONResponse(
        status_code=400,
        content={
            "error": exc.__class__.__name__,
            "message": str(exc)
        },
    )


async def email_already_exists_handler(request: Request, exc: EmailAlreadyExistsError):
    return JSONResponse(
        status_code=400,
        content={
            "error": "EMAIL_ALREADY_EXISTS",
            "message": str(exc)
        },
    )
    
async def invalid_credentials_handler(request: Request, exc: InvalidCredentialsError):
    return JSONResponse(
        status_code=401,  # 👈 importante, no 400
        content={
            "error": "INVALID_CREDENTIALS",
            "message": "Invalid email or password"
        },
    )