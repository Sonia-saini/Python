# arthmatic Operations :- Plus(+),minus(-), multiply(*),exponent(**), modular or reminder(%), divide(/)
x=5
y=6
plus=x+y
minus=x-y
multi=x*y
exponent=x**y
reminder=x%y
divide=x/y
print(type(plus),plus)
print(type(minus),minus)
print(type(multi),multi)
print(type(exponent),exponent)
print(type(reminder),reminder)
print(type(divide),divide)

# comparison operators:- equal to (==),less than(<),greater than (>),not equal to (!=);
equal=x==y
less_than=x<y
not_equal=x!=y
greater=x>y
less_than_and_equal=x<=5
print(equal,less_than,not_equal,greater,less_than_and_equal)
# logial operators :- or,and,not
print(not x<y and 7<8)
print (not 3>4 or 5<6)
print (False or not False and False)
# not is evaulated first
# and is evaulated next 
# or is evaulated last
# contidtional statements :- if , else if ,else

num=24
if num % 2==0 :
 print("divisble by 2")
if num %3==0 :
 print("divisible by 3")
else:
 print("not divisible by 2")