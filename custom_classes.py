class Calculator:
    def __init__(self):
        self._current_val = 0

    def divide(self,x,y):
        if y == 0:
            raise ValueError("y must not be equal to zero")
        division = x / y
        self._current_val = division
        return division