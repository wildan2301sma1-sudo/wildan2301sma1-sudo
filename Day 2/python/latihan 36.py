class Car:
    def __init__(self, brand, model):
        self.brand = brand 
        self.model = model
        
    def move(self):
        print("Drive!")
        
class Boat:
     def __init__(self, brand, model):
            self.brand = brand 
            self.model = model 
            
     def move(self):
         print("Sail!")
        
class Plane:
     def __init__(self, brand, model):
            self.brand = brand 
            self.model = model
              
     def move(self):
         print("Fly!") 
        
carl = Car("Ford", "Mustang")       #Create a car class
boatl = Boat("Ibiza", "Touring 20") #Create a Boat class
planel = Plane("Boeing", "747")     #Create a Plane class

for x in (carl, boatl, planel):
    x.move()
 
            