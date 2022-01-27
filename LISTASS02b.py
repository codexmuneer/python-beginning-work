'''Question # 04
Write a Python function to construct the following pattern, using a loop.'''



x =int(input("Enter your number to print the diamond of it : "))
# TO PRINT HALF OF PYRAMID
for i in range(x,0,-1):  
    for j in range(i):
        print("",end=' ')  # FOR SPACES
    for k in range(x+1,i,-1):
        print(x-i,end=" ") # FOR PRINT NUMBER AFTER SPACES
    print()
# TO PRINT PYRAMID IN REVERSE ORDER
for i in range(x+1):
    for j in range(i):
        print("",end=' ')
    for k in range(x+1,i,-1):
        print(x-i,end=" ")
    print()
# BY COMBINING BOTH IT WILL DIAMOND SHAPE