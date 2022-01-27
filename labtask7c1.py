'''Modify a calculator you made in the last lab. This time your function ask user to
enter the number and the operation you want to perform (+,-,*,/) after the
operation is performed your program should ask the user whether you want to
continue (Y/N)? your program will exit only when user enter “N”
Hint: use while loop.'''

"""Calculator"""

add = 1
sub = 2
mul = 3
div = 4
input_value = 0

while input_value !='N':
    
    num1 = float(input("Enter  first Number: \n"))
    num2 = float(input("Enter  second Number: \n"))



    print("for addition press ", add )
    print("for subtraction press  ", sub)
    print("for multiplication press  ", mul )
    print("for division press  ", div )

    operator = float(input("Enter your operator: \n"))

    if operator == 1:
        print("Addition: ", num1 + num2)

    elif operator == 2:
        print("Subtraction: ", num1 - num2)

    elif operator == 3:
        print("Multiplication: ", num1 * num2)

    elif operator == 4:
        print("Division: ", num1 / num2)
    
    else:
        print("ERROR!!!!!!")
    print("whether you want to continue (Y/N)?")    
    input_value = str(input())
