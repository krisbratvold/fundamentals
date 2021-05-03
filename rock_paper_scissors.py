import random

comp_wins = 0
wins = 0
while wins != 3 and comp_wins !=3:
    possible_actions = ["rock", "paper", "scissors"]
    comp_choice = random.choice(possible_actions)
    choice = input("rock, paper, or scissors?")

    if choice == comp_choice:
            print("You tie!")
    elif choice == "rock":
        if comp_choice == "scissors":
            wins += 1
            print("You win!")
        else:
            comp_wins += 1
            print("You lose!")
    elif choice == "scissors":
        if comp_choice == "paper":
            wins += 1
            print("You win!")
        else:
            comp_wins += 1
            print("You lose!")
    elif choice == "paper":
        if comp_choice == "rock":
            wins += 1
            print("You win!")
        else:
            comp_wins += 1
            print("You lose!")
else:
    if wins == 3:
        print("Champion!")
    elif comp_wins == 3:
        print("Loser!")