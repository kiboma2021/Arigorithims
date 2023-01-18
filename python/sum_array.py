'''
Write a program to check and return the pairs of a given array A whose sum value is equal to a target value N
arr = [1, 2, 40, 3, 9, 4]
N = 3
'''
def sumArray(arr,N):
    result=[]
    arr.sort() # Sort the array
    print(arr)

    i=0
    while arr[i]<N:
       # print("-----i---",arr[i])
        j=i+1
        while arr[j]<N:
            #print("----j---",arr[j])
            if arr[i]+arr[j]==N:
                result.append(arr[i])
                result.append(arr[j])
                print("Hurray!....")
            j+=1
        i+=1
    print(result)
    return result

sumArray([1, 2, 40, 3, 9, 4],12)