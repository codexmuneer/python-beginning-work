'''4. Write a Python function to construct the following pattern, using a
for loop. User should enter a symbol e.g *,^,@,- etc, the number of rows and your
function should a pattern like this of that symbol.'''

n = int(input("Enter the number of rows: "))
# symbol = str(input("Enter symbol: "))

for i in range(0,n+1):
    for j in range(n,0,-1):
        if i >= j:
            print(i," " , end="")
        else:
            print(" ", end="")
    print()