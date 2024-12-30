def square(x):
    return x * x


class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, value: float) -> float:
        """Adds value to current result"""
        self.result += value
        return self.result

    def multiply(self, value: float) -> float:
        """Multiplies current result by value"""
        if self.result == 0:
            self.result = value
        else:
            self.result *= value
        return self.result

    def get_result(self) -> float:
        return self.result
