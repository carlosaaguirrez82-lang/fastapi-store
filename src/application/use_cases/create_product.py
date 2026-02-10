from src.domain.repositories.product_repository import ProductRepository
from src.infrastructure.db.models.product import Product


class CreateProductUseCase:

    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def execute(self, title: str, price: float, stock: int, category_id: int):
        product = Product(
            title=title,
            price=price,
            stock=stock,
            category_id=category_id
        )
        return self.repository.create(product)