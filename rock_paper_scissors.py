import random

def get_player_move():
    while True:
        player_input = input("Choose [r]ock, [p]aper, or [s]cissors: ").lower()
        if player_input == "r":
            return "Rock"
        elif player_input == "p":
            return "Paper"
        elif player_input == "s":
            return "Scissors"
        else:
            print("Invalid input. Please enter 'r', 'p', or 's'.")

def get_computer_move():
    moves = ["Rock", "Paper", "Scissors"]
    return random.choice(moves)

def determine_winner(player_move, computer_move):
    if player_move == computer_move:
        return "It's a draw!"
    elif (player_move == "Rock" and computer_move == "Scissors") or \
         (player_move == "Paper" and computer_move == "Rock") or \
         (player_move == "Scissors" and computer_move == "Paper"):
        return "You win!"
    else:
        return "You lose!"

def main():
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        player_move = get_player_move()
        computer_move = get_computer_move()

        print(f"\nYou chose: {player_move}")
        print(f"The computer chose: {computer_move}")

        result = determine_winner(player_move, computer_move)
        print(result)

        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
