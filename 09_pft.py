# create differnt triangle shapes using loops
#-------------> right angle triangle
'''n = int(input("Enter your number to print triangle of it: ")) 
for i in range(0,n):
    for j in range(0,i+1):
        print("*", end='')
    print()'''
#--------------> downward rightangle triangle   
'''n = int(input("Enter your number to print triangle of it: ")) 
for i in range(n,0,-1):
    for j in range(i):
        print("*", end='')
    print()'''

# samosa
'''n = int(input("Enter your number to print triangle of it: "))

for i in range(0,n):
    for j in range(0,i+1):
        print("*", end='')
    print()
if i == j:
    for i in range(n-1,0,-1):
        for j in range(i):
            print("*", end='')
        print()
else:
    print("error")'''
    

n = int(input("Enter your number to print triangle of it: "))

for i in range(0,n):
    for j in range(i):
        for k in range(j):
            print("*", end='')
        print()