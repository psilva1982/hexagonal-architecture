from fastapi import APIRouter, Response
from utils.response import ResponseModel, ErrorResponseModel

import sys
sys.path.append('../../../')

from adapters.database.product import ProductDb
from app.services.product import ProductService

v1_product = APIRouter(prefix='/products')

@v1_product.get('/', response_description='Product list retrieve')
async def list_products():
    service = ProductService(persistence=ProductDb())
    products = service.get_all()

    if products:
        return ResponseModel(products, {"Retrieved products list"})
    
    else:
        return ResponseModel([], {"Empty list"})

@v1_product.get('/', response_description='Product list retrieve')
async def list_products():
    service = ProductService(persistence=ProductDb())
    products = service.get_all()

    if products:
        return ResponseModel(products, {"Retrieved products list"})
    
    else:
        return ResponseModel([], {"Empty list"})

@v1_product.get("/{id}", response_description="Product data retrieved")
async def get_person_data(id: str):
    service = ProductService(persistence=ProductDb())
    product = service.get(id=id)

    if product:
        return ResponseModel(product, "Product data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Product doesn't exist.")