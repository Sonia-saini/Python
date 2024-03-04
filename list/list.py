thislist = ["apple", "banana", "cherry"]
print(thislist)

# Lists allow duplicate values:

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
print(len(thislist))
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list1 = ["abc", 34, True, 40, "male"]
print(type(list1))
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
print(thislist[-2])
print(thislist[1:-1])
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
print(thislist[2:])
print(thislist[-4:-1])
if "apple" in thislist :
    print("yes")
thislist[1]="guwava"
print(thislist)
thislist[1:3]=["watermalon","banana","cake","asfs"]
print(thislist)
thislist[1:3]=["cake2"]
print(thislist)
thislist = ["apple", "banana", "cherry"]
thislist.insert(0, "watermelon")
print(thislist)
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
thislist.remove("kiwi")
print(thislist)
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
thislist.pop(0)#remove 0th index item
thislist.pop() #remove last item of the list
del thislist[1] #remove 1th index item and after this line thislist not found and we can print it.
print(thislist)
thislist.clear() # emty the list :- []
print(thislist)
del thislist #delete complete list and after this line thislist variable not found and we can print it.
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
i=0
while i<len(thislist):
   print(thislist[i])
   i=i+1
[print(x) for x in thislist]
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist=[]
for x in fruits :
   if "a" in x :
      newlist.append(x)
print(newlist)
print([x for x in fruits if "a" in x])
print([x for x in fruits if x!="apple"])
print([x for x in fruits])
newlist = [x for x in range(10)]
print(newlist)
newlist = [x for x in range(10) if x < 5]
print(newlist)
print([x.upper() for x in fruits])
print (["hello" for x in fruits])
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
thislist.sort(reverse=True)
print(thislist)
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
thislist.sort(reverse=True)
print(thislist)
def myfunc(n):
  return abs(n - 23)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key=str.lower)
print(thislist)
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
print(list(thislist))
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
print(list1+list2)

for x in list2 :
   list1.append(x)

print(list1)
list1.extend(list2)
print(list1)

