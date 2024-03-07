x=lambda a :a+10
print(x(2))
x=lambda a,b :a*b

print(x(10,20))
x=lambda a,b,c :a*b+c
print(x(2,3,10))
def myfunc(n):
  return lambda a : a * n
d=myfunc(4)
print(d(3))
print(myfunc(2)(3))