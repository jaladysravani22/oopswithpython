class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def move(self):
       
        pass

class Car(Vehicle):
    def move(self):
        return f"The {self.brand} car drives on roads."

class Plane(Vehicle):
    def move(self):
        return f"The {self.brand} plane flies in the sky."


vehicles = [Car("Tesla"), Plane("Boeing")]

for vehicle in vehicles:
    print(vehicle.move())
