import random

DIGITS = 4  # length of the secret number
SEPARATOR = "-" * 47  # visual separator for output lines


def intro():
    """Print game introduction and basic instructions."""
    print("Hi there!")
    print(SEPARATOR)
    print(f"I've generated a random {DIGITS} digit number for you.")
    print("Let's play a bulls and cows game.")
    print(SEPARATOR)
    print("Enter a number:")
    print(SEPARATOR)


def generate_secret():
    """Generate a random secret number with unique digits and non-zero first digit."""
    secret = ""

    while len(secret) < DIGITS:
        number = str(random.randint(0, 9))

        # first digit must not be zero
        if len(secret) == 0 and number == "0":
            continue

        # digits must be unique
        if number not in secret:
            secret += number

    return secret


def validate_guess(guess):
    """
    Validate user's guess.

    Returns:
        None if the guess is valid, otherwise an error message (str).
    """
    if len(guess) != DIGITS:
        return f"Input must be exactly {DIGITS} digits."

    if not guess.isdigit():
        return "Input must contain digits only."

    if guess[0] == "0":
        return "Number must not start with zero."

    # check uniqueness of digits using a set (no nested loops)
    if len(set(guess)) != len(guess):
        return "Digits must be unique."

    return None


def count_bulls_cows(secret, guess):
    """
    Count bulls and cows for the given secret and guess.

    Bull  = correct digit in the correct position.
    Cow   = correct digit in the wrong position.

    Returns:
        (bulls, cows) tuple of integers.
    """
    bulls = 0
    cows = 0

    # enumerate gives index + digit from the guess
    for index, guess_digit in enumerate(guess):
        if guess_digit == secret[index]:
            bulls += 1
        elif guess_digit in secret:
            cows += 1

    return bulls, cows


def format_result(count, singular_word):
    """
    Format result.

    Examples:
        0 -> '0 bulls'
        1 -> '1 bull'
        2 -> '2 bulls'
    """
    if count == 1:
        return f"{count} {singular_word}"
    return f"{count} {singular_word}s"


def play_game():
    """Main game loop that processes user guesses until the secret is found."""
    secret = generate_secret()
    guesses = 0

    while True:
        raw_guess = input(">>> ")
        guess = raw_guess.strip()

        error_message = validate_guess(guess)
        if error_message:
            print(error_message)
            print(SEPARATOR)
            continue

        guesses += 1
        bulls, cows = count_bulls_cows(secret, guess)

        if bulls == DIGITS:
            print("Correct, you've guessed the right number")
            guess_word = "guess" if guesses == 1 else "guesses"
            print(f"in {guesses} {guess_word}!")
            print(SEPARATOR)
            print("That's amazing!")
            break

        print(f"{format_result(bulls, 'bull')}, {format_result(cows, 'cow')}")
        print(SEPARATOR)


def main():
    """Run the Bulls & Cows game."""
    intro()
    play_game()


if __name__ == "__main__":
    main()
