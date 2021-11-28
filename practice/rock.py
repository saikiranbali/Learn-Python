# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

# Remember the rules:
#  1 and 3
#  2 and 1
#  3 and 2
# Rock beats scissors
# Paper beats rock
# Scissors beats paper


p1 = input("P1 : Enter your name : ")
p2 = input("P2 : Enter your name : ")
print("1. Rock\n2. Papper\n3. Scissors\n")
dec = ""
while dec != 'No': 
    choicep1 = int(input("\nP1 : Enter your choice : "))
    choicep2 = int(input("\nP2 : Enter your choice : "))
    if(choicep1==choicep2):
        print("Both are same\n")
        dec="Yes"
    elif((choicep2 == 1) or (choicep1 == 1) and (choicep2 == 3) or (choicep1 == 3)):
        if(choicep2>choicep1):
            print(p1 + " Wins")
        else:
            print(p2+" Wins")
        dec=input("Play Again (Yes or No) : ")
    elif((choicep2 == 1) or (choicep1 == 1) and (choicep2 == 2) or (choicep1 == 2)):
        if(choicep2>choicep1):
            print(p2 + " Wins")
        else:
            print(p1+" Wins")
        dec=input("Play Again (Yes or No) : ")
    elif((choicep2 == 3) or (choicep1 == 3) and (choicep2 == 2) or (choicep1 == 2)):
        if(choicep2>choicep1):
            print(p2 + " Wins")
        else:
            print(p1+" Wins")
        dec=input("Play Again (Yes or No) : ")
