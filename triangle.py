class Triangle:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def type_of_trangle(self):
        if self.a == self.b == self.c:
            print('Равносторонний трегуольник')
        elif self.a == self.b or self.a == self.c or self.b == self.c:
            print('Равнобедренный треугольник')
        else:
            print('Разносторонний треугольник')

    def find_area(self):
        s = (self.a + self.b + self.c) / 2
        area = (s * (s-self.a) * (s - self.b) * (s-self.c)) ** 0.5
        print(area)


tr1 = Triangle(5, 5, 6)
tr1.type_of_trangle()
tr1.find_area()