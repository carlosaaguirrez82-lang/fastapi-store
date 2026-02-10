from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.infrastructure.db.session import get_db
from src.application.use_cases.create_product import CreateProductUseCase
from src.application.use_cases.list_products import ListProductsUseCase
from src.infrastructure.db.repositories.product_repository_impl import ProductRepositoryImpl

router = APIRouter(prefix="/products", tags=["Products"])

@router.get("")
def list_products(db: Session = Depends(get_db)):
    return ListProductsUseCase(ProductRepositoryImpl(db)).execute()


@router.post("")
def create_product(title: str, price: float, stock: int, category_id: int, db: Session = Depends(get_db)):
    return CreateProductUseCase(ProductRepositoryImpl(db)).execute(
        title, price, stock, category_id
    )


