from itertools import product
from math import prod
from tkinter import N
from fastapi import FastAPI
from starlette.testclient import TestClient
from application.product import Product
from application.interface import DISABLE, ENABLE
from application.exceptions import ProductEnableError, ProductDisableError
import uuid

class TestProduct():

    def test_product_enable(self): 
        product = Product(
            id=uuid.uuid4(),
            name='Product',
            price=10
        )
        
        test1 = False
        try:
            product.enable()

        except ProductEnableError: 
           test1 = True

        product.price = 0
        test2 = False
        try:
            product.enable()

        except ProductEnableError: 
           test2 = True


        assert test1 == False
        assert test2 == True

    def test_product_disable(self): 
        product = Product(
            id=uuid.uuid4(),
            name='Product',
            price=0
        )

        test1 = False
        try:
            product.disable()
        except ProductDisableError: 
            test1 = True
        
        product.price = 10

        test2 = False
        try:
            product.disable()
        except ProductDisableError: 
            test2 = True

        assert test1 == False
        assert test2 == True

    def test_product_is_valid(self): 
        product = Product(
            id=uuid.uuid4(),
            name='Product',
            price=10,
        )
        test1 = True
        try:
            product.is_valid()
        except: 
            test1 = False
        
        product.price = -10
        test2 = False
        try:
            product.is_valid()
        except: 
            test2 = False
        

        assert test1 == True
        assert test2 == False

    # Add tests to other methods