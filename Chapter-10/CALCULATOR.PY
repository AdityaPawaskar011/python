# function to Add two numbers 
def add(num1,num2):
    return num1 + num2
# function to subtract two numbers 
def sub(num1,num2):
    return num1 - num2
# function to Multiply two numbers 
def mul(num1,num2):
    return num1 * num2
# function to Division two numbers 
def div(num1,num2):
    return num1 / num2
# function to Division two numbers 
def avg(num1,num2):
    return (num1 / num2)/2    

def rec():
    try:

        select = int(input("Select a operation from 1,2,3,4,5 : "))
    
        num1 = int(input("Enter first number: \n"))
        num2 = int(input("Enter second number: \n"))
        my_dict={1 : add,
         2 : sub,
         3 : mul ,
         4 : div ,
         5 : avg}
    

        res=my_dict[select](num1, num2)
        print(f"The {my_dict[select]} of {num1, num2} is {res}")
        return rec()
    except:
        print(f"Choose valid Number Between 1 to 5 To perfporm operation on {num1 , num2}")
 


rec()


   
    
    
