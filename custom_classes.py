class Calculator:
    def __init__(self):
        self._current_val = 0
    
    def multiply(self,x,y):
        product = x * y
        self._current_val = product
        return product