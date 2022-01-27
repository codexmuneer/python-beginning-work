'''write a program using ifelse that takes 4-digit number and output in reverse order example; 1234 as input and returns 4321 '''

num = int(input("Enter number to get it's reverse order: "))
if num > 999 and num < 10000:
    num1 = num // 1000
    rem1 = num % 1000
    num2 = rem1 // 100
    rem2 = rem1 % 100
    num3 = rem2 // 10
    rem3 = rem2 % 10

    formula = (rem3*1000)+(num3*100)+(num2*10)+num1

    print(formula)

else:
    print("input should be 4-digit only")