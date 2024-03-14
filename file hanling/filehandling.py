import os
x=open("demo.txt","r")
print(x.read(2))
print(x.read())
print(x.readline())
x.close()
x=open("demo.txt","a")
x.write("\n now file have more content")
x.close()
x=open("demo.txt","r")
print(x.read())
x.close()
f = open("demo.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the overwriting:
f = open("demo.txt", "r")
print(f.read())
os.remove("d1.txt")
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")
# x.write("hello sonia")