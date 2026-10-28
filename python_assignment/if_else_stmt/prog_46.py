#Q46. Write a program to print grade description using match case.
grade=input("Enter your grade (A, B, C, D, F):")
match grade:
    case 'A':
        print("Excellent! You have an A.")
    case 'B':
        print("Good! You have a B.")
    case 'C':
        print("Average! You have a C.")
    case 'D':
        print("Below Average! You have a D.")
    case 'F':
        print("Fail! You have an F.")
    case _:
        print("Invalid grade!")