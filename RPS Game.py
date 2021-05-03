
# Rock Paper Scissors game #
# Use the function get_hand to get the string representation of the user's and computer's hands #
# Call the function determine_winner to figure out who won #
# print out the player hand and computer hand #
# print out the winner #

import random

def get_hand(hand):
    # 0 = Scissor, 1 = rock, 2 = paper
    if hand == 0:
        return("scissors")
    elif hand == 1:
        return("rock")
    elif hand == 2:
        return("paper")



def determine_winner(player, comp):
    if player == 0:
        if comp == 0:
            return("nobody")
        elif comp == 1:
            return("computer")
        elif comp == 2:
            return("you")
    if player == 1:
        if comp == 0:
            return("you")
        elif comp == 1:
            return("nobody")
        elif comp == 2:
            return("computer")
    if player == 2:
        if comp == 0:
            return("computer")
        elif comp == 1:
            return("you")
        elif comp == 2:
            return("nobody")


player_Hand = 0

while player_Hand != 5:

    player_Hand = int(input("Choose what to throw! (0 = Scissors, 1 = rock, 2 = paper, or 5 to exit): "))

    if player_Hand == 5:
        break

    comp_Hand = random.randint(0, 2)

    player = get_hand(player_Hand)
    comp = get_hand(comp_Hand)

    winner = determine_winner(player_Hand, comp_Hand)


    print(f'You chose {player}!')
    print(f'Computer chose {comp}!')
    print(f'{winner.capitalize()} won!')