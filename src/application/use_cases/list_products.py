from src.domain.repositories.product_repository import ProductRepository


class ListProductsUseCase:

    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def execute(self):
        return self.repository.list()