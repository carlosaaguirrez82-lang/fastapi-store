from typing import List, TYPE_CHECKING
from datetime import datetime
from sqlalchemy import String, Text, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func
from infrastructure.db.base import Base

if TYPE_CHECKING:
    from .user import User
    from .menu import Menu

class UserRole(Base):
    __tablename__ = "tr_user_role"

    id: Mapped[int] = mapped_column(primary_key=True)
    
    id_user: Mapped[int] = mapped_column(ForeignKey("tr_user.id"), nullable=False)
    id_role: Mapped[int] = mapped_column(ForeignKey("tc_role.id"), nullable=False)


class Role(Base):
    __tablename__ = "tc_role"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    users: Mapped[List["User"]] = relationship(
        "User",
        secondary="tr_user_role", 
        back_populates="roles"
    )

    menus: Mapped[List["Menu"]] = relationship(
        "Menu",
        secondary="tr_role_menu", 
        back_populates="roles"
    )