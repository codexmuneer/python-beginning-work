'''Write a function that takes the values of two sides of a right triangle and then
determine the size of the hypotenuse. The formula for finding the hypotenuse is
                hyp = sqrt(a^2 + b^2)
You should ask user to enter the two sides of a rectangle (outside the function and pass its
values to function) Function should have default arguments set to 1, 1
Hint: (import math library and use sqrt() built-in function to calculate square root).'''

import math

def size_of_hyp(x = 1, y = 1):
    
    hyp = math.sqrt(x**2 + y**2)
    print("The size of the hypotenous of this triangle is: ", hyp)
    


side1 = float(input("Enter value of side 1: "))
side2 = float(input("Enter value of side 2: "))      
size_of_hyp(side1,side2)


    


