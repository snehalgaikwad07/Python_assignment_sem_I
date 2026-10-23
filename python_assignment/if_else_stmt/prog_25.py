#Q25. write a program to check whether a triangle is equilateral,isosceles , or scalene.
side_1 = int(input("Enter first side: "))
side_2 = int(input("Enter second side: "))
side_3 = int(input("Enter third side: "))
if side_1 <= 0 or side_2 <= 0 or side_3 <= 0 or side_1 + side_2 <= side_3 or side_1 + side_3 <=              side_2 or side_2 + side_3 <= side_1:
    print("Invalid triangle")
elif side_1 == side_2 == side_3:
    print("Equilateral triangle")
elif side_1 == side_2 or side_2 == side_3 or side_1 == side_3:
    print("Isosceles triangle")
else:
    print("Scalene triangle")