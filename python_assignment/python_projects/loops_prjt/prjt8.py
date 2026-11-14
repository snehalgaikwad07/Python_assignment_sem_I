
#******** Quiz Application ********

questions = [
    "1. Which language is used for web development?",
    "2. What is the capital of India?",
    "3. Which keyword is used to define a function in Python?",
    "4. What is the output of 5 + 5?",
    "5. Which data type stores True or False?"
]

answers = ["python", "delhi", "def", "10", "bool"]

score = 0

print("******** Welcome to Quiz Application ********")

for i in range(len(questions)):

    print("\n", questions[i])
    user_answer = input("Enter your answer: ")

    if user_answer.lower() == answers[i]:
        print("Correct Answer!")
        score = score + 1

    else:
        print("Wrong Answer!")
        print("Correct answer is:", answers[i])


total_questions = len(questions)
percentage = (score / total_questions) * 100

# Display 
print("\n----- Quiz Result -----")
print("Total Questions:", total_questions)
print("Correct Answers:", score)
print("Wrong Answers:", total_questions - score)
print("Score:", score, "/", total_questions)
print("Percentage:", percentage, "%")

# Performance message
if percentage >= 80:
    print("Performance: Excellent!")

elif percentage >= 60:
    print("Performance: Good!")

else:
    print("Performance: Keep Practicing!")
