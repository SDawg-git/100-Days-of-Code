import random
import game_data
import art



score = 0
game_over = False
choiceA = random.choice(game_data.data)
choiceB = random.choice(game_data.data)
if choiceA == choiceB:
    choiceB = random.choice(game_data.data)

print(art.logo)
while not game_over:

    print(F"Compare: {choiceA.get("name")}, a {choiceA.get("description")}, from {choiceA.get("country")}.")
    print(art.vs)
    print(F"Compare: {choiceB.get("name")}, a {choiceB.get("description")}, from {choiceB.get("country")}.")

    user_choice = input("Who has more followers? Type 'A' or 'B': ")

    if user_choice == "A":
        if choiceA.get("follower_count") > choiceB.get("follower_count"):
            score += 1
            print(art.logo)
            print(f"You're right! Current score: {score}")
            choiceB = random.choice(game_data.data)


        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            game_over = True
            exit()

    elif user_choice == "B":
        if choiceB.get("follower_count") > choiceA.get("follower_count"):
            score += 1
            print(art.logo)
            print(f"You're right! Current score: {score}")
            choiceA = choiceB
            choiceB = random.choice(game_data.data)

        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            game_over = True
            exit()

