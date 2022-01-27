'''6. Write a program that takes two numbers from the user and displays all prime numbers
between them. For example, if the user enters 5 and 15, your program should display 5, 7,
11, 13.'''

# num1 = int(input("Enter first number: "))
# #num2 = int(input("Enter Second number: "))

# #for i in range(1,num1):

# if  num1%2 == 0 or num1%3 == 0 or num1%7 == 0:
#     print("not prime number")
#         #break
# else:
#     print("It's a prime:  " )
#         #break

# num = int(input("Enter your number: "))
# i = 0
# prime1 = (num - 1)/6
# prime2 = (num + 1)/6

# if prime1//2 == 0 or prime2%2 == 0:
#     print("it's not prime")
# else:
#     print("it's prime")
num = int(input("Enter your number: "))
counter = 0
for i in range(2,num):
    if num%i == 0:
        print("it's not a prime number")
        break
    else:
        counter += 1
        
if counter >= 1:
    print("it's prime")
    
