# year=int(input("Enter the year:"))

# if (year%4==0 and year/100!=0) or (year/400==0):
#     print(f"{year} is Leap Year")
# else:
#     print(f"{year} is Not a Leap Year")



Username='Aditya'
Password='123'


# Login=input('Username:-')
# Pass= input('Password:-')



# if(Login==Username and Pass==Password):
#     print("Both Username and password are correct")
# elif(Login==Username and Pass!=Password):
#     print("Username is correct but password is incorrect")
# elif(Login!=Username ):
#     print("Username is incorrect")


# if Login==Username:
#     if Pass==Password:
#         print("Welcome! login was sucessful")
#     else:
#         print("Incorrect Password")
# else:
#     print("Username is incorrect")



Marks_Maths=int(input("Marks of Mathematic's:- "))

Marks_Physics=int(input("Marks of Physics's:- "))

Marks_Chemistry=int(input("Marks of Chemistry's:- "))

if  (Marks_Maths + Marks_Physics + Marks_Chemistry >= 180) or (Marks_Maths + Marks_Physics >= 140):
    print("You are eligible")
else:
    print("you are not eligible")


if (Marks_Maths >= 65 and Marks_Physics >= 55 and Marks_Chemistry >= 50 \
 and (Marks_Maths + Marks_Physics + Marks_Chemistry >= 180)) or (Marks_Maths + Marks_Physics >= 140):
    print("You are eligible")
else:
    print("you are not eligible")




