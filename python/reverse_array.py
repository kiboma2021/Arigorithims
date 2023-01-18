'''
arraylist = [c,o,d,i,n,g,' ',s,c,h,o,o,l,' ',c,l,o,s,e,d]
output = [c,l,o,s,e,d,' ',s,c,h,o,o,l,' ',c,o,d,i,n,g]

'''
def reverseArray(arr):
    arr=''.join(arr)
    print(arr)

    arr=arr.split(' ')
    print(arr)

    reversedstr=[]

    for i in range(len(arr)-1,-1,-1):
        reversedstr.append(arr[i])
    
    reversedstr=' '.join(reversedstr)
    reversedstr=reversedstr.split(' ')

    print(reversedstr)

arr=['c','o','d','i','n','g',' ','s','c','h','o','o','l',' ','c','l','o','s','e','d']
reverseArray(arr)