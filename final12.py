def count():
    fa = open("STORY.TXT", "r")
    d = fa.read()
   # m = d.split()
    countera = 0
    counterb = 0
    for i in d:
        if i in ("A,a"):
            countera += 1
        elif i in ("M,m"):
            counterb += 1
    print("A or a is:", countera , "M or m is: ".strip(), counterb)
    fa.close()
    
count()