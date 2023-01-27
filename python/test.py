def solution(cards):
    res=0
    for card in cards:
        for i in card:
            if i>res and card.count(i)==1:
                res=i
    if res==0:
        return -1
    else:
        return res

cards = [[5,5], [2,2]]
print(solution(cards))