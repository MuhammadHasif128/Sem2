class Shape:
    def __init__(self, side):
        self.side = side

    def calculate_perimeter(self):
        return 0


class Square(Shape):
    def __init__(self, side, length):
        super().__init__(side)
        self.length = length

    def calculate_perimeter(self):
        return self.side * self.length

    def __str__(self):
        return f"Square with {self.side} sides and length of {self.length} has a perimeter of {self.calculate_perimeter()}"


s = Square(4, 10)
print(s.__str__())





