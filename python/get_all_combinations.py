from itertools import combinations

def GetCombinations(mylist,r):
    return list(combinations(mylist,r))
mylist=['a','b','c','d']
r=len(mylist)
print(GetCombinations(mylist,r))
