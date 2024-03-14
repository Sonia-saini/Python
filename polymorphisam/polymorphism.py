x = "Hello World!"

print(len(x))
mytuple = ("apple", "banana", "cherry")

print(len(mytuple))
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
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

car1 = Car("Ford", "Mustang")       #Create a Car class
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat class
plane1 = Plane("Boeing", "747")     #Create a Plane class

for x in (car1, boat1, plane1):
  x.move()
print(len(thisdict))
class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car1(Vehicle):
  pass

class Boat1(Vehicle):
  def move(self):
    print("Sail!")

class Plane1(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car1("Ford", "Mustang") #Create a Car object
boat1 = Boat1("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane1("Boeing", "747") #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()