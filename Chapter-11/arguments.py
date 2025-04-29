#Arguments in Function


#1. Required arguments

# def greetings(name):         #Name is a Parameter 
#     print("Hello ",name,"!")

# greetings("Aditya")          #Aditya is argument


# def intro(Course_name,Instructor_name):
#     print("Welcome to ",Course_name," Course by ",Instructor_name)

# intro("Python","Aditya")    

# #2. Default argumemt 

# def greet(name="World"):
#     print("Hello",name,"!")

# greet()
# greet("Aditya")


# #3 Keyword Argument

# def div(a,b):
#     return a/b

# c=div(10,20)

# print(c)

# #4 Arbitary Argument 

# def Add2Number(a,b):
#     return (a+b)

# result=Add2Number(10,2)
# print (result)

# def add_numbers(*args):    #variable number of arguments
#     return sum(args)

# output=add_numbers(1,2)
# print(output)


#5 Arbitary kryword argument

def print_details(**keyword):
    for key,value in keyword.items():
        print(f"{key} : {value}")

print_details(name='Aditya',age = 26,city='Mumbai')

