'''Write a function that takes two numbers as an argument and return their HCF
(Highest Common Factor) /GCD (Greatest Common Divisor).'''

def calculate_hcf(x,y):
    if y == 0:
        return x
    return calculate_hcf(y, x%y)


x = int(input("Enter a no: "))
y = int(input("Enter a no: "))

print("The hcf is", calculate_hcf(x,y))