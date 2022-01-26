from routes.v1.product import v1_product
from fastapi import APIRouter

router = APIRouter()

router.include_router(v1_product, prefix="/v1")