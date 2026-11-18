#*********************  Hospital OPD Token Queue *************************


queue = []
time = 10
token = 1

while True:
    print("\n1. Register patient")
    print("2. Emergency patient")
    print("3. Serve patient")
    print("4. Cancel token")
    print("5. Display queue")
    print("6. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        name = input("Enter patient name: ")
        queue.append([token, name])
        print("Token number:", token)
        token = token + 1

    elif ch == 2:
        name = input("Enter emergency patient name: ")
        queue.insert(0, [token, name])
        print("Emergency token number:", token)
        token = token + 1

    elif ch == 3:
        if len(queue) > 0:
            p = queue.pop(0)
            print("Patient served:", p[1])
        else:
            print("No patients in queue!")

    elif ch == 4:
        t = int(input("Enter token number to cancel: "))

        for p in queue:
            if p[0] == t:
                queue.remove(p)
                print("Token cancelled!")
                break
        else:
            print("Token not found!")

    elif ch == 5:
        print("*** OPD Waiting Queue ***")

        if len(queue) == 0:
            print("Queue is empty!")
        else:
            for i, p in enumerate(queue):
                wait = i * time
                print("Token:", p[0], "| Name:", p[1],
                      "| Position:", i + 1,
                      "| Waiting time:", wait, "minutes")

        print("Total patients waiting:", len(queue))

    elif ch == 6:
        print("Thank you!")
        break

    else:
        print("Invalid choice!")