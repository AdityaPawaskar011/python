# #Print first 10 natural Numbers using while loop
# print('1.Print first 10 natural Numbers using while loop')
# Natural_number=1

# while Natural_number<=10:
#     print(Natural_number)
#     Natural_number+=1

# #print the pattern

# print('\n2.print the pattern' )
# n=5
# for i in range(1,n+1):
#     for x in range(1,i+1):
#         print(x,end=" ")
#     print()    
  
# for x in range(1,n+1):
#     for y in range(1,x+1):
#         print(x,end=" ")
#     print()    


# for x in range(1,n+1):
#     for y in range(1,x+1):
#         print('*',end=" ")
#     print()

# print()
# for x in range(1,n+1):
#     for y in range(n+1-x):
#         print('*',end=" ")
#     print()        

# print()

# for x in range(1,n+1):
#     for y in range(n-x):
#         print(" ",end=" ")
#     for z in range(x):
#         print("*",end=" ")
#     print()        


# for x in range(1,n+1):
#     for y in range(1,x):
#         print(" ",end=" ")
#     for z in range(n+1-x):
#         print("*",end=" ")    
#     print()



# a=[2,4,6,8,10]

# newList=[]
# for x in a:
#     b=x*x
#     newList.append(b)
# print(newList)  

# newList = [x*x for x in a]
# print(newList) 


# num=int(input("Enter a number to sum:- "))
# s=0

# for x in range(1,num+1):
#     s += x
# print('\n')
# print("sum is :- ",s)    

# x=sum(range(1,num+1))
# print("sum is :- ",x )



# num=int(input("Enter a number to sum:- "))

# for x in range(1,11):
#     mul = x*num
#     print(mul)


# numbers = [12, 75, 150, 180, 145, 525, 50]


# for x in range(len(numbers)):
#     if numbers[x] % 5 == 0:
#         if numbers[x] > 500:
#             break
#         if numbers[x] > 150:
#             continue 
#         print('postition',x)
#         print(numbers[x])
    
      
# 6.Count the total number of digits in a number
# number=75869
# a=0
# while number !=0:
#     number=number//10
#     a +=1
# print (a)


#Exercise 7: Print the following pattern

# n=5
# for x in range(1,n+1):
#     for y in range(n-x+1,0,-1):
#         print(y,end=" ")
#     print()    



# n = 5
# k = 5
# for i in range(0,n+1):
#     for j in range(k-i,0,-1):
#         print(j,end=' ')
#     print()


# Print list in reverse order using a loop

# list1 = [10, 20, 30, 40, 50]

# list1.reverse()
# print(list1)

# for x in range(len(list1)-1,-1,-1):
#     print(list1[x])

# for x in list1[::-1]:
#     print(x)


# i=len(list1)-1

# while i >= 0:
#     print(list1[i])
#     i -= 1


#Exercise 9: Display numbers from -10 to -1 using for loop

# for x in range(-10,0):
#     print(x)


#Exercise 10: Display a message “Done” after the successful execution of the for loop

# for i in range(5):
#     print(i)
# print("done!")   

#Exercise 11: Print all prime numbers within a range

# start=25
# end =50

# for x in range (start,end+1,1):
#     for y in range(2,x):
#         if x % y == 0:
#            break
#     else:
#         print(x)    



#Exercise 12: Display Fibonacci series up to 10 terms

# n=10
# start=0
# end =1


# print(start,end=' ')
# print(end,end=" ")
# for x in range(n+1):
#     num=start+end
#     print(num,end=" ")
#     start = end
#     end = num


# Exercise 13: Find the factorial of a given number

# n=5
# factorial=1
# for x in range(1,n+1):
#     factorial *= x

# print(factorial)


#14: Reverse a integer number


# number=76542
# rev=0

# while number > 0:
#      c=number%10
#     #  print(c)
#      rev = (rev*10) +c
#      number=number//10
# print(rev)

# number = str(number)
# print(number)

# rev= number[::-1]
# print(int(rev))


#Exercise 15: Print elements from a given list present at odd index positions


# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]


# for x in range(len(my_list)):
#     if x % 2 ==0:
#         continue
#     else :
#         print (my_list[x],end=' ')



# Exercise 16: Calculate the cube of all numbers from 1 to a given number?

# num=int(input("Enter a number t calculate cube:- "))


# for x in range(1,num+1):
#     cube= x*x*x
#     print (f"The cube of {x} is {cube}")


# Exercise 17: Find the sum of a series of a number up to n terms

# num = 2
# terms =5

# for x in range(1,terms+1):
#     num=num+num

# Exercise 18: Print the following pattern


# n=5


# for x in range (1,n+1):
#     for y in range(1,x+1):
#         print('*',end=" ")
#     print()    
# for x in range (1,n+1):
#     for y in range(n-x+1):
#         print('*',end=" ")
#     print()  


# Exercise 19: Print Full Multiplication Table


# num=10

# for x in range(1,num+1):
#     print(f"Multiplication table of {x} \n")
#     for y in range (1,num+1):
#         print (y*x,end=" ")
#     print()    

#Exercise 20: Print the alternate numbers pattern
import time


n=5
count=0

start_time = time.time()
for x in range(1,n+1):
    for y in range(1,x+1):
        count+=1
        print(count,end=" ")
    print() 
end_time = time.time()

print(f"Excutio Time: {end_time - start_time}")

#Exercise 21: Flatten a nested list using loops

#Exercise 22: Find largest and smallest digit in a number

# num1 = 9876543210
# num2 = -5082





















