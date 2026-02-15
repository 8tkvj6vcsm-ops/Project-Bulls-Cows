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

        if len(secret) == 0 and number == "0":
            continue

        if number not in secret:
            secret = secret + number

    return secret


def validate_guess(guess):
    guess = guess.strip()

    if len(guess) != digits:
        return "Input must be exactly 4 digits."

    if not guess.isdigit():
        return "Input must contain digits only."

    if guess[0] == "0":
        return "Number must not start with zero."

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
        elif guess[i] in secret:
            cows += 1

    return bulls, cows


def format_result(count, word):
    if count == 1:
        return str(count) + " " + word
    return str(count) + " " + word + "s"


def play_game():
    secret = generate_secret()
    guesses = 0

    while True:
        guess = input(">>> ")

        error_message = validate_guess(guess)
        if error_message:
            print(error_message)
            print(separator)
            continue

        guess = guess.strip()
        guesses += 1

        bulls, cows = count_bulls_cows(secret, guess)

        if bulls == digits:
            print("Correct, you've guessed the right number")
            print("in", guesses, "guesses!")
            print(separator)
            print("That's amazing!")
            break

        print(format_result(bulls, "bull") + ", " + format_result(cows, "cow"))
        print(separator)


def main():
    intro()
    play_game()


if __name__ == "__main__":
    main()