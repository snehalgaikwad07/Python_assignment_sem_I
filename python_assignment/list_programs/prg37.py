#37. Create a list and check palindrome list.
lst=[1,2,3,4]
rev=lst[::-1]
if lst==rev:
    print("list is palindrome")
else:
    print("list is not palindrome")