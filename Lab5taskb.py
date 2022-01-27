# write a function that takes the two numbers and perform all arthimetic operations 
# functions should have default arguments set to 1,1 
# add sub mult div

def all_ops(num1=1,num2=1):
    ADD = num1 + num2
    SUB = num1 - num2
    MUL = num1 * num2
    DIV = num1 / num2
    print("The sum of given numbers is: ", ADD)
    print("The subtraction of given numbers is: ", SUB)
    print("The multiplication of given numbers is: ", MUL)
    print("The division of given numbers is: ", DIV)
    
    return ADD,SUB,MUL,DIV

num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))
result = all_ops(num1, num2)


   
 