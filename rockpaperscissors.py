player_1 = input("Player 1, choose rock, paper, or scissors!")
player_2 = input("Player 2, choose rock, paper, or scissors!")

player_1 = player_1.lower()
player_2 = player_2.lower()

if player_1 == "rock" and player_2 == "rock":
    print ("Tie!")
elif player_1 == "rock" and player_2 == "paper":
    print ("Player 2 wins!")
elif player_1 == "rock" and player_2 == "scissors":
    print ("Player 1 wins!")
elif player_1 == "paper" and player_2 == "paper":
    print ("Tie!")
elif player_1 == "paper" and player_2 == "rock":
    print ("Player 1 wins!")
elif player_1 == "paper" and player_2 == "scissors":
    print ("Player 2 wins!")
elif player_1 == "scissors" and player_2 == "scissors":
    print ("Tie!")
elif player_1 == "scissors" and player_2 == "rock":
    print ("Player 2 wins!")
elif player_1 == "scissors" and player_2 == "paper":
    print ("Player 1 wins!")

