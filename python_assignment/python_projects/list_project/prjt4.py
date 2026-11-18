#****************** Multi-Criteria Student Ranking Tool*****************


stu = [
    ["Amit", 8.5, 90],
    ["Sneha", 9.2, 85],
    ["Rahul", 8.5, 95],
    ["Priya", 9.2, 92],
    ["Karan", 7.8, 80]
]

print("1. Sort by CGPA")
print("2. Sort by Attendance")
print("3. Sort by Name")
print("4. Sort by CGPA, Attendance and Name")

ch = int(input("Enter your choice: "))

sort = {
    1: lambda x: -x[1],
    2: lambda x: -x[2],
    3: lambda x: x[0],
    4: lambda x: (-x[1], -x[2], x[0])
}

if ch in sort:
    lst = sorted(stu, key=sort[ch])

    print("*** Student Ranking ***")
    print("Name\tCGPA\tAttendance")

    for i in lst:
        print(i[0], "\t", i[1], "\t", i[2], "%")
else:
    print("Invalid choice!")