"""
# If statement
#example 1
x = 100
y = 300

if x < y:
    print("x is less than y")

#example 2

num = 3 
if num > 0:
    print(num,"is a positive number")
print("This is always printed")

num = -1
if num > 0:
    print(num,"is a positive number. ")
print("This is always also printed")


#example 3

num = 3

if num >= 0:
    print("Positive or Zero")

else:
    print("Negative number")



#example 4

num = 5 

if num > 0:
    print("Positive number")

elif num == 0:
    print("Zero")

else:
    print("Negative number")
    
    

# example 5

num = float(input("enter a number: "))
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("positive number")
    
else:
    print("Negative number")
     
# example 6

marks = int(input("Enter the marks? "))
if marks > 85 and marks <= 100:
    print("congrats ! you scored grade A .....")

elif marks > 60 and marks <= 85:
     print("you scored grade B+ .....")
elif marks > 40 and marks <= 60:
     print("you scored grade B .....")
elif marks > 30 and marks <= 40:
     print("you scored grade C .....")

else:
    print("Sorry you are fail ? ")
    
"""
# example 7

age = 18

if ((age >= 8) and (age <= 12)):
    print("you are allowed. welcome !")
else:
    print("Sorry! you are not allowed. Bye!")

""" 
    
"""