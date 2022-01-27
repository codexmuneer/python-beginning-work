'''Write a Python program that requests five integer values from the user. It then prints one of
two things: if any of the values entered are duplicates, it prints "DUPLICATES"; otherwise, it
prints "ALL'''

a=int(input("Enter value one: "))
b=int(input("Enter value two: "))
c=int(input("Enter value three: "))
d=int(input("Enter value four: "))
e=int(input("Enter value five: "))

if   a==b or a==c or a==d or a==e:
      print('duplicate')
elif b==a or b==c or b==d or b==e:
      print('duplicate')
elif c==b or c==a or c==d or c==e:
      print('duplicate')
elif d==a or d==b or d==e or d==e:
      print('duplicate')
elif e==a or e==b or e==c or e==d:
    print('duplicate')
else:
    print("all")