# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary




answer = ""
bid_dictionary = {}


def highest_bidder(bid_dictionary):
    top_bid = 0
    top_bidder = ""
    for bidder in bid_dictionary:
        bid_amount = bid_dictionary[bidder]
        if int(bid_amount) > int(top_bid):
            top_bid = bid_amount
            top_bidder = bidder

    print(f"{top_bidder} won. ")


while answer != "no":
    name = input("What is your name: ")
    bid = input("What is your bid? £: ")
    bid_dictionary[name] = bid

    answer = input("Are there any other bidders? Type 'Yes' or 'No'. ").lower()
    print("\n" * 20)

highest_bidder(bid_dictionary)



