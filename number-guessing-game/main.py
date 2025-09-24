import random


def main() -> None:
    MIN_NUMBER = 1
    MAX_NUMBER = 100
    secret_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    attempts = 0
    print(f"Guess my number. It is an integer between {MIN_NUMBER} and {MAX_NUMBER}.")
    while True:
        attempts += 1
        try:
            guess_number = int(input("Number: "))
        except ValueError:
            print(
                f"Incorrect. It must be an integer between {MIN_NUMBER} and {MAX_NUMBER}."
            )
            continue
        if guess_number < MIN_NUMBER or guess_number > MAX_NUMBER:
            print(
                f"Incorrect. It must be an integer between {MIN_NUMBER} and {MAX_NUMBER}."
            )
            continue
        if guess_number > secret_number:
            print("Too high.")
            continue
        elif guess_number < secret_number:
            print("Too low.")
            continue
        else:
            print(f"Correct. My number was {secret_number}.")
            print(f"You guessed it in {attempts} attempts .")
            break


if __name__ == "__main__":
    main()
