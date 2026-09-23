import art
import os
import random
import game_data

def get_random_account():
    a_kisi, b_kisi = random.sample(game_data.data, 2)
    return a_kisi, b_kisi

account_a, account_b = get_random_account()

def check_answer():
    print(art.logo)
    if score > 0:
        print(f"You're right! Current score: {score}.")
    print(f"Compare A: {account_a['name']}, a {account_a['description']}, from {account_a['country']}.")
    print(art.vs)
    print(f"Against B: {account_b['name']}, a {account_b['description']}, from {account_b['country']}.")
    return input("Who has more followers? Type 'A' or 'B': ").lower()


winner = ""
score = 0
game_should_continue = True
while game_should_continue:
    choice = check_answer()
    if account_a['follower_count'] > account_b['follower_count']:
        winner = account_a
    else:
        winner = account_b


    if (choice == "a" and winner == account_a) or (choice == "b" and winner == account_b):
        score += 1
        os.system("clear")
        account_a = account_b
        account_b = random.choice(game_data.data)
        while account_a == account_b:
            account_b = random.choice(game_data.data)

    else:
        os.system("clear")
        print(art.logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        game_should_continue = False
