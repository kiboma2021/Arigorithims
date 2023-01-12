'''
Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 
'''


print("Enter a number:", end="") #0(1)
num = int(input()) #0(1)

divisors=[] #0(1)
for i in range(1,num): #0(n)
    if num%i == 0:
        divisors.append(i)
print (divisors)#O(1)
#0(n+4) # discard the constant time since it doesnt affect overall performance
# Hence the time complexity is O(n)
