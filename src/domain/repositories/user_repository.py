from abc import ABC, abstractmethod
from src.infrastructure.db.models.user import User


class UserRepository(ABC):

    @abstractmethod
    def get_by_email(self, email: str) -> User | None:
        pass

    @abstractmethod
    def create(self, user: User) -> User:
        pass
    
    @abstractmethod
    def assign_role(self, user_id: int, role_id: int) -> None:
        pass