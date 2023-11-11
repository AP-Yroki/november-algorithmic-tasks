class Car:

    def __init__(self,car_brand, model, year_release, mileage):
        self.car_brand = car_brand
        self.model = model
        self.year_release = year_release
        self.mileage = mileage


    def set_car_brand(self, car_brand):
        self.car_brand = car_brand

    def get_car_brand(self):
        print(self.car_brand)

    def get_model(self):
        print(self.model)

    def set_model(self, model):
        self.model = model

    def get_year_release(self):
        print(self.year_release)

    def set_year_release(self, year_release):
        self.year_release = year_release

    def get_mileage(self):
        print(self.mileage)

    def set_mileage(self, mileage):
        self.mileage = mileage

car1 = Car('Tesla', '1S Pro Max Ultra', 2047, 0)

car1.set_mileage(20941)
car1.get_mileage()