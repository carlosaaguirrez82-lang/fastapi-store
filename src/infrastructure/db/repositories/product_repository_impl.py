from sqlalchemy.orm import Session
from src.domain.repositories.product_repository import ProductRepository
from src.infrastructure.db.models.product import Product


class ProductRepositoryImpl(ProductRepository):

    def __init__(self, db: Session):
        self.db = db

    def create(self, product: Product):
        self.db.add(product)
        self.db.commit()
        self.db.refresh(product)
        return product

    def list(self):
        return self.db.query(Product).all()