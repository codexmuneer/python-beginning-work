'''2. Write a Python program to create the multiplication table (from 1 to
10) of a number.'''


print("######### Multiplication table maker ########")

num = int(input("Enter the number to print table of it: "))
i = 0
n = 10
while i < n:
    
    i += 1
    a = num * i
    print(num,"x", i ,"=", a)

