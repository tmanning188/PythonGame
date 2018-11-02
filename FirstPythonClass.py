import random


def rps_check(player, comp):

    if player == "rock" and comp == "scissors":
        return "You win!"
    elif player == "paper" and comp == "rock":
        return "You win!"
    elif player == "scissors" and comp == "paper":
        return "You win!"
    elif player == comp:
        return "Tie!"
    else:
        return "The computer wins!"


def comp_choice():

    num = random.randrange(1, 4)

    if num == 1:
        return "rock"
    elif num == 2:
        return "paper"
    else:
        return "scissors"


player_wins = 0
comp_wins = 0
total_games = 0


while True:

    player_input = (input("Please type rock, paper, or scissors:\n")).lower()
    flag = True

    while flag:
        if player_input == "rock":
            flag = False
        elif player_input == "paper":
            flag = False
        elif player_input == "scissors":
            flag = False
        else:
            player_input = input("Please enter a valid input:\n")

    comp_input = comp_choice()
    print("The computer chose " + str(comp_input) + "!")
    print(rps_check(player_input, comp_input))

    if str(rps_check(player_input, comp_input)) == "You win!":
        player_wins += 1
        total_games += 1
    elif str(rps_check(player_input, comp_input)) == "The computer wins!":
        comp_wins += 1
        total_games += 1
    else:
        total_games += 1

    print("You won " + str(player_wins) + " game(s) out of " + str(total_games) + ".\n")
    flag = True
    print("Would you like to play again?")
    player_input = (input("yes or no:\n")).lower()

    while flag:
        if player_input == "yes":
            flag = False
        elif player_input == "no":
            flag = False
        else:
            player_input = input("Please enter a valid input:\n")

    if player_input == "no":
        break
