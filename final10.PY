matrixR = []
column = []
nrows = int(input("nRows = "))
ncolumns = int(input("nColumns = "))

for i in range(nrows):
    for j in range(ncolumns):
        column.append(int(input("Enter your matrix elements: ")))
    matrixR.append(column)
    column = []
        
print(matrixR)
a = len(matrixR)
b = len(matrixR[0])
x = 0
y = 0
z = 0
for i in range(a):
    for j in range(b):
        if i == 0:
            x += matrixR[i][j]
            z += matrixR[j][i]
        if i == 1:
            y += matrixR[i][j]
        
            
if x == (y,z):
    print("Magic Matrix")
else:
    print("not a magic matrix")