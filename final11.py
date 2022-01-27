
def count():
    fa = open("STORY.TXT", "r")
    d = fa.read()
    m = d.split()
    counter = 0
    for i in m:
        if i in ("Me,me,My,my"):
            counter += 1
    print("Count of Me/My: ", counter)
    fa.close()
    
count()



