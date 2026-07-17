import random

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0

print("===================================")
print("     ROCK PAPER SCISSORS GAME")
print("===================================")
print("Instructions:")
print("Type rock, paper, or scissors.")
print("Type 'exit' anytime to quit.\n")

while True:
    # User input
    user_choice = input("Enter your choice: ").lower()

    if user_choice == "exit":
        break

    if user_choice not in choices:
        print("Invalid choice! Please enter rock, paper, or scissors.\n")
        continue

    # Computer choice
    computer_choice = random.choice(choices)

    print(f"\nYou chose      : {user_choice}")
    print(f"Computer chose : {computer_choice}")

    # Game logic
    if user_choice == computer_choice:
        print("Result: It's a Tie!")

    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("Result: You Win!")
        user_score += 1

    else:
        print("Result: Computer Wins!")
        computer_score += 1

    # Display scores
    print("\nCurrent Score")
    print(f"You      : {user_score}")
    print(f"Computer : {computer_score}")

    # Play again
    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        break

    print()

# Final Score
print("\n===================================")
print("           GAME OVER")
print("===================================")
print(f"Final Score")
print(f"You      : {user_score}")
print(f"Computer : {computer_score}")

if user_score > computer_score:
    print("\nCongratulations! You are the overall winner!")
elif computer_score > user_score:
    print("\nComputer wins the game!")
else:
    print("\nThe game ends in a tie!")

print("\nThanks for playing!")