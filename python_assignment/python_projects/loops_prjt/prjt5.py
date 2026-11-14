
#******** Number Guessing Game ********

secret_number = 37
attempts = 0
max_attempts = 5

while attempts < max_attempts:

    guess = int(input("Guess the secret number: "))
    attempts = attempts + 1

    if guess == secret_number:
        print("Congratulations! You guessed correctly.")
        break

    elif guess < secret_number:
        print("Too low!")

    else:
        print("Too high!")

# Display  result
print("\n----- Game Result -----")

if guess == secret_number:
    print("You Win!")
else:
    print("You Lose!")
    print("Secret Number was:", secret_number)

print("Attempts Used:", attempts)
