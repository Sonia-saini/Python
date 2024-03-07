a=300
b=400
c=500
if a>b :
    print("a is greater than b")
elif b>a:
    print("b is greater than a")
else :
    print(" a and b is equal")
if a ==b : print("a and b both equal")
print("a") if a>b else print("=") if a==b else print("b") 
print("b shorter") if b<a else print("a shorter") if a<b else print("both equal")
if a<b and a<c : print("a is smallest value")
if a > b or a < c:
  print("At least one of the conditions is True")
if not a>c :
    print("a is not greater than c")
if a<b :
    print("a is smaller than b")
    if(a<c):
        print("a is also smaller than c")
    else : print("c is not greter")
if c >a :
    pass


# In this example we use two variables, a and b, which are used as part of the if statement to test whether b is greater than a. As a is 33, and b is 200, we know that 200 is greater than 33, and so we print to screen that "b is greater than a".