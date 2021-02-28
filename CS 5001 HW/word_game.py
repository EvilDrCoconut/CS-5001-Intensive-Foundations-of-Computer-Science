'''
Luke Parkhurst
CS 5001
HW 6
Fall 2019
'''
'''
TEST CASES:
Test Case 1: Word: LET         Points: 3
Test Case 2: Word: COT         Points: 5
Test Case 3: Word: FAME        Points: 9
Test Case 4: Word: WI(blank)D  Points: 8
'''

# import all needed functions and random to help with choice function later
from scrabble_points import bag_of_letters
from scrabble_points import get_word_value
import random

# start of the create_alphabet function
def create_alphabet():
    alphabet = {} # sets the dictionary of alpahbet and gives key, value pairs
    alphabet['E'] = 12
    for x in ['A','I']: alphabet[x] = 9
    alphabet['O'] = 8
    for x in ['N','R','T']: alphabet[x] = 6
    for x in ['D','S','L','U']: alphabet[x] = 4
    alphabet['G'] = 3
    for x in ['B','C','F','H','M','P','V','W','Y','blank']: alphabet[x] = 2
    for x in ['J','K','Q','X','Z']: alphabet[x] = 1
    return alphabet # returns alphabet dictionary

# beginning of the create word_list function
def create_word_list():
    word_list = [] # starts the empty word list
    infile = open('wordlist.txt', 'r') # opens the wordlist file and sets it to variable infile
    for line in infile: # creates for loop for line in infile
        word_list.append(line) # appends each line to word_list
    infile.close() # closes the infile
    word_list = [s.rstrip() for s in word_list] # strips the list of all whitespace characters
    return word_list  # returns thw word_list

# start of the user menu function
def menu():
    allowed_cmmds  = ['W','P','D','Q'] # creates list of allowed commands then asks for user input and gives lists of choices
    userinp = input('Your options are as follows: D to draw 7 more letters \n W to make a new word to from your current letters \n P to print the list of currently made words, their point values, and your current score! \n Q to quit this expiriment (but who would!?) \n')
    userinp = userinp.upper() # turns user input into upper case
    if userinp not in allowed_cmmds: #checks to see if user input is a allowed command
        print('That is, not, an option!') # tells them if it's an invalid option
    return userinp # returns userinp

# beginning of the current_letters_mixer function, meant to help create a new current_letters list
def current_letters_mixer(current_letters, letters):
        if len(letters) < 7: # checks to see if there are at least 7 letters left in bag of letters
            print('Unable to give a new full set, you only have', len(letters), 'letters left!') # tells user if unable to give 7 more letters
        else: # otherwise
            current_letters = [] # sets empty list for current_letters
            while len(current_letters) < 7: # creates while loop for if the length og current_letters is less than 7
                t = random.choice(letters) # sets variable t to equal a random letter from the letters bag
                letters.remove(t) # removes that character from the letters bag
                current_letters.append(t) # appends the character to the current_letters list
        return current_letters # returns current_letters

