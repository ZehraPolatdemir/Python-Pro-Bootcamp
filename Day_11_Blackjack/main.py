import art
import random
import os

def game():

    def blackjack():
        if user_total < 21 and comp_total < 21:
            if user_total > comp_total:
                print("You win 😃")
            elif comp_total > user_total:
                print("You lose 😤")
        elif user_total == comp_total:
            print("Draw 🙃")
        elif user_total > 21:
            print("You went over. You lose 😭")
        elif comp_total > 21:
            print("Opponent went over. You win 😁")
        elif user_total == 21:
            print("Win with a Blackjack 😎")
        elif comp_total == 21:
            print("Lose, opponent has Blackjack 😱")



    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    user_carts = random.choices(cards, k=2)
    user_total = user_carts[0] + user_carts[1]
    if user_total > 17:
        cards[0] = 1

    comp_carts = random.choices(cards, k=2)
    comp_total = comp_carts[0] + comp_carts[1]
    while comp_total < 17:
        comp_carts += random.choices(cards, k=1)
        comp_total += comp_carts[-1]

    print(art.logo)
    print(f"Your cards: {user_carts}, current score: {user_total}")
    print(f"Computer's first card: {comp_carts[0]}")

    is_user_drawing = 1
    while is_user_drawing:
        get_cart = input("Type 'y' to get another card, type 'n' to pass:")
        if get_cart == "y":
            user_carts += random.choices(cards, k=1)
            user_total += user_carts[-1]
            print(f"\nYour final hand: {user_carts}, final score: {user_total}")
            print(f"Computer's final hand: {comp_carts}, final score: {comp_total}")
            if user_total > 21:
                is_user_drawing = 0

        elif get_cart == "n":
            print(f"Your final hand: {user_carts}, final score: {user_total}")
            print(f"Computer's final hand: {comp_carts}, final score: {comp_total}")
            is_user_drawing = 0

    blackjack()

    want_again = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    os.system('clear')
    if want_again == "y":
        game()
    else:
        print("The game has ended.")

game()