from random import randint
t = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
computer = random.choice(["Rock", "Paper", "Scissors", "Lizard", "Spock"])
player = False
while player == False:
    player = raw_input("Pick One:Rock, Paper, Scissors, Lizard, Spock")
    if player == computer:
        print("You Tied!")
    elif player == "Rock":
        if computer == "Paper":
            print("You Lose!", computer, "covers", player)
        elif computer == "Spock":
            print("You Lose!", computer, "vaporizes", player)
        else:
            print("You Win!", player, "smashes", computer)    
    elif player == "Paper":
        if computer == "Scissors":
            print("You Lose!", computer, "cuts", player)
        elif computer == "Lizard":
            print("You Lose!", computer, "eats", player)    
        else:
            print("You Win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You Lose!", computer, "smashes", player)
        elif computer == "Spock":
            print("You Lose!", computer, "smashes", player)    
        else:
            print("You Win!", player, "cuts", computer)
    elif player == "Lizard":   
        if computer == "Rock":
            print("You Lose!", computer, "crushes", player)
        elif computer == "Scissors":
            print("You Lose!", computer, "decapitates", player)
        else:
            print("You Win!", player, "kills", computer)  
    elif player == "Spock":    
        if computer == "Paper":
            print("You Lose!", computer, "disproves", player)
        elif computer == "Lizard":
            print("You Lose!", computer, "poisons", player)
        else:
            print("You Win!", player, "smashes", computer)        
    else:
        print("Invalid Play! Please check your spelling.")
player = False
computer =  t[randint(0,4)] 
