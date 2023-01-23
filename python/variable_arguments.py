'''
Write python function which takes a variable number of arguments.
'''

def addNums(*nums):
    total=0
    for num in nums:
        total+=num
    return total

print(addNums(10,20,30,45,25,63))

app_orr