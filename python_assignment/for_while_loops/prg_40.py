#Q40.Print numbers which are perfect squares between 1 and 100.
for i in range(1, 101):
    j = 1
    while j * j <= i:
        if j * j == i:
            print(i)
        j += 1