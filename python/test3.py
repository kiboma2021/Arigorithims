from itertools import combinations

def moseCordeconv(morsecode):
    morsecode=tuple(morsecode)
    result=[]
    n=len(morsecode)
    for j in range(1,n):
        i=j
        updatedmorsecode=list(morsecode)
        while i<n:
            if updatedmorsecode[i]=='.' and updatedmorsecode[i-1]==".":
                updatedmorsecode[i]='-'
                updatedmorsecode[i-1]='-'
                i+=3
            else:
                i+=1

        updatedmorsecode=''.join(updatedmorsecode)
        result.append(updatedmorsecode)

    print("=======",result)

morsecode="...."
moseCordeconv(morsecode)