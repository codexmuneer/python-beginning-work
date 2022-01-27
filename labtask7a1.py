#1. Write a function that takes one number as an argument and return their factorial.

def factorial(x):
    fact = 1
    i = 1
    while i <= x:
        fact *= i
        i += 1
    print("the fatorial is: ", fact)
  
num = int(input("Enter your number: "))
factorial(num)
