#SIMPLE QUIZE GAME PROJECT 

def quiz_game():
    score = 0

    print("Welcome to the Quiz Game!\n")

    # Question 1
    print("Q1. What is the capital of India?")
    print("A. Mumbai")
    print("B. Delhi")
    print("C. Pune")
    print("D. Chennai")
    ans = input("Enter your answer (A/B/C/D): ").upper()

    if ans == "B":
        print("Correct!\n")
        score += 1
    else:
        print("Wrong! Correct answer is B\n")

    # Question 2
    print("Q2. Which language is used for web development?")
    print("A. Python")
    print("B. HTML")
    print("C. C++")
    print("D. Java")
    ans = input("Enter your answer (A/B/C/D): ").upper()

    if ans == "B":
        print("Correct!\n")
        score += 1
    else:
        print("Wrong! Correct answer is B\n")

    # Question 3
    print("Q3. What is 5 + 3?")
    print("A. 5")
    print("B. 8")
    print("C. 10")
    print("D. 6")
    ans = input("Enter your answer (A/B/C/D): ").upper()

    if ans == "B":
        print("Correct!\n")
        score += 1
    else:
        print("Wrong! Correct answer is B\n")

    # Question 4
    print("Q4. Which is a programming language?")
    print("A. HTML")
    print("B. CSS")
    print("C. Python")
    print("D. All")
    ans = input("Enter your answer (A/B/C/D): ").upper()

    if ans == "D":
        print("Correct!\n")
        score += 1
    else:
        print("Wrong! Correct answer is D\n")

    # Question 5
    print("Q5. Which device is used to input data?")
    print("A. Monitor")
    print("B. Keyboard")
    print("C. Printer")
    print("D. Speaker")
    ans = input("Enter your answer (A/B/C/D): ").upper()

    if ans == "B":
        print("Correct!\n")
        score += 1
    else:
        print("Wrong! Correct answer is B\n")

    print("Quiz Finished!")
    print("Your Score:", score, "/ 5")

quiz_game()