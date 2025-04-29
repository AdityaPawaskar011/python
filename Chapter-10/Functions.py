#Create function
def greeting():
    print("This is my first function")

#call function 
greeting()

#add function
def Add2Numbers(a,b):
    result=a+b
    print(f"The sum of two numbers is: {result}")

Add2Numbers(10,10)
Add2Numbers(50,10)
Add2Numbers(b=100,a=100)


#Function with return statement 
def addNumber(a,b):
    return a+b
sum=addNumber(10,2)
print(sum)

