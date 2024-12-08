import random


choice = input("Type 'R' for Rock, 'P' for Paper and 'S' for Scissors ")
RPS = ["Rock", "Paper", "Scissors"]
computerChoice = random.choice(RPS)


if choice == "R" and computerChoice == "Rock":
    print("Tie")
elif choice == "R" and computerChoice  == "Paper":
    print("Loss")
elif choice == "R" and computerChoice  == "Scissors":
    print("Win")

elif choice == "P" and computerChoice  == "Rock":
    print("Win")
elif choice == "P" and computerChoice  == "Paper":
    print("Tie")
elif choice == "P" and computerChoice  == "Scissors":
    print("Loss")

elif choice == "S" and computerChoice  == "Rock":
    print("Loss")
elif choice == "S" and computerChoice  == "Paper":
    print("Win")
elif choice == "S" and computerChoice  == "Scissors":
    print("Tie")

