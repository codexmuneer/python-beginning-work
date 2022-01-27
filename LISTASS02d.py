'''A “Perfect” number is a positive whole number that is the sum of its proper divisors (including 1 and
excluding the number itself). For example, the proper divisors of 6 are 1, 2, 3 and 1 + 2 + 3 =
6. So, 6 is a perfect number. Similarly, 28 is also a perfect number.
Write a program that displaysfirst 4 perfect numbers.'''

# defining function for finding it's factor than adding which is it's divisor
def find_perfect(a): 
    sum = 0
    for i in range(1,a):
        if a % i == 0:
            sum += i
    if sum == a:
        return a


    
num = int(input("enter your number to check : "))   
add = 1
i = 1
while add <= num: # to check many times
    if find_perfect(i) == i: # finding number which is equal to i that is divisor and also addition of itself
        print(i)
        add += 1
    i += 1