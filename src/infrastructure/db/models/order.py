from typing import List, TYPE_CHECKING
from sqlalchemy import ForeignKey, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship
from infrastructure.db.base import Base

if TYPE_CHECKING:
    from .user import User
    from .address import Address
    from .product import Product

class OrderItem(Base):
    __tablename__ = "tr_order_product"

    id: Mapped[int] = mapped_column(primary_key=True)
    quantity: Mapped[int] = mapped_column(nullable=False)
    price: Mapped[float] = mapped_column(Float, nullable=False)

    id_order: Mapped[int] = mapped_column(ForeignKey("tr_order.id"), nullable=False)
    id_product: Mapped[int] = mapped_column(ForeignKey("tr_product.id"), nullable=False)

    order: Mapped["Order"] = relationship("Order", back_populates="items")
    product: Mapped["Product"] = relationship("Product")

class Order(Base):
    __tablename__ = "tr_order"

    id: Mapped[int] = mapped_column(primary_key=True)
    total: Mapped[float] = mapped_column(Float, default=0)

    id_user: Mapped[int] = mapped_column(
        ForeignKey("tr_user.id"),
        nullable=False
    )

    id_address: Mapped[int] = mapped_column(
        ForeignKey("tr_address.id"),
        nullable=False
    )

    user: Mapped["User"] = relationship(
        "User",
        back_populates="orders"
    )

    address: Mapped["Address"] = relationship(
        "Address",
        back_populates="orders"
    )

    items: Mapped[List["OrderItem"]] = relationship(
        "OrderItem",
        back_populates="order",
        cascade="all, delete-orphan"
    )