#Guess the number

import random
import time
import sys

def menu():
    choice = int(input("1) Play Game 2) View Scores: ")
    if choice == 1:
                 game()
    elif choice == 2:
                 viewScores()

                 


def game():
    
    name = str(input("Enter Name: "))
    number = random.randint(1, 1000)
    count = 0
    userGuess = int(input("Enter Guess:  (1-1000): "))
    print(number)

    while userGuess != number:
        
        time.sleep(0.5)
        print("Incorrect Guess")
        count = count + 1
        userGuess = int(input("Enter Guess (1-1000): "))
        time.sleep(0.5)

        if userGuess < number:
            time.sleep(0.5)
            print("Guess too low")

        elif userGuess > number:
            time.sleep(0.5)
            print("Guess too high")

    print("Correct Guess")
    print("Well done " + name + "you used " + count + "guesses")

    file = open("Scores.txt", "a")
    file.write("Name: " + name = "Score: " + str(count) + "\n \n")
    file.close()


    print("Details saved!")

def viewScores():
                 file = open("Scores.txt", "r")
                 print(file.readlines())
                 file.close()

                 print("\n \n")
                 menu()
