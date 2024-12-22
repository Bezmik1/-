class Vehicle():

    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def get_info(self):
        print("Марка: {} Модель: {}".format(self.make, self.model))

class Car(Vehicle):

    def __init__(self, make, model, fuel_type):
        super().__init__(make, model)
        self.fuel_type = fuel_type
    
    def get_info(self):
        print("Марка: {} Модель: {} Топливо: {}".format(self.make, self.model, self.fuel_type))

benz = Vehicle("Mercedes", "Benz Truck")
benz.get_info()
bmw = Car("BMW","M5 F90","ДВС")
bmw.get_info()