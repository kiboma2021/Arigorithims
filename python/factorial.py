def fact(n):
    result=1
    for i in range(1,n+1):
        result = i * result
    print(result)
    return (result)

fact(0)