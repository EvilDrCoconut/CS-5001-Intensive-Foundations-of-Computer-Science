'''
Luke Parkhurst
CS 5001
HW 6
Fall 2019
'''
# set up the points library for the get_word_value function
points = {}
for x in ['A','E','I','O','U','L','N','S','T','R' ]: points[x] = 1
for x in ['D','G']: points[x] = 2
for x in ['B','C','M','P']: points[x] = 3
for x in ['F','H','V','W','Y']: points[x] = 4
points['K'] = 5
for x in ['J','X']: points[x] = 8
for x in ['Q','Z']: points[x] = 10

# beginning of the bag of letters function to create the bag of 100 characters
def bag_of_letters(alphabet):
    letters = [] # starts an emypt list letters

    for k, v in alphabet.items(): #creates a for loop for key,value pairs
        while v > 0: # while the key's( letter's) value is above zero
            letters.append(k) # append the key (letter) to the list of characters
            v -= 1 # subtract one off the value

    return letters # return letters list

# beginning of the get_word_value function
def get_word_value(word, current_letters):
    word = word.upper() #sets the passed in word to uppercase
    score = 0 # creates zeroed variable for score tally
    for letter in word: # sets a loop for each letter in a word
        if letter not in current_letters: # if that letter is not in current_letters list
            print('This letter', letter, 'is not in your current letters! Try again!') # tell player
            return 0 # and return a zero score value
        else: # otherwise
            continue #ignore and continue function
    for letter in word: # for letter in word loop
        if letter in points: # if the letter is in the dictionary of points
            score += points[letter] # increase score by the numnber of pouints that letter was worth
    return score # return the score value
