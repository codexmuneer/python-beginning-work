#shelf will ask your age if age is <= 12 than 30% off and if >= 12 10% off

print("Enter your age: ")
age = int(input())

if age <= 12 :
    print("you have 20 percent off")

elif age > 12 :
    print ("you have 10 percent off")   
    
else :
    print ("invalid age")