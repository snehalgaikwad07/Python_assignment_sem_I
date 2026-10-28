#Q48. Write a program to print language choice using match case
language=input("Enter your language choice(Python,c ,c++,Java):" )
match language:
    case 'python':
        print("You have selected Python")
    case 'c':
        print("You have selected c.")
    case 'c++':
        print("You have selected c++.")
    case 'java':
        print("You have selected java.")
    case _:
        print("Invalid language!")