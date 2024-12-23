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

toplivo = Vehicle("Merc", "GLS")
toplivo.get_info()
porshe = Car("Porshee","M5 F90","Дизель")
porshe.get_info()
