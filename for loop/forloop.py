fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
for x in "banana":
  print(x)
# break the statement
for x in fruits:
  if x=="banana":
    break
  else :
    print(x)
# skip the element
for x in fruits:
  if x=="banana":
    continue
  else:
    print(x)
for x in range(5):
  print(x)
for x in range(2,9):
  print(x)
else :
  print("finally finished")
for x in range(2,10,10): # range(start,end,increment)
  print(x)
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
for x in [0, 1, 2]:
  pass