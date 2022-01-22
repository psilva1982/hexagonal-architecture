from adapters.database.product import ProductDb
from application.services.product import ProductService

service = ProductService(persistence=ProductDb())

users = service.get(id="1d183f97-6e48-4b08-9387-baca67fc3e54")

new_user = service.create(name="Product1", price=1.2)

