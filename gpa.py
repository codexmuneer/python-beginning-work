totalGrade = 0.0
totalCredit = 0
i = 0

while i < 3:
    grade = input(f"Input your grade for Subject {i+1}: ").lower()
    credit = int(input(f"Enter credit hours for Subject {i+1}: "))

    if grade == 'a' or grade == 'a+':
        total = 4.0 * float(credit)
    elif grade == 'a-':
        total = 3.67 * float(credit)
    elif grade == 'b+':
        total = 3.33 * float(credit)
    elif grade == 'b':
        total = 3.0 * float(credit)
    elif grade == 'b-':
        total = 2.67 * float(credit)
    elif grade == 'c+':
        total = 2.33 * float(credit)
    elif grade == 'c':
        total = 2.0 * float(credit)
    elif grade == 'c-':
        total = 1.67 * float(credit)
    elif grade == 'd+':
        total = 1.33 * float(credit)
    elif grade == 'd':
        total = 1.0 * float(credit)
    else:
        total = 0.0 * float(credit)

    totalGrade = totalGrade + total
    totalCredit = totalCredit + credit

    i = i+1

gpa = totalGrade / totalCredit
print(f"Your gpa is: {gpa}")
