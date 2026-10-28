#Q47. Write a program to check user role (admin, user, guest) using match case.
role=input("Enter your role (admin, user, guest):")
match role:
    case 'admin':
        print("Administrative privileges.")
    case 'user':
        print("uUser privileges.")
    case 'guest':
        print("limited guest privileges.")
    case _:
        print("Invalid role!")