'''3. Find the sum of the first 10 numbers that are divisible by 3 and 9.
Sample Output
495'''

i = 0
mul = 9
b = 0
while i < 10:
    i += 1
    a = mul * i
    b += a
print(b)
