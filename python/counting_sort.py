'''
Given a list of integers, count and return the number of times each value appears as an array of integers.
Always return a frequency array with 100 elements.
'''

def countingSort(arr):
    # Write your code here
    result=[]
    for i in range(0,100):
        if i in arr:
            result.append(arr.count(i))
        else:
            result.append(0)
    return result