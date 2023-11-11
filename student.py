
class Student:

    def __init__(self, name, age, mid_score):
        self.name = name
        self.age = age
        self.mid_score = mid_score

    def get_name(self):
        print(self.name)

    def set_name(self, name):
        self.name = name

    def get_age(self):
        print(self.age)

    def set_age(self, age):
        self.age = age


s1 = Student('Anton', 15, 5.00)
s2 = Student('Misha', 17, 3.55)

s1.set_age(22)
s1.get_age()

s2.set_name('Anatoliy')
s2.get_name()