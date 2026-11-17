#34. Create a list and find common elements between two lists.
lst1 = [10, 20, 30, 40, 50]
lst2 = [30, 40, 50, 60, 70]
common = []
for i in lst1:
    if i in lst2:
        common.append(i)
print("Common Elements:", common)