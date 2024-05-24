class Animal:
    def__init__(self,name):
         self.name = name()
        
    def move(self):
        pass
    def make_noise(self):
        pass
class Cat(Animal):
    def move(self):
        print("The cat is walking")
        
    def make_noise(self):
            print("mew")
class Bird(Animal):
    def move(self):
        print("The bird is fyling")
        
    def make_noise(self):
       print("chief")
       
class Fish(Animal):
    def move(self):
        print("The fish is swimming")
        
    def make_noise(self):
      print("Boops")