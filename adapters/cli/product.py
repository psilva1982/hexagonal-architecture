from app.services.interface import ProductServiceInterface
from app.services.product import ProductServiceInterface


def run(
    service: ProductServiceInterface,
    action: str,
    product_id: str,
    name: str,
    price: float,
) -> str:
    result = None

    if action == "create":
        product = service.create(name=name, price=price)
        result = f"Product ID {product.get_id()} with the name {product.name} has been created with the price {product.price} and status {product.get_status()}"

    elif action == "enable":
        product = service.get(id=product_id)
        service.enable(product=product)
        result = f"Product ID {product.get_id()} has been enabled"

    elif action == "disable":
        product = service.get(id=product_id)
        service.disable(product=product)
        result = f"Product ID {product.get_id()} has been disabled"

    else:
        product = service.get(id=product_id)
        result = f"Product ID: {product.get_id()}\nName: {product.name}\nPrice: {product.price}\nStatus: {product.get_status()}"

    return result
