'''
Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists 
(without duplicates). Make sure your program works on two lists of different sizes.
'''
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

unique_list =[] 
for i in a:
    for j in b:
        if i == j:
            if i not in unique_list:
                unique_list.append(i)

print(unique_list)
#This has quadratic time complexity

#SOLUTION 2
unique_list =[] 
for i in a:
    if i in b and i not in unique_list:
        unique_list.append(i)

print(unique_list)
#Now this has linear time complexity