from fastapi import APIRouter
from .users import router as users_router
from .products import router as products_router
from .auth import router as auth_router

router = APIRouter()
router.include_router(auth_router)
router.include_router(users_router)
router.include_router(products_router)
