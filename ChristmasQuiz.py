def menu():
    if input == "1":
        quiz()
    if input == "2":
        rps()


def quiz():
    print("Hardware Quiz")
    score = 0
    #Question 1
    print("Q1")
    print("Santa is real")
    ans1 = input("A) True B) False ")
    if ans1 == "A":
        print("Correct")
        score = score + 1
    else:
        print("Incorrect")
        score = score - 1


    #Question 2
    print("Q2")
    print("Rudolph eats your cookies")
    ans2 = input("A) True B) False ")
    if ans2 == "B":
        print("Correct")
        score = score + 1

    else:
        print("Incorrect")
        score = score - 1

    #Question 3

    print("Q3")
    print("Snow is white")
    ans3 = input("A) True B) False ")
    if ans3 == "A":
        print("Correct")
        score = score + 1
    else:
        print("Incorrect")
        score = score - 1

    print("Your score is: " + int(score))



def rps():
    import random
    print("Welcome to Rock, Paper, Scissors! ")

    for i in range(3):
        userGuess = input("Please Enter: Rock, Paper, Scissors: ")
        compGuess = random.randint(1,3)
    
    if userGuess == "Rock" and compGuess == "Rock":
        gameResult = "Tie"

    elif userGuess == "Rock" and compGuess == "Paper":
        gameResult = "CPU Wins"

    elif userGuess == "Rock" and compGurss == "Scissors":
        gameResult = "You Win"
    
    if userGuess == "Paper" and compGuess == "Paper":
        gameResult = "Tie"

    elif userGuess == "Paper" and compGuess == "Scissors":
        gameResult = "CPU Wins"

    elif userGuess == "Paper" and compGurss == "Rock":
        gameResult = "You Win"
    
    if userGuess == "Scissors" and compGuess == "Scissors":
        gameResult = "Tie"

    elif userGuess == "Scissors" and compGuess == "Rock":
        gameResult = "CPU Wins"

    elif userGuess == "Scissors" and compGurss == "Paper":
        gameResult = "You Win"


menu()
