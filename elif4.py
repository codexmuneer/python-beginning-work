#[in an Amusement Park]
#Rollercoaster ride:

#step 1: Ask age of the customerw

#step 2: if the customer is below 10 then they are not allowed to ride.

#step 3: if the customer has a height below 5 feet. they are not allowed to ride.

#step 4: if they are below 15 then their ticket price will be 7$, 
# below 18 price will be 10$ and for adult its 15$

#step 5: do they want to get a picture while riding? 
#	if yes, then it will cost +2$ regardless of their age.

#step 6: generate the total bill

print("###################***WELCOME TO AMUSEMENT PARK***################### \n")
print("#################**Roller coaster  ride**################# \n")

age =int(input("Enter Your age: \n"))
height =int(input("Enter Your height: \n"))
capture_pic = int(input("Do you want to capture picture in ride?,if yes press 1: \n"))
p1 = 7
p2 = 10
p3 = 15
extra_cost = 2

a = f"you are not allowed to ride "
b = f"cost {p1}$ \n"
c = f"cost {p2}$ \n"
d = f"cost {p3}$ \n"
e = f"ivalid age!!! \n"
f = f"cost {extra_cost}$ extra \n"
g = f"no picture will be captured during ride \n"

if age < 10  and height < 5:
    print(a)
elif age < 15 :
    total_bill = p1
    print(b)
elif age < 18 :
    total_bill = p2
    print(c)
elif age > 18 :
    total_bill = p3
    print(d)
else :
    print(e)
    
if capture_pic == 1:
    print(f)
else :
    print(g)
    
if capture_pic == 1 and age:
    total_bill += extra_cost
   # total_bill = total_bill + extra_cost
    print(total_bill)    
else :
    print(total_bill)


