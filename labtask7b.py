'''Question # 02
Write a program that examines three variables—x, y, and z—and
prints the largest odd number among them. If none of them are odd, it should
print a message to that effect.
Note: You have to take three values from user.'''


x = int(input("Enter first value: \n"))
y = int(input("Enter second value: \n"))
z = int(input("Enter third value: \n"))

if x%2 and y%2 and z%2 != 0:
    if x >= y and x >= z:
        print("greatest odd number is : ", x)
    elif y >= x and y >= z:
        print("greatest odd number is : ", y)
    else:
        print("greatest odd number is : ", z)

elif x%2 != 0 and y%2 == 0 and z%2 == 0:
    print("greatest odd number is : ", x)

elif x%2 == 0 and y%2 != 0 and z%2 == 0:
    print("greatest odd number is : ", y)
    
elif x%2 == 0 and y%2 == 0 and z%2 != 0:
    print("greatest odd number is : ", z)
    
elif x%2 != 0 and y%2 != 0 and z%2 == 0:
    if x >= y:
        print("greatest odd number is : ", x)
    else:
        print("greatest odd number is : ", y)

elif x%2 != 0 and y%2 == 0 and z%2 != 0:
    if x >= z:
        print("greatest odd number is : ", x)
    else:
        print("greatest odd number is : ", z)
        
elif x%2 == 0 and y%2 != 0 and z%2 != 0:
    if y >= z:
        print("greatest odd number is : ", y)
    else:
        print("greatest odd number is : ", z)
        
else:
    print("None of them are odd") 
    