class Parent:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def printname(self):
        print(self.name)
p1=Parent("sonia saini",20)

class Student(Parent):
 def __init__(self,name,age,year):
     super().__init__(name,age)
     self.passyear=year
 def Mygraduation(self):
   print('graduated in ',self.passyear)
p2=Student("sonika",30,2020)
p2.printname()
p2.Mygraduation()
p1.printname()
# print(p1)
tupl=("apple","mango","kiwi")
myitre=iter(tupl)
print(next(myitre))
print(next(myitre))
print(next(myitre))
# print(next(myitre))
