'''
Write python function which takes a variable number of arguments.
'''

def AddNums(*nums):
    total=0
    for i in nums:
        total+=i
    return total

print(AddNums(20,10,5,15))