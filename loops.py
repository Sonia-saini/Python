

# range(start,stop,step),range(stop)=range(0,stop,1)
from ctypes import sizeof
from operator import concat


for i in range(1,4,2):
    print("sonia saini",i)


# while loop
i=0
while i<5:
    print(i)
    i=i+1

# break statement
for i in range(1,10,2):
    if i%2==0:
        break
    elif i%3==0:
        print(i,"3factor")
        continue
    else : print(i,"break")

# list or array 

arr=[8,2,3,4]
for i in arr :
    print(i)
print(arr[0])
# slice a list
print(arr[1:2])
print (arr[2:])
print(arr[:3])
# size of list
print(len(arr))
# sort
# print(arr.sort)
# obj
obj={ "name":"sonia","lastname":"saini"}
for i in obj :
    print(i,obj[i])
print(obj)

# string :- list of characters
name="sonia saini"
lastname="saini"
# print all alphabate
for i in name :
    print(i)
# length of string
print(len(name))
# concatinate
print(concat(name,lastname))