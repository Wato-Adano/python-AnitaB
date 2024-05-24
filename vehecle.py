class Vehicle:
    def__init__(self,model,make):
    self model = model
    self make = make
        
    def move(self):
        print("The vehicle is moving")
class Bus(Vehicle):
    def__init__(self,model, make, capacity):
    super()_init_(model,make)
    self.capacity = capacity
        
    def hoot(self):
     print("The bus is hooting")
    
    def check_capacity(self):
        print("The capacity is {self_capacity}")
        
class Lorry(Vehicle):
    def__init__(self,model,make,lorry_weight):
    super_init_(model,make)
    self.lorry_weight =lorry_weight
        
    def unloading(self):
            print("Unloading the lorry")
            
            b=Bus("x","Isuzu",70)
            b.move()
            b.hoot()
            
            l=Lorry("t","vehicle",80)
    