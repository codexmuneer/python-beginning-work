"""Calculator"""
num1 = float(input("Enter  first Number: \n"))
num2 = float(input("Enter  second Number: \n"))

add = 1
sub = 2
mul = 3
div = 4

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