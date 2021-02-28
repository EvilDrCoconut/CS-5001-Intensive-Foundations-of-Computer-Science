'''
Luke Parkhurst
CS 5001
HW 5
Fall 2019
'''
# imports the needed files for the program
import random
from bulls_n_cows import counting_bulls_n_cows
# the list of guesses the computer will use
TEST_GUESSES = [[1,2, 3, 4], [5, 2, 3, 4], [7, 6, 5, 4], [0, 9, 8, 5],
                [2, 4, 6, 8], [1, 3, 5, 7], [1, 2, 0, 9]]
# the list of secret_codes the computer will use
TEST_SECRET = [[1, 9, 8, 7], [2, 4, 6, 7], [1, 2, 0, 9],[7, 6, 5, 4]]
# the beginning of the create guessbook functions, this creates a nested guessbook for the computer to input its attempts
def create_guessbook(guesses = 7):     
    guess_book = {}     # creates the dictionary guess_book
    for i in range(guesses):         # then iterates for each guess attempt, equivalent to 7
        entry = {}         # creates another dictionary call entry for that guess
        entry['GUESS'] =[] # will hold 4 or more ints # also creats the value for the computer's guess        
        entry['BULLS'] = 0  # creates a value to entry for the number of bulls in the guess
        entry['COWS'] = 0   # creates a value to entry for the number of cowes in the guess
        guess_book['GUESS ' + str(i)] = entry # then adds the entry to guess_book to create the nested dictionary
    return guess_book # returns the guess book once entry is created
 
# the beginning of the test count bulls and cows function 
def test_count_bulls_and_cows():
    secret_code = [5, 7, 4, 2]; tries = 0; history = [] # uses a chosen secret code, intializes tries, and starts the history of the guesses
    guesses = [[0, 1, 8, 3], [7, 2, 5, 4], [5, 7, 4, 2], [5, 2, 4, 7]] # intializes a set list of lists of computer guesses
    req = [[0, 0], [0, 4], [4, 0], [2, 2]] # initializes a list of lists for the required bulls and cows for each attempt

    for each in range(len(guesses)): # sets for loop for each list inside the list of guesses
        bulls, cows = counting_bulls_n_cows(secret_code, guesses[each]) # compares the secret code to the guess
        history.append([bulls, cows]) # adds the number of bulls and cows to the history
        print('Bulls: ', bulls, 'Cows: ', cows) # prints the number of bulls and cows per guess
    for i in range(len(history)) and range(len(req)): # compares the number of bulls and cows in history per guess to the reuired bulls and cows
        if history[i] == req[i]: tries += 0 # compares the list of bulls and cows to the required bulls and cows, adds 0 to tries if the required bulls and cows was met
        else: tries += 1 # else adds one to tries

    ''' Function test_count_bulls_and_cows
        Input: None.
        Returns: Number of failing test conditions for cow/bull sequences
        Do: Test various cow/bull sequences to ensure those counters
            are working as expected. Key cases: 0 cows, 0 bulls;
            4 cows, 0 bulls; 4 bulls, 0 cows, 2 cows, 2 bulls
    '''
    if tries == 0: return 0 # if tries equals 0 then returns 0
    else: return tries # else if tries is not 0, returns whatever tries is
        
# beginning of the auto play game function, requires the secret code and guess bokk dictionary
def auto_play_game(secret_code, guess_book):
    tries = 0 # initializes tries at 0
    
    while  tries != 7: # creates while loop for as long as tries is not 7
        
        guess = [] # initializes guess as an empty list
        for each in TEST_GUESSES: # for each list in the list in list of test_guesses
            guess = each # sets guess equivalent to each

            # then calls counting bulls n cows function, using the secret code and guess
            bulls, cows = counting_bulls_n_cows(secret_code, guess) # gives the constants bulls and cows their values 
            
            entry = guess_book['GUESS ' + str(tries)] # creates the key entry and puts it into guess_book with value of tries 
            entry['GUESS'] = guess # gives the value of GUESS to key entry
            entry['BULLS'] = bulls # gives the value fo BULLS to key entry
            entry['COWS'] = cows # gives the vale for COWS to key entry
            if bulls == 4: return True # if bulls is equal to 4, returns True

            tries += 1 # it True isn't returned, adds 1 to tries
    
        if tries == 7: return False # if tries reaches 7, returns False

    ''' Function auto_play_game
        Input:  secret_code (list of digits),
                guess_book (dictionary of guess history)
        Returns: True if auto-player a winner; False otherwise
        Do: Automate the playing of Bulls and Cows for regression
        testing. Instead of using interactive input from stdin, this
        function uses test data fed directly to the function to simulate
        an entire "systems test" and complete game flow
        Concept: instead of guess = input(...), now using
        guess = TEST_GUESSES[i]
    '''

# the beginning of the test regression bull cow function, takes the secret code
def test_regression_bull_cow(secret_code):

    guess_book = create_guessbook(7) # creates the constant guess_book using the create_guessbook function

    result = auto_play_game(secret_code, guess_book) # sets the result constant to the auto_play_game function, will be either True or False

    for each in guess_book: print(each, guess_book[each]) # prints each entry from the guess_book after game ends

    if result == True: # if result is True
        print('Computer won! This is not good for our future') # print that the computer won
    else: # otherwise if result is False
        print('Computer lost! HAHAHAHAHAHA') # print that it lost.....and laugh at it

    ''' Function test_regression_bull_cow
        Input: secret_code: secret to test with (the one we're "cracking").
        Returns: None
        Do: Automatically exercise and test the entire bulls n cows system
        by calling auto_play_game() multiple times with both "winning" and
        "losing" data. Printed output can then be "diff'd" and examined either
        manually or automatically via tool support
    '''
        
# beginning of the main function
def main():
    print('Beginning test suite. Testing count bulls and cows...') # tells user that its beginning test count bulls and cows
    fails = test_count_bulls_and_cows() # sets constant fails to value returned from test_bulls_and_cows function
    if fails > 0: # if fails is greater than 0
        print('Something went wrong. Pls go back and fix errors') # tell there is an error
    else: # otherwise print all tests passed
        print('Counting Bulls and Cows Passed All Tests')
    
    print('Beginning Auto Play Regression Tests') # tell user than the begining of auto play games is happening

    secret_code = tuple() # initiliazes secret code as a tuple
    for each in TEST_SECRET: # iterates for each list in the list of test_guesses
        for i in each: # iterates for each element (int) in the list of each
            secret_code += i, # adds i to secret code
        test_regression_bull_cow(secret_code) # runs the test regression bull function with the created secret code
        secret_code = tuple() # resets the secret code to an empty tuple

main() # intializes the main function
