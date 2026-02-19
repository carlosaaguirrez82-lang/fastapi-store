from abc import ABC, abstractmethod
from src.infrastructure.db.models.user import User


class UserRepository(ABC):

    @abstractmethod
    def get_by_email(self, email: str) -> User | None:
        pass

    @abstractmethod
    def get_by_google_id(self, google_id: str) -> User | None:
        pass

    @abstractmethod
    def create(self, user: User) -> User:
        pass

    @abstractmethod
    def create_google_user(self, email: str, google_id: str) -> User:
        pass

    @abstractmethod
    def update(self, user: User) -> User:
        pass

    @abstractmethod
    def assign_role(self, user_id: int, role_id: int) -> None:
        pass