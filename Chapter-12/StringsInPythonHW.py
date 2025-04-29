#1.
pi=3.14159265359

print(round(pi,2))
print("Value of pi is {}".format(pi))

print("Value of pi is {:.2f}".format(pi))


print(f'value of pi is {pi:.2f}')


#2.

my_string="Python course"

print(my_string[2:8:2])

#3 Get center characters
name='Aaditya'

def mid_str(word):
    middle=int(len(word)/2)
    if len(word) %2 == 0:
        return word[middle-1 : middle+1]
    else:
        return word[middle]
    
print(mid_str(name))    


#4 Remove first 3 and last 3 characters from given my_string = "Regression Analysis" 

my_string1 = "Regression Analysis"
print(my_string1[3:-3])


#5
my_string3 = 'Classification'
print(my_string3[-4:])

#6
word='python' 
print(word[::-1])


#palindrome

letter='madam'

if letter[::-1]==letter:
    print("Its palindrome")
else:
    print("Its not palindrome")

print(letter[::-1])


print("Its not palindrome") if letter[::-1]!=letter else print("Its  palindrome")

#find() and index()

text = "Hello, world!"

# using find()
index_find = text.find("world") # returns 7
index_not_found_find = text.find("world") # returns -1
print (index_not_found_find)

# using index()
index_index = text.index("world") # returns 7
try:
    index_not_found_index = text.index("world") # raises ValueError
except ValueError:
    print("Substring not found")


