# beginning of the make_words command where the user can make words
def make_words(current_letters, word_list,words_made, letters, total_score, alphabet):
            total_score = total_score # sets in function total score to total score
            if len(current_letters) == 0: # if length of current_letters is 0, tells player to go draw some letters
                print('You need some letters first!')
            else: # otherwise
                print(current_letters) # prints current letters
                for x in current_letters: # for loop on each current letter
                    if x == 'blank': # if one of the letters is a 'blank' token
                        inp = '' # empty variable for while loop
                        while inp not in ['Y','N']: # while loop for userinp to by yes (Y) or no (N)
                            blank_counter = 1 # sets blank number to one in case user has 2 blank tokens in current letters
                            inp = input("Would you like to change 'blank' to a letter? Y or N  ") # asks user if they would like to change 'blank' token
                            inp = inp.upper() # sets inp to uppercase
                            if inp not in ['Y','N']: # if user does not type y or n
                                print('Please choose yes (Y), or no (N)') # asks user to choose y or n
                            if inp == 'Y': # if inp is y
                                letter = 'letter' # creates letter variable for while loop
                                while len(letter) > 1 or letter not in alphabet: # while letter is greater than 1 (forces user to have a 1 character input)
                                    letter = input("What would you like 'blank' to be as a letter?  ") # sets letter to input for user choice
                                    letter = letter.upper() # puts letter into uppercase
                                    if len(letter) > 1 or letter not in alphabet: # checks to see if input is both one character and an allowed letter
                                        print('A single letter that is a letter!') # notifies if it isn't a valid choice
                                current_letters.remove('blank') # removes the 'blank' token
                                current_letters.append(letter) # adds the new letter
                                print("For blank", blank_counter, 'it is replaced with letter', letter) # notifies blank was changed for requested input
                                blank_counter += 1 # adds one to blank counter in case a 2nd blank is in list
                                print(current_letters) # prints new current letters
                            if inp == 'N': # if userinp is N
                                print('okay!') # say 'Okay' and move on

                word = input('Make a word with your letters! ') # set variable word to input
                word = word.lower() # turn word into lower case to compare to word_list
                if word not in word_list(): # checks to see if word is in word_list
                    print('Sorry, this was not an accounted for word (or possibly even a word at all...)') # if not, tells user so
                elif word in words_made: # also checks if the word was already made
                    print('Hey, you already made this word! Try again!') # and tells user if so
                else: # otherwise
                    word = word.upper() # sets word to uppercase
                    score = get_word_value(word, current_letters) # uses the get_word_value function to get score
                    if score == 0: # if score is returned zero
                        return 0 # then return 0
                    else: # otherwise
                        words_made[word] = score # uses the words_made function on word to find score
                        print('You current points from', word, 'are', score,'points!') # tells user of points earned and from what word
                        total_score += score # adds new score from score to total_Score
                        word.split() # splits the word so letters can be easily removed
                        for x in word: # for loop for letters in word
                            current_letters.remove(x) # removes letters in word from current letters
                        while len(current_letters) < 7: # while loop for current_letters if length is not 7
                            t = random.choice(letters) # sets variable t to a random choosen letter from letters
                            letters.remove(t) # removes the letter from letters list
                            current_letters.append(t) # adds the letter to the current letters list
                    print('New set of current letters: \n', current_letters) # print the new current letters
                return total_score # return the new total score


# beginning of the main function
def main():
    # creates all needed variables for the game by calling on respective functions
    alphabet = create_alphabet(); word_list = create_word_list; letters = bag_of_letters(alphabet); current_letters = []; words_made = {}; userinp = ''; total_score = 0

    # welcomes the user to the game and explains the rules
    print("Welcome to this Frakenstein word game of countdown and scrabble! You have been unfortunately chosen to partake in this expiriment!")
    print('The point of this game is to use the letters given to you (7 at a time) to make words. Each word is rewarded with points. \n After a word is made, the used letters disappear and new ones will replace them. \n There are 100 letters in total, and you must make as many words as possible. \n If a word is not recognized, your letters are returned and no points are given. \n If, however, you can not make a word, you can draw 7 more letters and discard your current letters.')
    
    while userinp != 'Q': # while userinp is not Q
        userinp = menu() # sets userinp to the menu function

        if userinp == 'D': # if userinp is D
            current_letters = current_letters_mixer(current_letters, letters) # creates the current letters lists with the current_letters_mixer function
            print('New set of current letters: \n', current_letters) # prints the user's new current letters

        if userinp == 'W': # if userinp is W, then calls the make_word function allowing user to make words
            total_score = make_words(current_letters, word_list, words_made, letters, total_score, alphabet)

        if userinp == 'P': # if userinp is P
            for k, v in words_made.items(): # starts a for loop for each key, value pair in words_made dictionary
                print(k,':', v, 'points') # prints the key (words made), value (points for that word) pairs
            print('Current score:', total_score) # prints current total score
        
        if userinp == 'Q': # if userinp is Q, thanks player for playing and exits giving total score
            print('Thanks for playing! Your total score was', total_score, 'points!')
            break
        if len(letters) == 0 and len(current_letters) == 0: # if both letters list and current_letters list are empty
            print('You are completely out of letters!') # tells user they are out of letters
            print('Thanks for playing! Your total score was', total_score, 'points!') # thanks user and prints points
            break # breaks in case loop goes funky

main()