class Circle:

    def __init__(self,radius):
        self.radius = radius

    def get_radius(self):
        print(self.radius)
    
    def set_radius(self, new_radius):
        self.radius = new_radius

krug = Circle(90)
krug.get_radius()
krug.set_radius(180)
krug.get_radius()