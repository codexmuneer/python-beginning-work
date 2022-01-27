'''Write a Program to Calculate Permutation(nPr) for given values of n and r
The nPr (permutation) formula is:
   p(n,r)= n!/(n-r)!'''

   
def n_fact(n):
    i = 1
    fact = 1
    while i <= n:
        fact *= i
        i += 1
    return fact

n = float(input("Enter the value for n: "))
r = float(input("Enter the value for n: "))
f = n-r
p = n_fact(n)
i = n_fact(f)

permutation = p/i
print("npr for n = ",n,"and r =",r,"is: ", permutation)





