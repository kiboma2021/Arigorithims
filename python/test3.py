def staircase(n):
    # Write your code here
    for i in range(1,n):
        print(' ' * (n-1-i), "#" * i)
    print("#" * n)

staircase(4)