str1="We GoNNA Go to amErica"
print(str1.lower())
print(str1.upper())

print(str1.split(" "))


print("================================================")
str1=str1.lower()
str2=str1.split(" ")

print(str1)
print(str2)

str3=' '.join(str2)
print(str3)
print("================================================")

#This loops through each character
for i in str1:
    print(i,end=" ")
print("\n")

#This loops through each word
for i in str2:
    print(i,end=" ")
print("\n")


print("===================Reverse all characters=============================")

for i in range(len(str1)-1,-1,-1):
    print(str1[i],end="")
print("\n")

print("===================Reverse each word =============================")

for i in range(len(str2)-1,-1,-1):
    print(str2[i],end=" ")
print("\n")