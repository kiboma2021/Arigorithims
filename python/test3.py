
def moseCordeconv(morsecode):
    result=[]
    n=len(morsecode)
    for i in range(0,n):
        if i<n-1 and len(result)!=0:
            if morsecode[i]=='.' and morsecode[i+1]=="." and result[len(result)-1]!='.':
                result.extend('-','-')
            else:
                result.append(morsecode[i])
        else:
            result.append(morsecode[i])            
    print(result)
                

morsecode="...."
moseCordeconv(morsecode)