'''
Given five positive integers, find the minimum and maximum values that can be calculated by 
summing exactly four of the five integers. Then print the respective minimum and maximum values 
as a single line of two space-separated long integers.

Example

arr=[2,45,14,5,15,1]

16 24

'''

def miniMaxSum(arr):
    # Write your code here
    arr=sorted(arr)
    n=len(arr)
    min_sum=0
    max_sum=0
    for i in range(0,n):
        if i==0:
            min_sum+=arr[i]
        elif i==n-1:
            max_sum+=arr[i]
        else:
            min_sum+=arr[i]
            max_sum+=arr[i]
    print(min_sum,end=" ")
    print(max_sum)            