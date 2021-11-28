# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)

# Extras:

# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, print this out.

import random

val = random.randint(1,9)
dec = 0
guess = '3'
while guess != 'exit':
    guess = input("guess generated number : ")
    if(int(guess)>9 or int(guess)<1):
        print("Please enter 1-9")
    elif(int(guess)==val):
        print("Guessed exact value")
        dec +=1
        guess = "exit"
    elif(int(guess)>val):
        print("Guessed High")
        dec += 1
    elif(int(guess)<val):
        print("Guessed Low")
        dec +=1
    
print("Guess after "+str(dec)+" attempts")