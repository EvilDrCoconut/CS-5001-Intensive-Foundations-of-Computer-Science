'''
Luke Parkhurst
CS 5001 Intensive Foundations
Fall 2019
HW 3 PIG
'''
'''
TEST CASE:
Test 1:
Test 2:
Test 3:
Test 4:
'''
# imports the random module
import random

# creates a function called roll for rolling the dice using random function
def roll():
    return random.randint(1, 6)

def main():
    
    # prints the welcome banter to the game, then tells 1st player of thier turn
    print('Welcome to PIG, the dice rolling game. \n', 'To play, type R to roll a 6 sided die, and H to hold your current points. \n', 'Watch out! Rolling a 1 means you lose all your accumalated points and pass the die to the next player! \n', 'The first person to 20 points wins!')
    print('__________________________________________________________')
    print('Player 1, you go first! \n', "Press 'R' to roll, press 'H' to hold!" )
 
    # constants to hold player score and gathered score
    player1_score = int(0)
    player2_score = int(0)
    points_gathered = int(0)
    
    # flag to help create while statement
    won = 0

    # while loop set up with won flag set to 0
    while won == 0 :
        # while loop set up as player 1's score is under 20
        while player1_score < 20:

            #user input for player one
            user_inp = input('Player 1, would you like to "R" roll, or "H" hold? \n').upper()

            # if player one chooses roll, it rools the die, points is the rolled number, if points
            # rolls a one, ends player one's turn, sets points gathered to 0 and moves to player two, 
            # else adds points to points gathered and asks player one again to roll or hold,
            if user_inp == 'R':
                points = int(roll())
                if points ==  1:
                    points = 0
                    points_gathered = 0
                    print("Sorry, you rolled a 1! It is the next player's turn!")
                    print("Player 1's current score is: ", player1_score)
                    print('________________________________________________')
                    break
                else:
                    print(' You earned ', points, 'points!')
                    points_gathered += points
                    points = 0
                
                # if player 1 score is equal to or above 20, gives win message and sets won flag to 1
                if (player1_score + points_gathered) >= 20:
                    print('Player 1 wins with a score of ', (player1_score + points_gathered), 'points!')
                    print('Thanks for playing!')
                    won = 1
                    break
                continue

            # if player one holds, points gathered added to player score, moves to player 2's turn
            # sets points gathered to 0 
            if user_inp == 'H':
                player1_score += points_gathered
                points_gathered = 0
                print("Player 1's current score is: ", player1_score)
                print('________________________________________________')
                print("It is the next player's turn!")
            break

        # while loop set up as player 2's score is under 20
        while player2_score < 20:
            
            # asks for player 2's user input
            user_inp = input('Player 2, would you like to "R" roll, or "H" hold? \n').upper()

            # if player two chooses roll, it rools the die, points is the rolled number, if points
            # rolls a one, ends player two's turn, sets points gathered to 0 and moves to player two, 
            # else adds points to points gathered and asks player two again to roll or hold,        
            if user_inp == 'R':
                points = int(roll())
                if points ==  1:
                    points = 0
                    points_gathered = 0
                    print("Sorry, you rolled a 1! It is the next player's turn!")
                    print("Player 2's current score is: ", player2_score)
                    print('________________________________________________')
                    break
                else:
                    print(' You earned ', points, 'points!')
                    points_gathered += points
                    points = 0
                
                # if player 2 score is equal to or above 20, gives win message and sets won flag to 1
                if (player2_score + points_gathered) >= 20:
                    print('Player 2 wins with a score of ', (player2_score + points_gathered), 'points!')
                    print('Thanks for playing!')
                    won = 1
                    break
                continue

            # if player one holds, points gathered added to player score, moves to player 2's turn
            # sets points gathered to 0 
            if user_inp == 'H':
                player2_score += points_gathered
                points_gathered = 0
                print("Player 2's current score is: ", player2_score)
                print('________________________________________________')
                print("It is the next player's turn!")
            break



main()