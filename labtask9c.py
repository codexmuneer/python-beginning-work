'''Write a program the prompts the user for information for three students. For each student
prompt for the student ID and three quiz grades. Use a nested loop, where the inner loop
prompts for the three quiz grades. Print the student’s name and average – formatted to
two decimal places. View the sample output as a guide.'''

student_score = 0

for i in range(1,4):
    student_name = str(input(f"Enter the name of student {i}: "))
    
    for j in range(1,4):
        
        student_scores = int(input(f"Enter score {j}: "))
        student_score += student_scores
        
    print("Name: ", student_name)
    print("Average: ", round(student_score/3,2))
    if student_score > 0:
        student_score = 0