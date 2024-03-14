class myclass :
    x=5
p1=myclass()
print(p1.x)
class Person:
 def __init__(self,name,age):
        self.name=name
        self.age=age
 def __str__(self):
  return f"{self.name}({self.age})"
 def myfunc(anc):
    print("my name is "+anc.name)
p2= Person("sonia",20)
# modify the object
p2.age=40
# delete object property
del p2.name
p2.myfunc()
print(p2.name,p2.age,p2)