'''Write a python program that prints the following patterns separately one below the other.
Use nested for loop to generate the patterns.'''

for i in range(0,7):
    for j in range(0,i+1):
        print("*", end='')
    print()
print()
for i in range(7,0,-1):
    for j in range(i):
        print("*", end='')
    print()
print()   
for i in range(1,7):
    for j in range(6,i,-1):
        print(" ", end='')
    for k in range(0,i):
        print("*", end='')
    print()
print() 
for i in range(7,0,-1):
    for j in range(i,7):
        print(" ", end="")
    for k in range(0,i):
        print("*", end="")
    print()    
