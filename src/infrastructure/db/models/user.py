from datetime import datetime
from typing import List, TYPE_CHECKING
from sqlalchemy import String, Boolean, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func
from infrastructure.db.base import Base

if TYPE_CHECKING:
    from .role import Role
    from .address import Address
    from .order import Order
    from .cart import Cart

class User(Base):
    __tablename__ = "tr_user"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=True)
    google_id: Mapped[str] = mapped_column(String(255), unique=True, nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    roles: Mapped[List["Role"]] = relationship(
        "Role",
        secondary="tr_user_role",
        back_populates="users"
    )

    addresses: Mapped[List["Address"]] = relationship(
        "Address",
        back_populates="user",
    )

    orders: Mapped[List["Order"]] = relationship(
        "Order",
        back_populates="user"
    )

    cart: Mapped["Cart"] = relationship(
        "Cart", 
        uselist=False, 
        back_populates="user"
    )