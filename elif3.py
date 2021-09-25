#For example, lets say you are recording the score for a certain course.
# The total score is 100, with 50 points for the theoritical work and 50 for practical.
# You want to display an error message or warning if the score exceeds 100


#score = 100
#theoritical_work= 50
#practical_work = 50

theoritical_work = int( input("enter theoritical work points"))
practical = int(input("enter practical points"))
score = theoritical_work + practical
if score > 100 :
   print("warning!! score exceed 100")
else :
   print("your score is:", score)