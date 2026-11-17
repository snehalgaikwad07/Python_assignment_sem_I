#2. Create a list and replace an element at a given index.
lst=[10,20,30,40,50]
print("Before replacing element:",lst)
index=int(input("Enter index of element to replace:"))
new_element=int(input("Enter new element:"))
lst[index]=new_element
print("After replacing element:",lst)