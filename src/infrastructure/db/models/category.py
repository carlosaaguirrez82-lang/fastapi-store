from typing import List, TYPE_CHECKING
from sqlalchemy import String, Text, Table, Column, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from infrastructure.db.base import Base

if TYPE_CHECKING:
    from .product import Product

product_category_association = Table(
    "tr_product_category",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("id_product", ForeignKey("tr_product.id"), nullable=False),
    Column("id_category", ForeignKey("tc_category.id"), nullable=False),
)

class Category(Base):
    __tablename__ = "tc_category"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)

    products: Mapped[List["Product"]] = relationship(
        "Product",
        secondary=product_category_association,
        back_populates="categories"
    )