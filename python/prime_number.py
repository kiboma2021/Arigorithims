'''
Ask the user for a number and determine whether the number is prime or not. 

'''
import math
get_number =int(input("Enter a number: "))
count=0
for i in range (2,get_number):
    if get_number%i == 0:
        count+=1
        break
if count>0:
    print("The entered number is not a prime number")
else:
    print("The entered number is a prime number") 


count=0
sqrt_number=int(math.sqrt(get_number))+1
for i in range (2,sqrt_number):
    if get_number%i == 0:
        count+=1
        break
if count>0:
    print("The entered number is not a prime number")
else:
    print("The entered number is a prime number") 