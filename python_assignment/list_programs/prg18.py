#18. Take user input to create a list and display it.
lst=[]
n=int(input("Enter number of elements in list:"))
for i in range(n):
    element=input("Enter element:")
    lst.append(element)
print("List:",lst)