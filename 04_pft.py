'''5. Age Classifier
Write a program that asks the user to enter a person’s age. The program should display a
message indicating whether the person is an infant, a child, a teenager, or an adult. Following
are the guidelines:
A. If the person is 1 year old or less, he or she is an infant.
B. If the person is older than 1 year, but younger than 13 years, he or she is a child.
C. If the person is at least 13 years old,but lessthan 20 years old, he or she is a teenager.
D. If the person is at least 20 years old, he or she is an adult.'''

a=int(input("Enter your age: "))

if a<1:
    print("infant")
elif  a>=1 and a<=13:
    print("child")
elif  a>13 and a<=20:
    print("teenager")
else:  
    print("adult")