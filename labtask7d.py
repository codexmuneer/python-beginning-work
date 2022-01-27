'''
Question # 04
Build a GPA calculator that inputs grades of 3 different subjects along with the credit hours
from the user and displays the user’s GPA. The input grades and their corresponding grading
points are given below.
Grade Points
A 4.0
A- 3.67
B+ 3.33
B 3.0
B- 2.67
C+ 2.33
C 2.0
C- 1.67
D+ 1.33
D 1.0
F 0

The formula is
gpa = (gp1 * ch1 + gp2 * ch2 + gp3 * ch3)/ (ch1 + ch2 + ch3)
Where GP1 is Points of Subject 1 and CH1 show credit hours of subject 1.
'''
print("############################.....GPA CALCULATOR......###################\n")


i = 0
a,b,c,d,e,f,g,h,m,j,k = 4.0,3.67,3.33,3.0,2.67,2.33,2.0,1.67,1.33,1.0,0
total_gpa = 0.0
total_ch = 0

while i < 3 :
    
    gpa = input(f"please enter your grade in subject {i + 1} : \n").lower()
    ch = int(input(f"Please enter the credits hours of subject {i + 1} : \n"))
       
    if gpa == ('a'):
        gpa = a * ch
    elif gpa == ('a-'):
        gpa = b * ch

    elif gpa  == ('b+'):
        gpa = c * ch

    elif gpa == ('b'):
        gpa = d * ch
  
    elif gpa == ('b-'):
        gpa = e * ch
           
    elif gpa == ('c+') :
        gpa = f * ch 
        
    elif gpa == ('c') :  
        gpa = g * ch

    elif gpa == ('c-') :
        gpa = h * ch

    elif gpa == ('d+') :
        gpa = k * ch
 
    elif gpa == ('d'):
        gpa = j * ch
        
    elif gpa== ('k'):
        gpa = k * ch
  
    
    total_gpa = total_gpa + gpa 
    total_ch = total_ch + ch      
    i = i + 1
        
        
total = total_gpa / total_ch
print("Your GPA is: ",total)     

