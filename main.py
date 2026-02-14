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
    numbers = list("0123456789")

    first = random.choice(numbers[1:])
    numbers.remove(first)

    rest = random.sample(numbers, digits - 1)

    secret = first
    for n in rest:
        secret = secret + n

        return secret



def validate_guess(guess):
    if len(guess) != digits:
        return "Input must be exactly 4 digits."

    if not guess.isdigit():
        return "Input must contain digits only."

    if guess[0] == "0":
        return "Number must not start with zero."

    if len(set(guess)) != digits:
        return "Digits must be unique."

    return None


def count_bulls_cows(secret, guess):
    bulls = 0
    cows = 0

    for i in range(digits):
        if guess[i] == secret[i]:
            bulls += 1
        elif guess[i] in secret:
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


def main():
    intro()
    play_game()


main()