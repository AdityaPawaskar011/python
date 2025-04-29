print ('Hello world!')

print("Won't give up!")

print('''"Double Quotes" and 'singl quotes' can be tricky''' )

print("\"Quotes\" and single quotes' can be tricky")

 

# % format of string 

name='Madhav'
print(type(name))
print('Hello my name is %s' %(name))
# %s ,%d are satrings for place holders

name='Aditya'
age=21
print("My name is {} and I am {}.".format(name,age))

print("My name is {0} and i am {1}.".format(name,age))

print("My name is {name} and i am {age}.".format(name='Adi',age=25))


# Escape characters 

print("Hello \naditya")

print("Hello \t aditya")


a="Hello"
b="Python"

print(a+b)
print(a*2)
print(a[1])
print(a[1:4])

if 'H' in a:
    print ("yes")
else:
    print("No")

if 'M' not in b:
    print ("yes")
else:
    print("No")

print(r'\n')



