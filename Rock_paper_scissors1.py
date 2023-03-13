p1_score = 0
p2_score = 0
valid_options = ["rock", "paper", "scissors"]

while p1_score != 3 and p2_score != 3:
    print("Chose rock, paper or scissors")

    valid_choice = True
    while valid_choice:
        player_one_choice = input("Player one, type your choice: ")
        if player_one_choice in valid_options:
            valid_choice = False

    valid_choice = True
    while valid_choice:
        player_two_choice = input("Player two, type your choice: ")
        if player_two_choice in valid_options:
            valid_choice = False

    if player_one_choice == "rock" and player_two_choice == "scissors" \
    or player_one_choice == "paper" and player_two_choice == "rock" \
    or player_one_choice == "scissors" and player_two_choice == "paper":
        print("Player one won")
        p1_score += 1

    elif player_one_choice == player_two_choice:
        print("Draw")

    else:
        print("Player two won")
        p2_score += 1

    print("Player 1 score:", p1_score, "Player 2 score:", p2_score)

if p1_score == 3:
    print("Player one won game")
else:
    print("Player two won game")