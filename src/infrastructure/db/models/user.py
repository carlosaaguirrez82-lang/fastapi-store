from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional
from src.infrastructure.db.base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)

    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)

    # Password solo si es login tradicional
    password: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)

    # Nuevo: proveedor de autenticación
    provider: Mapped[str] = mapped_column(String(50), default="local")
    # valores: local | google

    # Nuevo: id único que Google envía
    google_id: Mapped[Optional[str]] = mapped_column(String(255), nullable=True, unique=True)

    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    roles = relationship(
        "UserRole",
        back_populates="user",
        cascade="all, delete-orphan"
    )

    orders = relationship(
        "Order",
        back_populates="user"
    )