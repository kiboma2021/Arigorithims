"""
+ - Records a new score that is the sum of the previous two scores
D - Records a new score that is double the previous score
C - Invalidates the previous score, removing it from the record

"""
ops=['5','2','C','D','+']
result=0
n=len(ops)
ans=[]

#print(n)
for i in range(0,n):
    if ops[i] == '+':
        ans.append(int(ans[len(ans)-1])+ans[len(ans)-2])
    elif ops[i]=='D':
        ans.append(int(ans[len(ans)-1])*2)
    elif ops[i]=='C':
        ans.pop()
    else:
        ans.append(int(ops[i]))

for i in ans:
    result+=i
print(result)
        
