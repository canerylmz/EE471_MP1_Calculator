class Calculator:
    def __init__(self):
        self._current_val = 0

    def add(self,x,y):
        sum = x + y
        self._current_val = sum
        return sum

    def subtract(self,x,y):
        diff = x - y
        self._current_val = diff
        return diff
    
    def multiply(self,x,y):
        product = x * y
        self._current_val = product
        return product

    def divide(self,x,y):
        if y == 0:
            raise ValueError("y must not be equal to zero")
        division = x / y
        self._current_val = division
        return division