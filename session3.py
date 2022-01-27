'''take input for user as string and check how many  vowels are there in:'''


word = str(input("Enter you sentence to know how many vowels present in it: ")).lower()
counter = 0
 
for i in word:
    if i in ("a,e,i,o,u"):
            counter += 1
    
print(counter)    
    