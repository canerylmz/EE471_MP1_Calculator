class Calculator:
    def __init__(self):
        self._current_val = 0

    def subtract(self,x,y):
        diff = x - y
        self._current_val = diff
        return diff