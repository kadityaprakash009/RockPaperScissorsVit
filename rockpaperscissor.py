import random
def game():
    player_score = 0
    computer_score = 0

    for round in range(1, 4):
        print("Round", round)
        player = input("Select rock, paper, or scissors: ")
        computer = random.choice(["rock", "paper", "scissors"])
        print("Computer chose:", computer)
        if player == computer:
            print("It's a tie!")
        elif player == "rock" and computer == "scissors":
            print("You win!")
            player_score += 1
        elif player == "paper" and computer == "rock":
            print("You win!")
            player_score += 1
        elif player == "scissors" and computer == "paper":
            print("You win!")
            player_score += 1
        else:
            print("Computer wins!")
            computer_score += 1

    print("Final Score:")
    print("Your score:", player_score)
    print("Computer score:", computer_score)
    if player_score > computer_score:
        print("Congratulations! You won the game!")
    elif player_score < computer_score:
        print("Sorry! The computer won the game.")
    else:
        print("It's a tie game!")

game()




