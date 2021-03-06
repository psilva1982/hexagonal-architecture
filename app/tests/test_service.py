from unittest import mock
import unittest
from app.product import Product
from app.services.interface import ProductPersistenceInterface
from app.services.product import ProductService
import uuid 
from app.interface import ENABLE

class TestProductService(unittest.TestCase):

    def setUp(self):
        self.id = uuid.uuid4()
        self.persistence = ProductPersistenceInterface
        self.product = Product(id=self.id, name="Product", price=10)

    def test_get(self):
        self.persistence.get = mock.MagicMock(name='get')
        self.persistence.get.return_value = self.product

        service = ProductService(persistence=self.persistence)

        result = service.get(id=str(id))
        assert result.get_id() == self.product.get_id()
        assert result.get_name() == self.product.get_name()

    def test_create(self):

        id = uuid.uuid4()
        new_product = Product(id=id, name="Product", price=10)
        new_product.is_valid()

        self.persistence.save = mock.MagicMock(name='save')
        self.persistence.save.return_value = new_product

        service = ProductService(persistence=self.persistence)
        result = service.create(name=new_product.name, price=new_product.price)

        assert result == new_product
        assert result != None

    def test_enable_and_disable(self):
        
        self.persistence.enable = mock.MagicMock(name='enable')
        self.persistence.disable = mock.MagicMock(name='disable')
        service = ProductService(persistence=self.persistence)

        self.product.price = 10
        service.enable(product=self.product)

        self.product.price = -10
        service.disable(product=self.product)

        assert True