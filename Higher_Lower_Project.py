import random

data = [
    {"name": "Instagram", "follower_count": 649, "description": "Social media platform", "country": "United States"},
    {"name": "Cristiano Ronaldo", "follower_count": 593, "description": "Footballer", "country": "Portugal"},
    {"name": "Lionel Messi", "follower_count": 475, "description": "Footballer", "country": "Argentina"},
    {"name": "Selena Gomez", "follower_count": 424, "description": "Musician and actress", "country": "United States"},
    {"name": "Kylie Jenner", "follower_count": 396, "description": "Reality TV personality and businesswoman",
     "country": "United States"},
    {"name": "Dwayne Johnson", "follower_count": 386, "description": "Actor and professional wrestler",
     "country": "United States"},
    {"name": "Ariana Grande", "follower_count": 376, "description": "Musician and actress", "country": "United States"},
    {"name": "Kim Kardashian", "follower_count": 361, "description": "Reality TV personality and businesswoman",
     "country": "United States"},
    {"name": "Beyoncé", "follower_count": 313, "description": "Musician", "country": "United States"},
    {"name": "Nike", "follower_count": 298, "description": "Sportswear multinational", "country": "United States"},
    {"name": "Justin Bieber", "follower_count": 292, "description": "Musician", "country": "Canada"},
    {"name": "Taylor Swift", "follower_count": 266, "description": "Musician", "country": "United States"},
    {"name": "Virat Kohli", "follower_count": 254, "description": "Cricketer", "country": "India"},
    {"name": "Jennifer Lopez", "follower_count": 247, "description": "Musician and actress",
     "country": "United States"},
    {"name": "Zendaya", "follower_count": 182, "description": "Actress and musician", "country": "United States"}
]


def format_data(account):
    return f"{account['name']}, a {account['description']}, from {account['country']}"


def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


def game():
    score = 0
    game_should_continue = True
    account_b = random.choice(data)

    print("--- Welcome to Higher Lower ---")

    while game_should_continue:
        account_a = account_b
        account_b = random.choice(data)

        while account_a == account_b:
            account_b = random.choice(data)

        print(f"Compare A: {format_data(account_a)}.")
        print("--- VS ---")
        print(f"Against B: {format_data(account_b)}.")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        print("\n" * 20)

        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")


game()