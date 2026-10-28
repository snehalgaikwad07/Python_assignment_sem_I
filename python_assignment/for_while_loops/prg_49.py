#Q49. Display menu-driven program using while loop.
print("Menu")
print("1.java")
print("2.c")
print("3.c++")
while True:
    choice=int(input("Enter a choice between(1-3):"))
    match choice:
        case 1:
            print("Java")
        case 2:
            print("c")
        case 3:
            print("c++")
        case _:
            print("Wrong choice!")
        
    