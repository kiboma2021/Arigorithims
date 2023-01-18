def diagonalDifference(arr):
    # Write your code here
    primary=0
    secondary=0
    n=len(arr)
    print(n)
    
    for i in range(0,n):
        print("====",arr[i][n-1-i])
        primary+=arr[i][i]
        secondary+=arr[i][n-1-i]
    diagonaldif=abs(abs(primary)-abs(secondary))
    return diagonaldif #diagonaldif

a = [[ 1, 2, 3, -4 ],
     [ 5, 6, 7, 8 ],
     [ 1, 2, 3, 4 ],
     [ -5, 6, 7, 8 ]]

print(diagonalDifference(a))