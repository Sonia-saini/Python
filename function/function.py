arr=[23,34,453,23424,5345,243,45,4565456,67]


def checkit(num):
   if num%2==0 :
      print(num ,"is even number")
   else :
      print(num,'is odd numer')

for i in arr :
   checkit(i)

def my_function():
  print("Hello from a function")

my_function()

def myname(name,lastname):
   print("My name is " + name + " "+lastname)
myname("sonia","saiini")
myname("arunita","sharma")
def myfunction(*kids):
  print("The youngest child is " + kids[2])

myfunction("Emil", "Tobias", "Linus","saini")

def names(**name):
  print("my name is "+ name["lastname"]+name["firstname"])

names(firstname="sonia",lastname="saini")
def default(country="India"):
   print("i am from "+country)
default()
default("America")
def my_function1(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function1(fruits)
def my_function2(x):
  return 5 * x

print(my_function2(3))
print(my_function2(5))
print(my_function2(9))
# The pass Statement
# function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.

# Example
def myfunction1():
  pass
def funct(x,/):
  print(x)
funct(3)
funct(5) #funct(x=4) wrong
def funct1(*,x):
  print(x)
funct1(x=3)
# funct1(5) wrong way
def my_function3(a, b, /, *, c, d):
  print(a + b + c + d)

my_function3(5, 6, c = 7, d = 8)

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")