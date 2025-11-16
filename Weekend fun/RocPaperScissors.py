player_one = input("player one enter: rock, paper, or scissors: ")
player_two = inputplayer_one = input("player two enter: rock, paper, or scissors: ")

if(player_one == "rock" and player_two == "scissors"):
    print("player one wins")
elif(player_one == "rock" and player_two == "paper"):
    print("player two wins")
elif(player_one == "paper" and player_two == "scissors"):
    print("player two wins")
elif(player_one == "paper" and player_two == "rock"):
    print("player one wins")
elif(player_one == "scissors" and player_two == "paper"):
    print("player one wins")
elif(player_one == "scissors" and player_two == "rock"):
    print("player two wins")
else:print("tie")
    
