class Car:
    def __init__(self, color, brand, year, model, version, position = 0, gas 
    = True):
        self.color = color
        self.brand = brand
        self.year = year
        self.model = model
        self.version = version
        self.position = 0
        self.gas = gas

    def make_car_go(self):
        while self.gas == True:
            self.position += 1
            print(self.position)
        return self

car1 = Car("white", "toyota", 2017, "carolla", "base")
car2 = Car("black", "subaru", 2011, "impreza", "base")

car1.make_car_go()
