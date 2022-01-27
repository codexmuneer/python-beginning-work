'''1. Write a Python program that requests five integer values from the user. It then prints the
maximum and minimum values entered. If the user enters the values 3, 2, 5, 0, and 1, the
program would indicate that 5 is the maximum and 0 is the minimum. Your program should
handle ties properly; for example, if the user enters 2, 4 2, 3 and 3, the program should report 2
as the minimum and 4 as maximum.'''

num1 = int(input("Enter value one : "))
num2 = int(input("Enter value two : "))
num3 = int(input("Enter value three : "))
num4 = int(input("Enter value four : "))
num5 = int(input("Enter value five : "))


if num1>=num2 and num1>=num3 and num1>=num4 and num1>=num5:
    if num2<=num1 and  num2<=num3 and num2<=num4 and num2<=num5:
        print(num1,"is the maximum and ",num2,"is the minimum")
    elif num3<=num1 and num3<=num2 and num3<=num4 and num3<=num5:
        print(num1,"is the maximum and ",num3,"is the minimum")
    elif num4<=num1 and num4<=num2 and num4<=num3 and num4<=num5:
        print(num1,"is the maximum and ",num4,"is the minimum")
    elif num5<=num1 and num5<=num2 and num5<=num4 and num5<=num3:
        print(num1,"is the maximum and ",num5,"is the minimum")

elif num2>=num1 and num2>=num3 and num2>=num4 and num2>=num5:
    if num1<=num2 and  num1<=num3 and num1<=num4 and num1<=num5:
        print(num2,"is the maximum and ",num1,"is the minimum")
    elif num3<=num1 and num3<=num2 and num3<=num4 and num3<=num5:
        print(num2,"is the maximum and ",num3,"is the minimum")
    elif num4<=num1 and num4<=num2 and num4<=num3 and num4<=num5:
        print(num2,"is the maximum and ",num4,"is the minimum")
    elif num5<=num1 and num5<=num2 and num5<=num3 and num5<=num4:
        print(num2,"is the maximum and ",num5,"is the minimum")

elif num3>=num1 and num3>=num2 and num3>=num4 and num3>=num5:
    if num1<=num2 and  num1<=num3 and num1<=num4 and num1<=num5:
        print(num3,"is the maximum and ",num1,"is the minimum")
    elif num2<=num1 and num2<=num3 and num2<=num4 and num2<=num5:
        print(num3,"is the maximum and ",num2,"is the minimum")
    elif num4<=num1 and num4<=num2 and num4<=num3 and num4<=num5:
        print(num3,"is the maximum and ",num4,"is the minimum")
    elif num5<=num1 and num5<=num2 and num5<=num3 and num5<=num4:
        print(num3,"is the maximum and ",num5,"is the minimum")
        
elif num4>=num1 and num4>=num2 and num4>=num3 and num4>=num5:
    if num1<=num2 and  num1<=num3 and num1<=num4 and num1<=num5:
        print(num4,"is the maximum and ",num1,"is the minimum")
    elif num2<=num1 and num2<=num3 and num2<=num4 and num2<=num5:
        print(num4,"is the maximum and ",num2,"is the minimum")
    elif num3<=num1 and num3<=num2 and num3<=num4 and num3<=num5:
        print(num4,"is the maximum and ",num3,"is the minimum")
    elif num5<=num1 and num5<=num2 and num5<=num3 and num5<=num4:
        print(num4,"is the maximum and ",num5,"is the minimum")
        
elif num5>=num1 and num5>=num2 and num5>=num3 and num5>=num4:
    if num1<=num2 and  num1<=num3 and num1<=num4 and num1<=num5:
        print(num5,"is the maximum and ",num1,"is the minimum")
    elif num2<=num1 and num2<=num3 and num2<=num4 and num2<=num5:
        print(num5,"is the maximum and ",num2,"is the minimum")
    elif num3<=num1 and num3<=num2 and num3<=num4 and num3<=num5:
        print(num5,"is the maximum and ",num3,"is the minimum")
    elif num4<=num1 and num4<=num2 and num4<=num3 and num4<=num5:
        print(num5,"is the maximum and ",num4,"is the minimum")
        
else:
    print("INVALID NUMBER!!!!!!!!")
        
        









# if num1 >= num2 and num1 >= num3 and num1 >= num4 and num1 >= num5:
#     higher = num1

# elif num2 >= num1 and num2 >= num3 and num2 >= num4 and num2 >= num5:
#     higher = num2

# elif num3 >= num1 and num3 >= num2 and num3 >= num4 and num3 >= num5:
#     higher = num3
    
# elif num4 >= num1 and num4 >= num2 and num4 >= num3 and num4 >= num5:
#     higher = num4
    
# elif num5 >= num1 and num5 >= num2 and num5 >= num3 and num5 >= num4:
#     higher = num5


# if num1 <= num1 and num1 <= num2 and num1 <= num3 and num1 <= num4:
#     lower = num1 

# elif num2 <= num1 and num2 <= num2 and num2 <= num3 and num2 <= num4:
#     lower = num1 

# elif num3 <= num1 and num3 <= num2 and num3 <= num4 and num3 <= num3:
#     lower = num1 
    
# elif num4 <= num1 and num4 <= num2 and num4 <= num3 and num4 <= num4:
#     lower = num1 

# elif num5 <= num1 and num5 <= num2 and num5 <= num3 and num5 <= num4:
#     lower = num1 

# print(higher, "is the maximum number and ",lower,"is the minimum number")
        
        
        