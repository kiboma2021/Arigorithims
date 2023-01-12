'''
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.

Extras:

If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

'''


print("Please enter a number:")
num=int(input())

if num%2==0:
    print("The number entered is an even number")
else:
    print("The number entered is an odd number")

if num%4==0:
    print("The number entered is a multiple of four")
