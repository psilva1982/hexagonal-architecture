
class ProductEnableError(Exception):
    def __init__(self):
        Exception.__init__(self,'Price must be greater than 0 to enable')

class ProductDisableError(Exception):
    def __init__(self):
        Exception.__init__(self,'Price must be less than  equal 0 to disable')

class ProductStatusError(Exception):
    def __init__(self):
        Exception.__init__(self,'the status must be enabled or disabled')