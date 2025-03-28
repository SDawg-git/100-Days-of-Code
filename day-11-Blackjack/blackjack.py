import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


playGame = input("Do you want to play a game of Blackjack? Y/N: ")
if playGame == "Y":


    playerDeck = []
    dealerDeck = []

    playerDeck.append(random.choice(cards))
    dealerDeck.append(random.choice(cards))
    playerDeck.append(random.choice(cards))

    print(f" Your cards: {playerDeck}, current score: {sum(playerDeck)} ")
    print(f" Computer's first draw: {dealerDeck}")


    anotherCard = input("Type 'Y' to get another card, type 'N' to pass: ")

    while anotherCard == "Y" and sum(playerDeck) <= 21 and sum(dealerDeck) <= 21:

        if sum(dealerDeck) < 17:
            dealerDeck.append(random.choice(cards))

        randomCard = random.choice(cards)
        if randomCard == 11:
            aceOrOne = input("Would you like the Ace to count as 1 or 11?: ")
            if aceOrOne == 1:
                playerDeck.append(1)
                print("appended 1")
                print(f"Your current deck is {playerDeck}, with the score of {sum(playerDeck)}")
            elif aceOrOne == 11:
                playerDeck.append(11)
                print("appended 11")
                print(f"Your current deck is {playerDeck}, with the score of {sum(playerDeck)}")
        else:
            playerDeck.append(randomCard)
            print(f"Your current deck is {playerDeck}, with the score of {sum(playerDeck)}")
            #print(f"RNG card of '{randomCard}' appended")





        if sum(playerDeck) > 21:
            print(f"You went over 21 with the score of {sum(playerDeck)}, YOU LOSE")
            exit()
        elif sum(dealerDeck) > 21:
            print(f"The dealer went over 21 with the score of {sum(dealerDeck)}, YOU WIN!")
            exit()
        else:
            anotherCard = input("Type 'Y' to get another card, type 'N' to pass: ")
        #print(sum(playerDeck))
        #print(sum(dealerDeck))


    while sum(dealerDeck) < 17:
        dealerDeck.append(random.choice(cards))



    if sum(playerDeck) > 21:
        print(f"You went over 21 with the score of {sum(playerDeck)}, YOU LOSE")
        exit()
    if sum(dealerDeck) > 21:
        print(f"The dealer went over 21 with the score of {sum(dealerDeck)}, you win with the deck of {playerDeck} score of {sum(playerDeck)}!")
        exit()


    else:

        if sum(playerDeck) > sum(dealerDeck):
            print(f"Your score of {sum(playerDeck)} is higher than the {sum(dealerDeck)} score of the dealer"
                f"\n YOU WIN")
        elif sum(playerDeck) < sum(dealerDeck):
            print(f"Your score of {sum(playerDeck)} is lower than the {sum(dealerDeck)} score of the dealer"
                f"\n YOU LOSE")
        else:
            print(f"It's a tie with the player deck being {playerDeck} and dealer deck being {dealerDeck}")
