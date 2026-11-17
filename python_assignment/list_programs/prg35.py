#35. Create a list and remove all even numbers.
lst=[1,2,3,4,5,6,7,8,9,10]
new_lst=[]
for i in lst:
    if i%2!=0:
       new_lst.append(i)
print("After removing all even numbers:",new_lst)
