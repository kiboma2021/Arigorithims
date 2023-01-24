def sortBrackets(str):
    container1=[]
    container2=[]
    for i in str:
        print(container1)
        if i=='{' or i=='[' or i=='(':
            container1.append(i)
        elif i=='}':
            if container1[len(container1)-1] !='{':
                return False
            else:
                container1.pop()
        elif i==']':
            if container1[len(container1)-1] !='[':
                return False
            else:
                container1.pop()
        elif i==')':
            if container1[len(container1)-1] !='(':
                return False
            else:
                container1.pop()
        else:
            pass
    if len(container1) !=0:
        return False
    else:
        return True

str='{[{}]}'
print(sortBrackets(str))