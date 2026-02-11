from fastapi import FastAPI
from src.presentation.routes.router import router

# Handlers
from src.presentation.exceptions.handlers import (
    domain_exception_handler,
)

# Domain base exception
from src.domain.exceptions.base import DomainError


app = FastAPI(title="Store API")

app.include_router(router)

# Registrar handler global para errores de dominio
app.add_exception_handler(DomainError, domain_exception_handler)