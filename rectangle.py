class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def find_square(self):
        square = self.length * self.width
        print(f'Площадь: {square}')

    def find_perimeter(self):
        perimeter = (self.length + self.width) * 2
        print(f'Периметр: {perimeter}')


rc1 = Rectangle(7, 3)
rc1.find_square()
rc1.find_perimeter()