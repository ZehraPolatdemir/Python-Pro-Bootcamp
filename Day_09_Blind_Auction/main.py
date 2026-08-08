import art
import os
print(art.logo)
print("Welcome to the secret auction program.")
auction_bids = {}
continue_bidding = True
while continue_bidding:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    more_bidders = input("Are they any bidders? Type 'yes' or 'no'.").lower()

    auction_bids[name] = price

    if more_bidders == "no":
        continue_bidding = False
        highest_bid = 0
        winner = ""
        for bidder in auction_bids:
            current_bid = auction_bids[bidder]
            if current_bid > highest_bid:
                highest_bid = current_bid
                winner = bidder
        print(f"The winner is {winner} a bid of ${highest_bid}")

    if more_bidders == "yes":
        os.system("clear")

