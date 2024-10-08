import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    max_attempts = 10  # Limit the number of attempts

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts}: Guess a number between 1 and 100: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue
        
        attempts += 1  # Increment the attempt count

        # Check the guessed number
        if guess < 1 or guess > 100:
            print("Out of bounds! Please guess a number between 1 and 100.")
        elif guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
            break
    else:
        print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")

# Run the game
if __name__ == "__main__":
    number_guessing_game()
