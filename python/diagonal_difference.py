'''
Given a square matrix, calculate the absolute difference between the sums of its diagonals.

'''

def diagonalDifference(arr):
    # Write your code here
    primary=0
    secondary=0
    n=len(arr)-1
    for i in range(0,n+1):
        primary+=arr[i][i]
        secondary+=arr[i][n-i]
    diff=abs(primary-secondary)
    return diff