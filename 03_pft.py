'''Write a program that takes numbers of seconds as input from user and calculate total number
of hours, minutes and seconds from it. Lets say if user enters 12345 it should display output as:
Hours: 3
Minutes: 25
Seconds: 45'''

a=int(input("Enter Seconds to get output in hours, mins and seconds: \n"))

hours = float(a/3600)
mint=int(a/60)%60
second=(a%60)


print("Hours: ",int(hours))
print("Minutes: ",mint)
print("Seconds: ",second)