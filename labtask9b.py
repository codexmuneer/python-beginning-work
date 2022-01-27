'''2. Write a Python function to construct the following pattern, using a
for loop. User should enter a symbol e.g *,^,@,- etc, and your
function should a pattern like this of that symbol'''

#n = int(input("Enter your number to print triangle of it: "))
symbol = str(input("Enter symbol: "))
for i in range(0,5):
    for j in range(0,i+1):
        print(symbol, end='')
    print()
if i == j:
    for i in range(5-1,0,-1):
        for j in range(i):
            print(symbol, end='')
        print()
else:
    print("error")