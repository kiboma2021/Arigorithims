'''
Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. 
 1, 1, 2, 3, 5, 8, 13
'''

def fibonnaci_generate(n):
    if n == 1:
        return [0]
    fib_nums=[0,1]
    for i in range(3,n+1):
        next_num=fib_nums[i-3] + fib_nums[i-2]
        fib_nums.append(next_num)
    return fib_nums

for i in fibonnaci_generate(1):
    print(i, end=" ")
    
print("\n")

