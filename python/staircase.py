''''
This is a staircase of size n=4:
    #
   ##
  ###
 #### 

Its base and height are both equal to n. It is drawn using # symbols and spaces. 
The last line is not preceded by any spaces.
Write a program that prints a staircase of size .

'''

def staircase(n):
    # Write your code here
    for i in range(1,n):
        print(' '*(n-1-i),"#"*i)
    print("#"*n)


staircase(20)