username = input("Enter username:")
print("Username is: " + username)
try:
    
    print(x) #x is not defined
except:
    print("throw error")

try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
finally:
   print("try expect finished")


try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

try:
  f = open("demofile.txt")
  print(f)
  try:
    f.write("sonia")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")

x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")

