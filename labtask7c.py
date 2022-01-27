'''Write a program that check whether a year is leap year or not? create a function named
isLeap has an formal parameter, year, determines whether the year is a leap year, or not and
print the message to that effect. A year is a leap year if it is divisible by 4 but is not divisible
by 100 except when divisible by 400.
You should ask user to enter year (outside the function and pass its value to function)
Reflect the concept of required argument
Hint :(use conditional statements)
For example,
• 1999 is not a leap year
• 2000 is a leap year
• 2004 is a leap year
• 1000 is not a leap year '''

def isleap(year):

    if(year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0):
        print("it is leap year ") 

    else:
        print("It's not a leap year")
    


year = int(input("Enter year to check if it is leap or not: "))
isleap(year)