class Calculator:
    def __init__(self):
        self._current_val = 0

    def add(self,x,y):
        sum = x + y
        self._current_val = sum
        return sum