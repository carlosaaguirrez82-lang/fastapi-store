from src.domain.exceptions.base import DomainError


class EmailAlreadyExistsError(DomainError):
    """Raised when trying to create a user with an existing email"""
    pass

class InvalidCredentialsError(DomainError):
    """Raised when authentication credentials are invalid"""
    pass