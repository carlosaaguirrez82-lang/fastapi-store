from typing import List, TYPE_CHECKING
from sqlalchemy import String, Float, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from infrastructure.db.base import Base
from .category import product_category_association

if TYPE_CHECKING:
    from .category import Category

class Product(Base):
    __tablename__ = "tr_product"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    stock: Mapped[int] = mapped_column(nullable=False)
    image: Mapped[str] = mapped_column(String(500), nullable=True)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    categories: Mapped[List["Category"]] = relationship(
        "Category",
        secondary=product_category_association,
        back_populates="products"
    )