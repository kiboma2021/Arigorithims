'''
Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. 
Print the decimal value of each fraction on a new line with  places after the decimal.

'''

def plusMinus(arr):
    # Write your code here
    n=len(arr)
    pos_count=0
    neg_count=0
    zero_count=0
    for i in arr:
        if i<0:
            neg_count+=1
        elif i==0:
            zero_count+=1
        else:
            pos_count+=1
    print(format((pos_count/n),'.6f'))
    print(format((neg_count/n),'.6f'))
    print(format((zero_count/n),'.6f'))