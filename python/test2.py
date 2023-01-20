"""
Compare two strings in python
eg hello and heoll should be equal

"""

str1="hello"
print(sorted(str1))

def compareStr(str1,str2):
    str1=sorted(str1.lower())
    str2=sorted(str2.lower())

    if len(str1) != len(str2):
        #print("Length not the same")
        return False
    else:
        for i in range(0,len(str1)):
            if str1[i]!=str2[i]:
                #print("Strings are not the same")
                return False
    #print("string characters are the same")
    return True

str1=input("Enter the first string: ")
str2=input("Enter the second string: ")
print(compareStr(str1,str2))