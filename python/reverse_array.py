'''
arraylist = [c,o,d,i,n,g,' ',s,c,h,o,o,l,' ',c,l,o,s,e,d]
output = [c,l,o,s,e,d,' ',s,c,h,o,o,l,' ',c,o,d,i,n,g]

'''
def reverseArray(arr):
    n=len(arr)-1
    for i in range(n,0,-1):
        print(arr[i])

arr=[c,o,d,i,n,g,' ',s,c,h,o,o,l,' ',c,l,o,s,e,d]
reverseArray('[c,o,d,i,n,g,' ',s,c,h,o,o,l,' ',c,l,o,s,e,d]')