import random
import sys

print("=" * 40)
print("🚢 WELCOME TO BATTLESHIP 🚢")
print("=" * 40)

print("""
Your mission is to find and sink all 3 hidden ships.

Rules:
• There are 3 hidden ships.
• You have 5 lives.
• A HIT does NOT cost a life.
• A MISS costs 1 life.
• Sink all 3 ships before you run out of lives!

Difficulty Levels:
1. Easy   (5 x 5)
2. Medium (7 x 7)
3. Hard   (10 x 10)
""")
def game(size):
    values = set()
    while len(values) < 3:
        ship = (random.randint(1, size), random.randint(1, size))
        values.add(ship)
    lives = 5
    guesses = set()
    misses = set()
    while lives > 0:
        try:
            row = int(input("Enter row:"))
            column = int(input("Enter column:"))
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue
        guess = (row, column)
        if row < 1 or row > size or column < 1 or column > size:
            print(f"Invalid input. Please enter numbers between 1 and {size}.")
            continue
        if guess in guesses:
            print("You already guessed that position and it was a HIT. Try again.")
            continue
        if guess in misses:
            print("You already guessed that position and it was a MISS. Try again.")
            continue
        if guess in values:
            print("=" * 40)
            print("HIT!")
            print("Ships remaining: ", len(values) - len(guesses))
            print("Lives remaining: ", lives * "❤️")
            print("=" * 40)
            guesses.add(guess)
            if guesses == values:
                print("Congratulations! You sank all the ships!")
                break
        else:
            print("=" * 40)
            print("MISS!")
            print("Ships remaining: ", len(values) - len(guesses))
            print("Lives remaining: ", (lives-1) * "❤️")
            print("=" * 40)
            misses.add(guess)
            lives -= 1
            if lives == 0:
                print("Game Over! You've run out of lives.")
                print(f"The ships were located at: {values}")
                break
    play_again()
    
def play_again():
    while True:
        choice = input("Do you want to play again? (y/n): ").lower()
        if choice == "y":
            difficulty()
        elif choice == "n":
            print("Thanks for playing! Goodbye!")
            sys.exit()
        elif choice.lower() == "exit":
            print("Exiting the game. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please enter 'y' or 'n'.")

def start_game():
    while True:
        start = input("Want to start playing? (y/n): ").lower()
        if start == "y":
            print("Great! Let's set up the game.")
            difficulty()
            break
        elif start == "n":
            print("Maybe next time! Goodbye!")
            sys.exit()
        elif start.lower() == "exit":
            print("Exiting the game. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please enter 'y' or 'n'.")

def difficulty():
    while True:
        difficulty = input("Choose difficulty level (1-Easy, 2-Medium, 3-Hard): ")

        if difficulty == "1":
            game(5)
            break

        elif difficulty == "2":
            game(7)
            break

        elif difficulty == "3":
            game(10)
            break
        elif difficulty.lower() == "exit":
            print("Exiting the game. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")


start_game()

