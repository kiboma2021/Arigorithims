def fib(n):
   p, q = 0, 1
   while(p < n):
       yield p
       p, q = q, p + q

## iterating using loop
for i in fib(10):
   print(i)    # output => 0 1 1 2 3 5 8