from sqlalchemy import String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING, List, Optional

from infrastructure.db.base import Base

if TYPE_CHECKING:
    from .role import Role



class RoleMenu(Base):
    __tablename__ = "tr_role_menu"

    id: Mapped[int] = mapped_column(primary_key=True)
    id_menu: Mapped[int] = mapped_column(ForeignKey("tc_menu.id"), nullable=False)
    id_role: Mapped[int] = mapped_column(ForeignKey("tc_role.id"), nullable=False)

class Menu(Base):
    __tablename__ = "tc_menu"

    id: Mapped[int] = mapped_column(primary_key=True)
    label: Mapped[str] = mapped_column(String(30), unique=True, nullable=False)
    path: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    icon: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    id_parent: Mapped[Optional[int]] = mapped_column(ForeignKey("tc_menu.id"), nullable=True)
    order_index: Mapped[int] = mapped_column(Integer, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    roles: Mapped[List["Role"]] = relationship(
        "Role",
        secondary="tr_role_menu",
        back_populates="menus"
    )

    submenus: Mapped[List["Menu"]] = relationship(
        "Menu",
        back_populates="parent",
        cascade="all, delete-orphan"
    )

    parent: Mapped[Optional["Menu"]] = relationship(
        "Menu",
        back_populates="submenus",
        remote_side=[id]
    )