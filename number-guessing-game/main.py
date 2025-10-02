"""
Number Guessing Game

A number guessing game where the player attempts to guess a randomly chosen
number between MIN_NUMBER and MAX_NUMBER.
"""

import random

MIN_NUMBER: int = 1
MAX_NUMBER: int = 100

WELCOME_MESSAGE = "Guess my number. It is between {min} and {max}."
PROMPT_MESSAGE = "Enter a number: "
NOT_A_NUMBER_MESSAGE = "Not a number. Enter a number between {min} and {max}."
OUT_OF_RANGE_MESSAGE = "Out of range. Enter a number between {min} and {max}."
HIGH_MESSAGE = "You guessed higher than my number."
LOW_MESSAGE = "You guessed lower than my number."
CORRECT_MESSAGE = "Correct. My number was {secret_number}."
ATTEMPTS_MESSAGE = "You guessed it in {number_of_attempts} attempts ."


def is_valid_guess_number(guess_number: int) -> bool:
    """
    Check if the number the player guessed is within the valid range
    [MIN_NUMBER, MAX_NUMBER]

    Args:
        guess_number (int): The number the player guessed.

    Returns:
        bool: True, if the number the player guessed is within the valid range,
        False otherwise.
    """
    return MIN_NUMBER <= guess_number <= MAX_NUMBER


def main() -> None:
    """
    Main entry point of program.

    This program randomly chooses a number between MIN_NUMBER and MAX_NUMBER
    and prompts the user to guess until the correct number is found. Hints are
    provided after each guess, and the number of attempts is reported.
    """
    secret_number: int = random.randint(MIN_NUMBER, MAX_NUMBER)
    number_of_attempts: int = 0

    print(WELCOME_MESSAGE.format(min=MIN_NUMBER, max=MAX_NUMBER))

    while True:
        number_of_attempts += 1
        try:
            guess_number: int = int(input(PROMPT_MESSAGE))
        except ValueError:
            print(NOT_A_NUMBER_MESSAGE.format(min=MIN_NUMBER, max=MAX_NUMBER))
            continue

        if not is_valid_guess_number(guess_number):
            print(OUT_OF_RANGE_MESSAGE.format(min=MIN_NUMBER, max=MAX_NUMBER))
            continue

        if guess_number > secret_number:
            print(HIGH_MESSAGE)
        elif guess_number < secret_number:
            print(LOW_MESSAGE)
        else:
            print(CORRECT_MESSAGE.format(secret_number=secret_number))
            print(ATTEMPTS_MESSAGE.format(number_of_attempts=number_of_attempts))
            break


if __name__ == "__main__":
    main()
