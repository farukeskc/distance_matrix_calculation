class Cell:
    def __init__(self, x, y, Q, code):
        self.x = x
        self.y = y
        self.Q = Q
        self.code = code

    def __str__(self):
        return f'Cell({self.x}, {self.y}, {self.Q}, {self.code})'