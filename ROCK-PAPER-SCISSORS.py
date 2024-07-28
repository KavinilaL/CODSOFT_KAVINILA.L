import random

options =("rock","paper","scissors")
running True

while running:
   
    player = None
    computer = random.choice(options)
   
    while player not in options:
        player = input("Enter a choice(rock, paper,scissors"):")
       
    print(f"player:{player}")
    print(f"compter:{computer}")

    if player == computer:
        print("it is a TIE!!")
    elif player == "rock" and compter == "scissors":
        print(" you win!!")
    elif player == "paper" and compter == "rock":
        print(" you win!!")
    elif player == "scissors" and compter == "paper":
        print(" you win!!")
    else:
        print("You lose!")
    k = input("play again? (y/n):")
    if(k.lower() != "y"):
        running = False
       
        print("Thanks For Playing!")
