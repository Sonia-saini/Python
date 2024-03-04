thissets={"apple","mango","banana"}
print(thissets,type(thissets))
# Duplicates Not Allowed
# Sets cannot have two items with the same value.

# Example
# Duplicate values will be ignored:

thisset = {"apple", "banana", "cherry", "apple"}

print(thisset) # it will print only first apple and ignore oter repititve element
thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)
thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)
print(len(thisset))
set1 = {"abc", 34, True, 40, "male"}
print(type(set1))
thisset=set(("apple", "banana", "cherry"))
print(thisset)
for x in thisset :
    print(x)
print ("banana" in thisset)
thisset.add("kiwi")
print(thisset)
tropical = {"pineapple", "mango", "papaya"}
list1=["apple","banana"]
thisset.update(tropical)
thisset.update(list1)
print(thisset)
thisset.remove("banana")
thisset.discard("apple")
thisset.pop()
print(thisset)
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)
# Example
# The del keyword will delete the set completely:

thisset = {"apple", "banana", "cherry"}
for x in thisset :
    print(x)
del thisset
thisset = {"apple", "banana", "cherry"}
set1={"kiwi","mango","banana"}
set2=thisset.union(set1)
thisset.update(set1)
print(set2,thisset)
set1.intersection_update(thisset)
print(set1)
# print(thisset)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)
x.intersection_update(y)
print(x)
x.symmetric_difference_update(y)
print(z,x)
x = {"apple", "banana", "cherry",True}
y = {"google", "microsoft", "apple",1}
z=x.symmetric_difference(y)
print(z)