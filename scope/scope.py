# local scopes example 
y=5000 #global scope variable
x=400
def local():
    global x
    x=5 #local scope variable
    global z
    z=66
    print(x)
    def mylocal():

      print(x)
      print(y)
    mylocal()
local()
print(z)
# print(x)