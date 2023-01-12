'''
Ask the user for a string and print out whether this string is a palindrome or not. 
(A palindrome is a string that reads the same forwards and backwards.)

NB: Strings are lists
'''
my_string ="eggs"

#SOLUTION 1
if my_string == my_string[::-1]:
    print("The given string is a palindrome 1")
else:
    print("The given string is not a palindrome 1")

#SOLUTION 2

rev_str=""
for i in my_string:
    rev_str=i+rev_str
if rev_str == my_string:
    print("The given string is a palindrome 2")
else:
    print("The given string is not a palindrome 2")