#String Indexing 



my_name='Aditya'
print(my_name[0])
print(my_name[-1])


name="Hello world!"
print(name[5])

print(name[0:5:2])

print(name[-2])   # last 2 characters


print(name[0::2])  #every second character 
print(name[:])  #all characters
print(name[::])  #all characters

print(name[::-1])  #reverse characters


#String Methods

print(len(name))
print(name.upper())
print(name.lower())
print(name.count('o'))
print(name.find('h'))
print(name.split(' '))
print(name.replace('world','Aditya'))
print(name.title())

name2="  Hello Aditya     "
print(name2.strip())

words=("Aditya","is","great")

print(" ".join(words))
