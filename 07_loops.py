'''n = 0
while n<5:
    print("Hello world")
    n += 1 #incrementing 1
    
print("out of loop")

i = 0
n = 10
while i <= n:
    print(i)
    i += 1 #increamnet i by 1
    
  
# program to sum of natural number 

sum = 0
i = 1
n = int(input("Enter any natural num to print the sum upto it: "))
while i <= n:
    sum = sum + i
    i = i + 1 # update counter
    
print("the sum is", sum)


#sum of even  numbers
sum  = 0 
i = 1
while i <= 10:
    if i%2==0:
        sum += i
    i += 1
print(sum)    

# sum of natural number until press q by user
#atm card example

sum = 0
input_value = 0
while input_value != 'q':
    sum += int(input_value)
    print("Sum = ", sum)
    print("Enter the new number to add or press q to quit the program")
    input_value = input()

# break and continue 
i = 1
while i < 10:
    if i == 5:
        break
    print("NUMBER is ",i) 
    i += 1
    
print("out of loop") 
'''
i = 1
while i < 10:
    if i == 5:
        continue
    print("NUMBER is ",i) 
    i += 1
    
print("out of loop")     

     
    
