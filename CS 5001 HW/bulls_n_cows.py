'''
Luke Parkhurst
CS 5001
HW 5
Fall 2019
'''
'''
TEST CASES
Test Case 1: secret_code: 0123  guess: 3210     Cows: 4   Bulls: 0
Test Case 2: secret_code: 0123  guess: 0167     Cows: 0   Bulls: 2
Test Case 3: secret_code: 0123  guess: 1023     Cows: 2   Bulls: 2
Test Case 4: secret_code: 0123  guess: 0123     Cows: 0   Bulls: 4
'''
# start of the counting bulls and cows function, requires the users' (or computer's) guess and the secret code used
def counting_bulls_n_cows(secret_code, guess):
    # sets variables of bulls and cows to 0
    bulls = 0; cows = 0
    # creats a loop for all indexes in both guess and secret code
    for i in range(len(guess)) and range(len(secret_code)):
        if guess[i] == secret_code[i]: bulls += 1 # if the indexed part of the guess matches the indexed part of secret code, adds one to bull
        elif guess[i] in secret_code: cows += 1 # else if, the indexed part of guess is in secret code, adds one to cows
    
    return bulls, cows # returns both variables for bulls and cows