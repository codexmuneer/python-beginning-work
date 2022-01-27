'''7.Shipping Charges
The Fast Freight Shipping Company charges the following rates:

Weight of Package Rate per Pound
2 pounds or less $1.50
Over 2 pounds but not more than 6 pounds $3.00
Over 6 pounds but not more than 10 pounds $4.00
Over 10 pounds $4.75

Write a program that asks the user to enter the weight of a package and then displays the shipping
charges.'''

a=int(input("Enter the  weight of the  package: "))
if a==0:
    print("NONE")
elif a<=2:
    print("$",a*1.50)
elif a>2 and a<=6:
    print("$",a*3.00)
elif a>6 and a<=10:
    print("$",a*4.00)
else:
    print("$",a*4.75)