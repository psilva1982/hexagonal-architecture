from pickle import TRUE
from tkinter import N
from tkinter.messagebox import NO
from uuid import uuid4
from .interface import ProductInterface
from .interface import ENABLE, DISABLE
from application import exceptions

class Product(ProductInterface):

    def is_valid(self) -> bool:
        if self.status == None:
            self.status = DISABLE
        
        if self.status != ENABLE and self.status != DISABLE:
            raise exceptions.ProductStatusError
        
        if self.price < 0 and self.status == ENABLE:
            raise exceptions.ProductEnableError

        return True

    def enable(self):
        if self.price > 0: 
            self.status = ENABLE

        else: 
            raise exceptions.ProductEnableError

    def disable(self):
        if self.price <= 0: 
           self.status = DISABLE

        else: 
            raise exceptions.ProductDisableError

    def get_name() -> str:
        pass

    def get_id() -> str:
        pass

    def get_price() -> float:
        pass
    
    def get_status() -> str:
        pass