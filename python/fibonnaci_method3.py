''''
Using generator method
Generate n fibonacci numbers

'''
def fib(n):
    p,q=0,1
    i=0
    while i<n:
        yield p
        p,q=q,p+q
        i+=1

for i in fib(10):
    print(i, end=" ")
print("\n")
