'''Write a function in Python that is provided a positive integer. The function returns a list of lists with the
first sub-list containing the even numbers up to that integer and the second sub-list containing the odd
numbers up to that integer.
Example:
Sample Input: 5
Expected output: [ [2, 4], [1, 3, 5] ]'''

num = int(input("Enter number: "))
l = [[],[]]

for i in range(1, num+1):
    if i%2 == 0:
        l[0].append(i)
    if i%2 != 0:
        l[1].append(i)
print(l)
        
