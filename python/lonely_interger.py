'''
Given an array of integers, where all elements but one occur twice, find the unique element.

Example
a=[1,2,3,4,5,1,3,2,5]

The unique element is 4 .

'''

def lonelyinteger(a):
    # Write your code here
    for i in a:
        if a.count(i)==1:
            return i