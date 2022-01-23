from adapters.database.product import ProductDb
from app.services.product import ProductService

service = ProductService(persistence=ProductDb())



new_product = service.create(name="Product1", price=1.2)
product = service.get_by_name(name="Product1")

print(product)
