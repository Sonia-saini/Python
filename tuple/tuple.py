thistuple = ("apple", "banana", "cherry")
print(thistuple)
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
print(len(thistuple))
thisnottuple=("apple")
print(type(thisnottuple))
thistuple=("apple",)
print(type(thistuple))
tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)
print(tuple(("a","b","c")))
print(tuple1[1])
print(tuple1[-1])
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[1:3])
# This example returns the items from the beginning to, but NOT included, "kiwi":

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])
# By leaving out the end value, the range will go on to the end of the tuple:

# Example
# This example returns the items from "cherry" and to the end:

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])
if "apple" in thistuple :
    print("yes i found apple")
x = ("apple", "banana", "cherry")
y=list(x)
y.append("orange")
y[1]="kiwi"
x=tuple(y)
y=("mango",)
print(x+y)
thistuple = ("apple", "banana", "cherry")
x=list(thistuple)
x.remove("cherry")
thistuple=tuple(x)
print(thistuple)
thistuple = ("apple", "banana", "cherry")
del thistuple
fruits = ("apple", "banana", "cherry") #packing the tuple
(red,Yellow,green)=fruits #unpackiing the tuple
print(red,Yellow,green)
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, *yellow, red,pink) = fruits

print(green)
print(yellow)
print(red,pink)
thistuple = ("apple", "banana", "cherry")
for i in thistuple :
    print(i)
for i in range(len(thistuple)) :
    print(thistuple[i],i)

i=0
while i<len(thistuple) :
    print(thistuple[i])
    i+=1
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
print(tuple1+tuple2)
print(tuple1*2)