print(10 > 9)
print(10 == 9)
print(10 < 9)
# Print a message based on whether the condition is True or False:

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
# Evaluate a string and a number:

print(bool("Hello"))
print(bool(15))
# The following will return True:

print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))
print(bool(""))
print(bool(0))
print(bool([]))
print(bool({}))
print(bool(None))
print(bool(()))
print(bool(False))
# Example
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

def evenNumber(x):
  if x%2==0:
    return True
  else:
    return False
  
if evenNumber(8):
  print("Yes")
else:
  print("No")

x = 200
print(isinstance(x, int),isinstance(x,str))