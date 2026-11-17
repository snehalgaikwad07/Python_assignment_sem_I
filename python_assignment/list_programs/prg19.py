#19. Create a list of 10 numbers and remove duplicates.
lst=[1,2,3,4,5,6,7,8,9,10,1,2,3,4,5]
print("Original list:",lst)
lst=list(set(lst))
print("List after removing duplicates:",lst)