'''
Luke Parkurst
CS 5001
HW 5
Fall 2019
'''
'''
TEST CASES
Test Case 1: secret_code: 0123  guess: 3210     Cows: 4   Bulls: 0
Test Case 2: secret_code: 0123  guess: 0167     Cows: 0   Bulls: 2
Test Case 3: secret_code: 0123  guess: 0123     Cows: 0   Bulls: 4     Told: 'You Win'
Test Case 4: secret_code: 0123  guess: 023j     Cows: 0   Bulls: 0     Unexpected character: told to rechoose
'''
# imports the random functioon and counting bulls n cows from the bulls n cows file
import random; from bulls_n_cows import counting_bulls_n_cows

# beginning of the guesses function
def guesses():
    guess = [] # sets guess to an empty list

    while len(guess) < 4: # creates a while loop for while the length of guess is less than 4
        userinp = -1 # initializes userinp at -1 to start while loop
        while userinp > 9 or userinp < 0: # creates a while loop for user inp if less than 0 or greater than 9
            # creates a try funtion for user input which should be an integer
            try: userinp = (int(input('Choose a number from 0 to 9 (will be asked four times): ')))
            # creates an except function for value error if user attempts to put non numeric character
            except ValueError: print('Incorrect value, please choose a single number from 0 to 9 (will be asked for 4 values)')
            if userinp > 9 or userinp < 0: # creates an if function for if the user chooses an option greater than 9 and less than 0
                print('I said a number from 0 to 9 you dummy!') # reminds user of what they can choose
        guess.append(userinp) # appends the userinp to guess
    return guess # returns guess

# the start of the main function 
def main(): 
    # initializes the constants secret_code (which is a random sample to make sure it has different elements)
    # tries which is set to 0, and the guess_history as an empty list
    secret_code = random.sample(range(0, 9), 4);  tries = 0;  guess_history = []
    
    while  tries != 7: # creates a for loop until when tries reaches 7
        
        guess = guesses() # sets guess constant equivalent to returned value from guesses function

        # sets constants bulls and cows equivalent to the returned values from counting_bulls_n_cows functions
        bulls, cows = counting_bulls_n_cows(secret_code, guess) 
        
        # appeneds to guess_histoy the attempt number, the guess given, the number of bulls, and the number of cows as a list
        guess_history.append(['Attempt:', tries+1, guess, 'Bulls:',bulls, 'Cows:',cows])

        if bulls == 4: print('You Win!'); break # if the number of bulls is 4 (all matching numbers), prints you win and breaks loop
        else: print('Bulls: ', bulls, 'Cows: ', cows) # otherwise it prints the bulls and cows from the attempt

        for i in guess_history: print(i) # prints each list from the lists inside guess_book

        tries += 1 # adds one tries if winning number isn't reached
    
    if tries == 7: print('Sorry, you lose! The secret code was', secret_code, '!') # if tries reaches 7, prints 'you lose' and the actual secret code

main() # initializes main