''''
Using generator method
Generate fibonacci numbers upto n
'''

def fib(n):
    p,q=0,1
    while p < n:
        yield p
        p,q=q,p+q

for i in fib(10):
    print(i, end=" ")
print("\n =================================================================")