"""Write a program that takes two variable x and y from user and pass these two values  to a  functio named largest_odd(user)
your function should print largest odd numberr betweenthem, if none of them are odd, it shoul print a message to that effect"""

def largest_odd(x,y):
    
    if x%2 and y%2 != 0:
        if x > y:
            print("x =", x ,"is greatest odd number between them")
        else:
            print("y =", y ,"is greatest odd number between them")  
             
    elif x % 2 == 0 and y % 2 != 0:
        print(y,"is greatest odd number")
        
    elif x % 2 != 0 and y % 2 == 0:
        print(x,"is greatest odd number")
                         
    else:
        print("None of them are odd")       
            
x = int(input("Enter x: "))
y = int(input("Enter y: "))

largest_odd(x,y)