language='python'

for x in language:
    print(x)


for x in range(1,5):
    print(x)

for x in range(1,10,2):
    print(x)


#pass statement


for i in range(5):
    pass

print('-------------PASS--------------------')
i=5
while i>0:
    if i == 3:
     pass
    else:
     print(i)
    i -= 1

print('-------------BREAK--------------------')


for i in range(5):
   if i == 3:
      continue
   print(i)



for num in range(3):
   for i in range(1,4):
      print(i)
   print('- - - - - - - ')  
