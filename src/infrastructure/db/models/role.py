from datetime import datetime
from sqlalchemy import String, DateTime, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.infrastructure.db.base import Base


class Role(Base):
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False
    )

    description: Mapped[str] = mapped_column(
        String(255),
        nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )

    created_by: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=True
    )

    users = relationship(
        "UserRole",
        back_populates="role"
    )