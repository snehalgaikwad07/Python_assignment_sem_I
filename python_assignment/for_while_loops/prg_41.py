#Q41.Print numbers which are perfect cubes between 1 and 100
for i in range(1, 101):
    j = 1
    while j ** 3 <= i:
        if j ** 3 == i:
            print(i)
        j += 1