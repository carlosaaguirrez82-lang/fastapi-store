from datetime import datetime
from typing import List, TYPE_CHECKING
from sqlalchemy import ForeignKey, Integer, Boolean, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from infrastructure.db.base import Base

if TYPE_CHECKING:
    from .user import User
    from .product import Product

class CartItem(Base):
    __tablename__ = "tr_cart_item"

    id: Mapped[int] = mapped_column(primary_key=True)
    quantity: Mapped[int] = mapped_column(Integer, default=1, nullable=False)
    is_selected: Mapped[bool] = mapped_column(Boolean, default=True)
    id_cart: Mapped[int] = mapped_column(ForeignKey("tr_cart.id"), nullable=False)
    id_product: Mapped[int] = mapped_column(ForeignKey("tr_product.id"), nullable=False)
    cart: Mapped["Cart"] = relationship("Cart", back_populates="items")
    product: Mapped["Product"] = relationship("Product")

class Cart(Base):
    __tablename__ = "tr_cart"

    id: Mapped[int] = mapped_column(primary_key=True)
    id_user: Mapped[int] = mapped_column(ForeignKey("tr_user.id"), unique=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    user: Mapped["User"] = relationship("User", back_populates="cart")
    
    items: Mapped[List["CartItem"]] = relationship(
        "CartItem", 
        back_populates="cart",
        cascade="all, delete-orphan"
    )