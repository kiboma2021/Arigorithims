"""
You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.

You are given a list of strings operations, where operations[i] is the ith operation you must apply to the record and is one of the following:

An integer x.
Record a new score of x.
'+'.
Record a new score that is the sum of the previous two scores.
'D'.
Record a new score that is the double of the previous score.
'C'.
Invalidate the previous score, removing it from the record.
Return the sum of all the scores on the record after applying all the operations.

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
        
