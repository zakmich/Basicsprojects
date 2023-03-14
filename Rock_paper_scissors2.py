p1_score = 0
p2_score = 0

valid_options = ["rock", "paper", "scissors"]

def choice_input(player):
    while True:
        player_choice = input(f"{player}, type your choice: ")
        if player_choice in valid_options:
            return player_choice
def whow_win(player_one_choice, player_two_choice):
    if player_one_choice == player_two_choice:
        print("Draw")
        return 0

    possibilities = {
        ("rock", "scissors"): 1,
        ("paper", "rock"): 1,
        ("scissors", "paper"): 1
        }

    return possibilities.get((player_one_choice, player_two_choice), 2)


while p1_score != 3 and p2_score != 3:
    print("Chose rock, paper or scissors")
    player_one_choice = choice_input("Player one")
    player_two_choice = choice_input("Player two")
    score = whow_win(player_one_choice, player_two_choice)

    if score == 1:
        print("Player one won")
        p1_score += 1
    elif score == 2:
        print("Player two won")
        p2_score += 1

    print("Player 1 score:", p1_score,"|" " Player 2 score:", p2_score)

if p1_score == 3:
    print("Player one won game")
else:
    print("Player two won game")