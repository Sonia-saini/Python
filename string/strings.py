from operator import concat


print("hello")
print('Hello')
a='sonia'
print(a)
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

a = "Hello, World!"
b=[1,2,3,4,5]
print(len(b))
print(a[1])
for i in a :
    print(i,len(a))
txt = "The best things in life are free!"
print("The" in txt)

# if 
if "The" in txt :
    print("Yes present")
else :
    print("No")
print("the" not in txt)
if "The" not in txt :
    print("no present")
else :
    print("yes")
b = "  Hello, World!    "
print(b[2:5])
print(b[:5])
print(b[2:])
print(b[-5:-2])
print(b.upper(),b.lower(),b.strip(),b.replace("H","S"),b.split(","))

# concatination
x="hii"
y="soni"
z=x+y
print(x+" "+y)
# string format
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
txt="i want {} pieces of {} in {}"

print(txt.format(3,"apple","10 rs"))
txt = "We are the so-called \"Vikings\" from the north."
print(txt)