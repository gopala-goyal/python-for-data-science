names =  list(input("Enter the names of students: ").split(','))
assignments =  list(input("Enter the number of assignments: ").split(','))
grades =  list(input("Enter the grade: ").split(','))

# message string to be used for each student
# HINT: use .format() with this string in your for loop
message = "Hi {},\n\nThis is a reminder that you have {} assignments left to submit before you can graduate. You're current grade is {} and can increase to {} if you submit all assignments before the due date.\n\n"

# write a for loop that iterates through each set of names, assignments, and grades to print each student's message
for i in range(len(names)):
    grade = int(grades[i]) + (2*int(assignments[i]))
    print(message.format(names[i], assignments[i], grades[i], grade))
