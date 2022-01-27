'''1. The file names.txt contains a list of names, one per line.
a. Write a program that start printing the first 4 character of every
name in a file (names.txt).

b. Write a program that prints the sum of the lengths of the names
in names.txt.
c. Write a program that prints the average of the lengths of the
names in names.txt.
d. Write a program that reads in the names form names.txt and
prints the shortest name along with its length.
e. Write a python function that reads in the names
in names.txt and prints all the names that have the length given
as a parameter e.g print_name(5)'''
# a
# file = open("names.txt", 'r')
# for i in file:
#     i = i.strip()
#     i = i[0:4]
#     print(i)
# file.close()

# b
# file = open("names.txt", 'r')
# counter = 0
# for i in file:
#     i = i.strip()
#     counter += len(i)
# print(counter)
# file.close()

# #c
# file = open("names.txt", 'r')
# counter = 0
# x = 0
# for i in file:
#     i = i.strip()
#     counter += len(i)
#     x += 1
   
# avg = counter/x   
# print("Average is :", avg)
# file.close()

#d
# file = open("names.txt", 'r')
# first = file.readline()
# a = len(first)
# for i in file:
#     if len(i) < a:
#         print(i)
# file.close()

# e 
# file = open("names.txt", 'r')
# def print_name(x):
#     for i in file:
#         i = i.strip()
#         if len(i) == x :
#             print(i)
# print_name(5)
# file.close()

#f
# file1 = open("names.txt", 'r')
# file2 = open("name_subj.txt", 'w')

# for  line in file1:
#     line = line.strip()
#     a = line + " Programming fundamentals , English , Calculus, Pakistan Studies, Physics"
#     file2.write(a)
#     print(a)
# file1.close
# file2.close

# g

def search_key():
    n = input("Enter name ")
    file = open("names.txt", "r")
    x = file.read()
    if n in x:
        return True
    else:
        return False
    file.close()
        
search_key()

