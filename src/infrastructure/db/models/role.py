from sqlalchemy import String, desc
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.infrastructure.db.base import Base

class Role(Base):
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=True)
    created_ad: Mapped[str] = mapped_column(nullable=False)    

    users = relationship(
        "UserRole",
        back_populates="role"
    )