import random

digits = 4
separator = "-" * 47


def intro():
    print("Hi there!")
    print(separator)
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print(separator)
    print("Enter a number:")
    print(separator)


def generate_secret():
    secret = ""

    while len(secret) < digits:
        number = str(random.randint(0, 9))

        # první číslo nesmí být 0
        if len(secret) == 0 and number == "0":
            continue

        # kontrola, aby se čísla neopakovala
        if number not in secret:
            secret = secret + number

    return secret


def validate_guess(guess):

    if len(guess) != digits:
        return "Input must be exactly 4 digits."

    if not guess.isdigit():
        return "Input must contain digits only."

    if guess[0] == "0":
        return "Number must not start with zero."

    # kontrola duplicit bez set()
    for i in range(len(guess)):
        for j in range(i + 1, len(guess)):
            if guess[i] == guess[j]:
                return "Digits must be unique."

    return None


def count_bulls_cows(secret, guess):
    bulls = 0
    cows = 0

    for i in range(digits):
        if guess[i] == secret[i]:
            bulls += 1
        else:
            # kontrola cows ručně
            for j in range(digits):
                if guess[i] == secret[j]:
                    cows += 1

    return bulls, cows


def play_game():
    secret = generate_secret()
    guesses = 0

    while True:
        guess = input(">>> ")

        error = validate_guess(guess)
        if error:
            print(error)
            print(separator)
            continue

        guesses += 1

        bulls, cows = count_bulls_cows(secret, guess)

        if bulls == digits:
            print("Correct, you've guessed the right number")
            print("in", guesses, "guesses!")
            print(separator)
            print("That's amazing!")
            break

        print(bulls, "bulls,", cows, "cows")
        print(separator)


intro()
play_game()