#***************** College Attendance Tracker **************************

roll = [1, 2, 3, 4, 5]
att = []
names = ["Amit", "Sneha", "Rahul", "Priya", "Karan"]

n = int(input("Enter number of lectures: "))

for i in range(n):
    lst = []
    print("\nLecture", i + 1)

    for j in range(len(roll)):
        a = input(names[j] + " (P/A): ").upper()

        if a == "P":
            lst.append("P")
        else:
            lst.append("A")

    att.append(lst)

print("\n--- Attendance Sheet ---")
print("Name\tAttendance")

for i in range(len(roll)):
    p = 0

    for j in range(n):
        p = p + att[j].count("P")

    total = 0
    for j in range(n):
        total = total + att[j][i].count("P")

    per = (total / n) * 100
    print(names[i], "\t", total, "/", n, "\t", round(per, 2), "%")

# Defaulter report
defaulter = []

for i in range(len(roll)):
    total = 0

    for j in range(n):
        total = total + att[j][i].count("P")

    per = (total / n) * 100

    if per < 75:
        defaulter.append([names[i], per])

defaulter.sort(key=lambda x: x[1])

print("\n--- Defaulter Report ---")
print("Students below 75% attendance:")

for i in defaulter:
    print(i[0], "-", round(i[1], 2), "%")

# Save output in text file
f = open("attendance_report.txt", "w")

f.write("--- Attendance Sheet ---\n")
f.write("Name\tAttendance Percentage\n")

for i in range(len(roll)):
    total = 0

    for j in range(n):
        total = total + att[j][i].count("P")

    per = (total / n) * 100
    f.write(names[i] + "\t" + str(total) + "/" + str(n) +
             "\t" + str(round(per, 2)) + "%\n")

f.write("\n--- Defaulter Report ---\n")

for i in defaulter:
    f.write(i[0] + " - " + str(round(i[1], 2)) + "%\n")

f.close()

print("\nReport saved in attendance_report.txt")