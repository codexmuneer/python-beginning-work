'''Write a Program that takes ‘n’ and ‘x’ from user and computes the following series.'''

# DEFINING FACTORIAL FUNCTION
def n_fact(a):
    i = 1
    fact = 1
    while i <= a:
        fact *= i
        i += 1
    return fact

n = int(input("Enter the value of n: "))
x = int(input("Enter the value of x: "))
sum_of_series = 1 # PUTTING 1 CUZ FOR O! = 1 ALSO X^0 == 1

for  k in range(1,n+1):
    
    s = (x**k)/(n_fact(k))    # SOLVING EQUATION
    sum_of_series += s     # SUMMATION OF SERIES USING THIS
    
print("RESULT = ", sum_of_series)