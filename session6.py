'''combination of numbers'''

#n = int(input("Enter numbers: "))
a = 0
for i in range(1,4):
    for j in range(1,4):
        for k in range(1,4):
            if i != j and j != k and i != k:
                print(i,j,k)
                a += 1

print(a)






'''
a = 3 
b = 2

while a>0:
    b = a
    while b > 0:
        print("value of a is ",a," and b is ",b)
        b -= 1
    a -= 1
'''