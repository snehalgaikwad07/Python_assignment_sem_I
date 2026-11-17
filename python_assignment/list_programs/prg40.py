#40. Create a list and demonstrate all list methods.
lst = [10, 20, 30, 40]

print("Original List:", lst)

lst.append(50)
print("After append:", lst)

lst.insert(1, 15)
print("After insert:", lst)

lst.extend([60, 70])
print("After extend:", lst)

lst.remove(30)
print("After remove:", lst)

lst.pop()
print("After pop:", lst)

print("Index of 40:", lst.index(40))

lst.append(20)
print("Count of 20:", lst.count(20))

lst.sort()
print("After sort:", lst)

lst.reverse()
print("After reverse:", lst)

lst.copy()
print("After copy:", lst)

lst.clear()
print("After clear:", lst)