"""Write a program to check a triangle is equilateral, isoceles or scalene. YOUR PROGRAM SHOULD ASK THE USER TO INPUT X,Y,Z VALUES
note: equilateral = 3 sides equal
isoceles = 2 sides  equal
scalene = all side unequal"""

x = int(input("Enter value of side first: "))
y = int(input("Enter value of side second: "))
z = int(input("Enter value of side third: "))

if x == y == z:
    print("It is Equaliteral triangle. ")
    
elif x == y or x == z or y == z:
    print("It is Isoceles triangle. ")

else:
    print("It is Scalene triangle. ")
    