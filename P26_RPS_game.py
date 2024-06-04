import random


def main():
    while True:
        choices = ["rock", "paper", "scissor"]
        computer = random.choice(choices)
        player = None

        while player not in choices:
            player = input("Enter your choice: ").lower()

        if player == computer:
            print("your choice matches with the computer")
        elif player == "rock":
            if computer == "paper":
                print("computer: ", computer)
                print("player: ", player)
                print("you lose")
            if computer == "scissor":
                print("computer: ", computer)
                print("player: ", player)
                print("you win")
        elif player == "paper:":
            if computer == "rock":
                print("computer: ", computer)
                print("player: ", player)
                print("you win")
            if computer == "scissor":
                print("computer: ", computer)
                print("player: ", player)
                print("you lose")
        elif player == "scissor":
            if computer == "rock":
                print("computer: ", computer)
                print("player: ", player)
                print("you lose")
            if computer == "paper":
                print("computer: ", computer)
                print("player: ", player)
                print("you win")
        while True:
            play_again = input("Do you want to play again: ").lower()
            if (play_again == "yes" or play_again == "no"):
                break
        if play_again != "yes":
            break

if __name__ == '__main__':
    main()
