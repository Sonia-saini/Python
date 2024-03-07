from traceback import print_tb


thisdic={
    "name":"sonia",
    "batch":"web-19",
    "city":"jind",
    "city":"hisar"
}
print(thisdic)
print(thisdic["name"])
# length
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(len(thisdict))
# type
print(type(thisdic))
# use dict()
dicts=dict(name="sonia",last_name="saini")
print(dicts)
print(thisdic.get("city"),thisdic.keys())
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x,car.values()) #before the change

car["color"] = "white"

print(x,car.items()) #after the change

if "model" in car :
    print("yes")
# change the values
car["year"]=2020
car.update({"brand":"bmw"})
# add new key values
car['type']="car"
car.update({"electrical":False})
print(car)
#remove the key values
car.pop("type")
car.popitem()
del car["color"] # del car means car dictionary is deleted (not exist)
car.clear()
print(car)
for x in thisdic :
    print(x) #print keys
    print(x +":"+ thisdic[x]) #print values
for x in thisdic.values() :
    print(x) # print values
for x in thisdic.keys() :
    print(x) #print all keys
for x,y in thisdic.items():
    print(x,y)
#copy
x=thisdic.copy()
y=dict(thisdic)
print(x,y)
# Example
# Create three dictionaries, then create one dictionary that will contain the other three dictionaries:

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily)
# acces value 
print(myfamily["child1"]["name"])