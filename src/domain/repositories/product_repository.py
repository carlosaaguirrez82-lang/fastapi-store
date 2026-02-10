from abc import ABC, abstractmethod
from src.infrastructure.db.models.product import Product


class ProductRepository(ABC):

    @abstractmethod
    def create(self, product: Product) -> Product:
        pass

    @abstractmethod
    def list(self) -> list[Product]:
        pass