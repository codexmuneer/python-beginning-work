'''Write a function that takes two numbers as an argument and return their LCM.'''


def lcm(x,y):
    
   if x >= y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm
        


x = int(input("Enter a no: "))
y = int(input("Enter a no: "))

print("The LCM is ",lcm(x,y))
