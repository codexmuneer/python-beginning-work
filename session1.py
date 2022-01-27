'''Write a function isdivisible that two argumnet that takes two argument returns true or false indicate that first parameter is 
divisible by other or not'''

def indivisible(a,b):
    if a%b == 0:
        print(a," is divisible by ",b)
    
    else:
        print(a," is not divisible by ", b)
        
        
indivisible(9,2)