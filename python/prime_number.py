'''
Ask the user for a number and determine whether the number is prime or not. 

'''

get_number =int(input("Enter a number: "))
count=0
for i in range (2,get_number):
    if get_number%i == 0:
        count+=1

print("The entered number is not a prime number")