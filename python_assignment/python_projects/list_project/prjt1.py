#***************** College Attendance Tracker **************************

roll = [1, 2, 3, 4, 5]
name = ["Amit", "Sneha", "Rahul", "Priya", "Karan"]

att = []

n = int(input("Enter number of lectures: "))

for i in range(n):
    lst = []
    print("Lecture", i + 1)

    for j in range(len(roll)):
        a = input(name[j] + " (P/A): ").upper()
        lst.append(a)

    att.append(lst)

print("--- Attendance Sheet ---")

defaulter = []

for i in range(len(roll)):
    p = 0

    for j in range(n):
        if att[j][i] == "P":
            p = p + 1

    per = (p / n) * 100

    print(name[i], ":", p, "/", n, "=", round(per, 2), "%")

    if per < 75:
        defaulter.append([name[i], per])

defaulter.sort(key=lambda x: x[1])

print("--- Defaulter List ---")

for i in defaulter:
    print(i[0], "-", round(i[1], 2), "%")

f = open("attendance.txt", "w")

f.write("--- Attendance Sheet ---\n")

for i in range(len(roll)):
    p = 0

    for j in range(n):
        if att[j][i] == "P":
            p = p + 1

    per = (p / n) * 100

    f.write(name[i] + " : " + str(p) + "/" + str(n) + " = " + str(round(per, 2)) + "%\n")

f.write("--- Defaulter List ---\n")

for i in defaulter:
    f.write(i[0] + " - " + str(round(i[1], 2)) + "%\n")

f.close()

print("Attendance saved in attendance.txt")