import random
from random import choices
while True:
    choices = ["rock","paper","scissors"]    
    computer = random.choice(choices)
    player = None

    while player not in choices:
            print("Please, Enter any one in Rock, Paper , Scissors ")
            player = input( " rock, paper, scissors?: ").lower()

    if player == computer:
            print("computer: ", computer )
            print("player: ", player )
            print("Tie!!!")
    elif player == "rock":
            if computer == "scissor":
                print("computer: ", computer )
                print("player: ", player )
                print("You Win")
            if computer == "paper":
                print("computer: ", computer )
                print("player: ", player )
                print("You loose")
    elif player == "paper":
            if computer == "scissor":
                print("computer: ", computer )
                print("player: ", player )
                print("You Loose")
            if computer == "rock":
                print("computer: ", computer )
                print("player: ", player )
                print("You Win")
    elif player == "scissors":
            if computer == "paper":
                print("computer: ", computer )
                print("player: ", player )
                print("You Win")
            if computer == "rock":
                print("computer: ", computer )
                print("player: ", player )
                print("You Loose")
    play_again = input("Play again? (yes/no): ").lower()
    if play_again != "yes":
        break
print("Bye!!!")
