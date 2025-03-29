import random

print("Welcome to the number guessing game.")
easyOrHard = input("Do you want to play the easy or hard mode? Type 'Easy' or 'Hard': ")
guesses = 0
if easyOrHard == "Easy":
    guesses = 10
else:
    guesses = 5

numberToGuess = random.randint(1,100)

gameWon = False



while guesses > 0 and gameWon != True:
    guess = int(input("Enter your guess: "))

    if guess == numberToGuess:
        print("Congrats! You've guessed the number!")
        gameWon = True

    elif guess > numberToGuess:
        guesses -= 1
        if guesses > 0:
            print(f"Number too high - you have {guesses} guesses left, try again: ")


    elif guess < numberToGuess:
        guesses -= 1
        if guesses > 0:
            print(f"Number too low - you have {guesses} guesses left, try again: ")

if gameWon == False:
    print("You've lost! Ran out of guesses.")

