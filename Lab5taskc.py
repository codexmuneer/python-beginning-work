# Writes a function that takes seconds as a input and displays the time  in hours, min , second
#eg. if the user input 3700 s it should display 1 hour 1 min and 40 sec

def time(sec):
    
    sec1 = int(sec / 3600)
    sec2 = int((sec % 3600)/60)
    sec3 = int((sec % 3600)%60)
    
    print(sec1,"hour", sec2,"min and ", sec3,"seconds")
    

sec = int(input("Enter given seconds: "))
time(sec)