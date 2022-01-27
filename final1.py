'''Consider a file containing your name and roll number. Write a program that reads the data from the file and
counts number of times each character appears in the file.
Example: If a file data.txt contains the following text:
Ali Ahmad p20010'''

f = open("data.txt","w")
f.write("Ali Ahmad p20010")
f.close()

f = open("data.txt","r")
a = f.read()
counter = 0
for i in a:
    print(i," appeared ", a.count(i), " times")
    counter += 1

print("total characters in a file is ", counter)
    
f.close()       