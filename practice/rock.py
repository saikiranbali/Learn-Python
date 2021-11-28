# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

# Remember the rules:
#  1 and 3
#  2 and 1
#  3 and 2
# Rock beats scissors
# Paper beats rock
# Scissors beats paper

#Solution 1

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
    else:
        print("\nEnter a value b/w 1-3")
        dec="Yes"


#Solution 2
import sys

user1 = input("What's your name?")
user2 = input("And your name?")
user1_answer = input("%s, do yo want to choose rock, paper or scissors?" % user1)
user2_answer = input("%s, do you want to choose rock, paper or scissors?" % user2)

def compare(u1, u2):
    if u1 == u2:
        return("It's a tie!")
    elif u1 == 'rock':
        if u2 == 'scissors':
            return("Rock wins!")
        else:
            return("Paper wins!")
    elif u1 == 'scissors':
        if u2 == 'paper':
            return("Scissors win!")
        else:
            return("Rock wins!")
    elif u1 == 'paper':
        if u2 == 'rock':
            return("Paper wins!")
        else:
            return("Scissors win!")
    else:
        return("Invalid input! You have not entered rock, paper or scissors, try again.")
        sys.exit()

print(compare(user1_answer, user2_answer))

#Clever solution 3
print('''Please pick one:
            rock
            scissors
            paper''')

while True:
    game_dict = {'rock': 1, 'scissors': 2, 'paper': 3}
    player_a = str(input("Player a: "))
    player_b = str(input("Player b: "))
    a = game_dict.get(player_a)
    b = game_dict.get(player_b)
    dif = a - b

    if dif in [-1, 2]:
        print('player a wins.')
        if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
            continue
        else:
            print('game over.')
            break
    elif dif in [-2, 1]:
        print('player b wins.')
        if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
            continue
        else:
            print('game over.')
            break
    else:
        print('Draw.Please continue.')
        print('')