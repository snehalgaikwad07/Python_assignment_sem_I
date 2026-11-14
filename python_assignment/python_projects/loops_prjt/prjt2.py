#*************** Student marks and grade report ********************
n = int(input("Enter number of students: "))

total = 0
pass_count = 0
fail_count = 0

for i in range(1, n + 1):

    print("\nEnter details of Student", i)

    name = input("Enter student name: ")
    marks = float(input("Enter marks out of 100: "))

    if marks >= 0 and marks <= 100:

        total = total + marks

        if marks >= 75:
            grade = "A"
        elif marks >= 60:
            grade = "B"
        elif marks >= 50:
            grade = "C"
        elif marks >= 40:
            grade = "D"
        else:
            grade = "Fail"

        print("Student Name:", name)
        print("Marks:", marks)
        print("Grade:", grade)

        if marks >= 40:
            pass_count = pass_count + 1
        else:
            fail_count = fail_count + 1

    else:
        print("Invalid Marks! Enter marks between 0 and 100.")

# Calculate average
valid_count = pass_count + fail_count

if valid_count > 0:
    average = total / valid_count
    print("\n----- Class Performance  -----")
    print("Class Average:", average)
    print("Pass Count:", pass_count)
    print("Fail Count:", fail_count)
else:
    print("No valid student marks entered.")
