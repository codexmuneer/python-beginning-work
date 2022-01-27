'''A palindrome is nothing but any number or a string which remains unaltered when reversed.

Example: 12321
Output: Yes, a Palindrome number

Example: RACECAR
Output: Yes, a Palindrome string
first make it for int and than  string'''
'''
#for integers
num = int(input("Enter your value to know it's palindrome or not: "))
temp = num
rev = 0
while num > 0:
    rem = num % 10
    rev = rev*10 + rem
    num = num//10
if temp == rev:
    print("yes, it's a palindrome number")

else:
    print("it's not a palindrome number")
'''

#for strings
alp = str(input("Enter a word to check it's palindrome or not: "))
w = ""
for i in alp:
    w = i + w
if alp==w:
    print("yes, it's a palindrome")
else:
    print("it's not a palindrome")