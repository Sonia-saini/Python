import datetime
x=datetime.datetime.now()

print(x.year)
print(x.strftime("%A")) #wednesday
print(x.strftime("%a")) #wed
print(x.strftime("%w"))# 3
print(x.strftime("%d")) #13
print(x.strftime("%b")) #Mar
print(x.strftime("%B")) # March
print(x.strftime("%m")) # 03