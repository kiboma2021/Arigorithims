'''
Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. 
 1, 1, 2, 3, 5, 8, 13
'''

def fibonnaci_generate(n):
    fib_nums=[1,1]
    for i in range(3,n+1):
        next_num=fib_nums[i-3] + fib_nums[i-2]
        fib_nums.append(next_num)
    print(fib_nums)
    return fib_nums

fibonnaci_generate(9)
fibonnaci_generate(99)