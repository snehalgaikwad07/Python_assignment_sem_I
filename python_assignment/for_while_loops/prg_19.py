#Q19. Check whether a number is prime
num = int(input("Enter a number: "))
i = 1
count = 0
while i <= num:
    if num % i == 0:
        count = count + 1
    i = i + 1
if num > 1 and count == 2:
    print("Prime number")
else:
    print("Not a prime number")