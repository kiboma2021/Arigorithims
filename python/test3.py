cards=[[5,7,5,8,8,4,9,9],[5,6,4,5,6,2,4],[6,5,6,5,4,2,5,8,8,9,9]]
highest_num=0
for card in cards:
    #card=sorted(card)
    for i in card:
        if i>highest_num and card.count(i)==1:
            highest_num=i
if highest_num==0:
    print(-1)
else:
    print(highest_num)