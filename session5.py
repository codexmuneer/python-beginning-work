'''write a program to check a character is uppercase or lowercase'''


'''
fog = str(input("Enter any alphabet: "))
if fog.islower():
    print("Lower case")
else:
    print("upper case")
'''
ch=input("Please enter a character: ")
if(ch>='A' and ch<='Z'):
    print(ch," is an uppercase letter")
elif (ch>='a' and ch<='z'):
    print(ch," is a lowercase letter")
else:
    print(ch," is not in Alphabet")

    
