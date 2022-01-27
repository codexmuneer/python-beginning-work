'''Write a program that computes the product of any two matrices entered by the user. Your
program should check if the two matrices are multipliable or not. In case of non-multipliable
matrices, the program should display a proper message and prompt the user to reinter matrices
with proper dimensions.
Note: Do not use built-in function for matrix multiplication'''
'''The product of two matrices can be computed by multiplying elements of the first row of the first matrix with the first column of the second matrix then,add all the
product of elements.Continue this process until each row of the first matrix is multiplied with each column of the second matrix.'''

'''[1 2 3]   [1 2 3] (0,1) 0 is row amd 1 is column
   [4 5 6] x [4 5 6]
   [7 8 9]   [7 8 9]  '''
   
row1 = []
column1 = []
row2 = []
column2 = []
mat1c = 0
mat2r = 1
x = 0
sr = []
while mat1c != mat2r:   
    mat1r = int(input("Enter the number of rows of matrix 1: "))
    mat1c = int(input("Enter the number of columns of matrix 1: "))
    mat2r = int(input("Enter the number of rows of matrix 2: "))
    mat2c = int(input("Enter the number of columns of matrix 2: "))
    if mat1c != mat2r:
        print("Error! column of matrix 1 is not equal to rows matrix 2, please re-enter correct rows and columns") 

for i in range(0,mat1r):
    for j in range(0, mat1c):
        column1.append(int(input(f"Enter element of matrix 1 ({i},{j}) ")))
    row1.append(column1)
    column1 = []
for i in range(0,mat2r):
    for j in range(0, mat2c):
        column2.append(int(input(f"Enter element of matrix 2 ({i},{j}) ")))
    row2.append(column2)
    column2 = [] 
    
print(row1 ," x ",row2 )

a = len(row1)
b = len(row2)
c = len(row2[0])    
for m in range(a): # 2 rows to 2 bar
    for n in range(c):  # 3 column to 3 bar
        for o in range(b):
            x += row1[m][o]*row2[o][n]
            sr.append(x)
            x = 0
    #    print(sr)
        

print(sr)

