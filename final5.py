'''4. Write a function that takes unsorted list as a parameter and return a sorted list in descending
order (Donot use any built-in function)'''
    

a = [20,33,1,3,5,2]
x = len(a)
dec=[]
max = a[0]

for j in range(x):
    for i in a:
        if i > max:
            max = i
    dec.append(max)
    a.remove(max)
    if a != []:
        max = a[0]
print(dec)