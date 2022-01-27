''' Write a program that accepts an integer and displays its factors. For example, if the
user enters 12, the program should display 2, 3, 4 and 6. '''

num = int(input("Enter your number which you wanna know it's factor: "))
i = 1

while i <= num:
    x = num % i
    if x == 0:
        y = num/i
        print(y)    
    i += 1 
    
