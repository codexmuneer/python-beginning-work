'''Write a function that takes a number as a parameter and prints whether the number is a special number or
not. A number is a special number, if we take the square of number and the sum of the digits in the square
is equal to original number itself. If the number passed to the function is a special number, your function
should print ”It is a special number” otherwise it should print “Not a special number”.'''

def special_num(x):
    y = x*x
    q = y%10
    s = 0
    while y >  0:

        y //= 10
        s += y
        
    z = q + s       
                
    if  z == a:
        print("it's special number")
    else:
        print("it's not a special number")


a = int(input("Enter your number here: "))
b = special_num(a)
