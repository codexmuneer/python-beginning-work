'''create a list which contains the first three odd positive integers and a list b which contains the first three even positive integers.
a= [1, 3, 5] b= [2, 4, 6]
● Create a new list c which combines the numbers from both lists (order is unimportant).
● Append 7, 8 and 9 to the end of c.
● Print the first three elements of c.
● Print the last element of b. 
● Print the length of a
● Find the minimum value in list c (Do not use built-in function)
● Find the average/mean value from list c (Donot use built-in function)
● Insert fourth element in list c 42'''

a= [3, 1, 5] 
b= [2, 4, 6]
c= a + b
print(c) #------------> will combine lists of a and b
c.append(7) #------------> will append 7 in end to the list of c 
c.append(8) #------------> will append 8 in end to the list of c
c.append(9) #------------> will append 9 in end to the list of c
print(c) #---> 7,8,9 in end of c list
print(c[0:3]) #-------> first three element of c
print(b[2]) #----------------->last element of b 
print(len(a))#-------------> length of a list

#finding minimum value in list c
less = c[0]
for i in c:
    if i < less:
        less = i
print(less)

#finding average of list c values
avg = 0
for i in c:
    avg += i
print(avg/len(c))

#inserting fourth element in c
c.insert(4,42)
print(c)


