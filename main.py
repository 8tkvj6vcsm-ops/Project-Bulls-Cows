import random
import time
from typing import Optional, Tuple


DIGITS = 4
SEPARATOR = "-" * 47


def intro() -> None:
    """Print the game intro text."""
    print("Hi there!")
    print(SEPARATOR)
    print(f"I've generated a random {DIGITS} digit number for you.")
    print("Let's play a bulls and cows game.")
    print(SEPARATOR)
    print("Enter a number:")
    print(SEPARATOR)


def generate_secret(length: int = DIGITS) -> str:
    """Generate a secret number with unique digits, not starting with zero."""
    digits = list("0123456789")
    first = random.choice(digits[1:])  # 1-9
    digits.remove(first)
    rest = random.sample(digits, k=length - 1)
    return first + "".join(rest)


def validate_guess(guess: str, length: int = DIGITS) -> Optional[str]:
    """
    Validate user guess. Returns an error message if invalid, otherwise None.
    Rules: correct length, digits only, not starting with zero, unique digits.
    """
    if len(guess) != length:
        return f"Input must be exactly {length} digits."
    if not guess.isdigit():
        return "Input must contain digits only."
    if guess[0] == "0":
        return "Number must not start with zero."
    if len(set(guess)) != length:
        return "Digits must be unique (no duplicates)."
    return None


def count_bulls_cows(secret: str, guess: str) -> Tuple[int, int]:
    """Return (bulls, cows). Cows exclude positions already counted as bulls."""
    bulls = sum(1 for s, g in zip(secret, guess) if s == g)
    common = len(set(secret) & set(guess))
    cows = common - bulls
    return bulls, cows


def plural(n: int, word: str) -> str:
    """Return correctly pluralized English label for 'bull'/'cow'."""
    return f"{n} {word}" if n == 1 else f"{n} {word}s"


def play_one_game() -> None:
    """Run one game session."""
    secret = generate_secret(DIGITS)
    guesses = 0
    start = time.time()

    while True:
        guess = input(">>> ").strip()
        error = validate_guess(guess, DIGITS)
        if error:
            print(error)
            print(SEPARATOR)
            continue

        guesses += 1
        bulls, cows = count_bulls_cows(secret, guess)

        if bulls == DIGITS:
            elapsed = int(time.time() - start)
            print("Correct, you've guessed the right number")
            print(f"in {guesses} guesses!")
            print(SEPARATOR)
            print("That's amazing!")
            print(f"Time: {elapsed} seconds")
            return

        print(f"{plural(bulls, 'bull')}, {plural(cows, 'cow')}")
        print(SEPARATOR)


def main() -> None:
    """Program entry point."""
    intro()
    play_one_game()


if __name__ == "__main__":
    main()
