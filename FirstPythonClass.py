import random


def rpc_check(player, comp):

    if player == "rock" and comp == "scissors":
        print("You win!")
    elif player == "paper" and comp == "rock":
        print("You win!")
    elif player == "scissors" and comp == "paper":
        print("You win!")
    elif player == comp:
        print("Tie!")
    else:
        print("The computer wins!")


def comp_choice():

    num = random.randrange(1, 4)

    if num == 1:
        return "rock"
    elif num == 2:
        return "paper"
    else:
        return "scissors"


while True:

    player_input = input("Please type rock, paper, or scissors:\n")
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
        rpc_check(player_input, comp_input)

    flag = True
    print("Would you like to play again?")
    player_input = input("yes or no:\n")

    while flag:
        if player_input == "yes":
            flag = False
        elif player_input == "no":
            flag = False
        else:
            player_input = input("Please enter a valid input:\n")

    if player_input == "no":
        break
