class Base:
    def __init__(self):
        self.x = 10
class Derived(Base):
    def __init__(self):
        super().__init__()
        self.y = 20

class BaseForma:
    def PrintName(self): print("Forma2")
class Forma:
    def PrintName(self): print("Forma1")
class Square(BaseForma, Forma):
    pass
class Circle(Forma):
    def PrintName(self): print("Circle")
class Rectangle(Forma):
    def PrintName(self): print("Rectangle")
for form in [Square(),Circle(),Rectangle()]:
     form.PrintName()

class CarList:
    cars = ["Dacia","BMW","Toyota"] 
    def __iter__(self):
        self.pos = -1
        return self #iter(self.cars)
    def __next__(self):
        self.pos += 1
        if self.pos==len(self.cars): raise StopIteration
        return self.cars[self.pos]
c = CarList() 
for i in c:
    print (i)