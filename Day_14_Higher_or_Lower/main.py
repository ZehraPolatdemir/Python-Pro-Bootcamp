import art
import os
import random
import game_data

def get_random_account():
    a_kisi, b_kisi = random.sample(game_data.data, 2)
    return a_kisi, b_kisi

def format_data(account):
    formatted_string = f"{account['name']}, a {account['description']}, from {account['country']}"
    return formatted_string


def check_answer(current_score, a_account, b_account):
    print(art.logo)
    if current_score > 0:
        print(f"You're right! Current score: {current_score}.")

    print(f"Compare A: {format_data(a_account)}")
    print(art.vs)
    print(f"Against B: {format_data(b_account)}")

    return input("Who has more followers? Type 'A' or 'B': ").lower()

def check_guess(account_a, account_b, guess):
    if account_a > account_b:
        return guess == "a"
    else:
        return guess == "b"

def play_game():

    score = 0
    game_should_continue = True
    account_a, account_b = get_random_account()


    while game_should_continue:
        choice = check_answer(score, account_a, account_b)

        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]

        is_correct = check_guess(a_follower_count,b_follower_count,choice)
        os.system("clear")

        if is_correct:
            score += 1
            account_a = account_b
            account_b = random.choice(game_data.data)
            while account_a == account_b:
                account_b = random.choice(game_data.data)

        else:
            print(art.logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            game_should_continue = False

play_game()







