'''
Luke Parkhurst
CS 5001 Intesive Foundations
Fall 2019
HW 3 Morse Code
'''
'''
TEST CASES:
Test Case 1: Input: dog                         Output:  -.. --- --.
Test Case 2: Input: cat is dog                  Output:  -.-. .- - / .. ... / -.. --- --.
Test Case 3: Input: Solid bananas               Output:  ... --- .-.. .. -.. / -... .- -. .- -. .- ...
Test Case 4: Input: Solid bananas in soup        Output:  ... --- .-.. .. -.. / -... .- -. .- -. .- ... / .. -. / ... --- ..- .--.
'''
# the code list contains all needed characters
code_list = [[' ',  '/'], ['A', '.-'], ['B', '-...'], ['C', '-.-.'], ['D', '-..'], ['E',  '.'], ['F', '..-.'], ['G', '--.'], ['H', '....'], ['I', '..'], ['J', '.---'], ['K', '-.-'], ['L', '.-..'], ['M', '--'], ['N', '-.'], ['O', '---'], ['P', '.--.'], ['Q', '--.-'], ['R', '.-.'], ['S', '...'], ['T', '-'], ['U', '..-'], ['V', '...-'], ['W', '.--'], ['X', '-..-'], ['Y', '-.--'], ['Z', '--..'], ['0', '-----'], ['1', '.----'], ['2', '..---'], ['3', '...--'], ['4', '....-'], ['5', '.....'], ['6', '-....'], ['7', '--...'], ['8',  '---..'], ['9', '----.'], ['?', '..--..'], ['!', '-.-.--'], ['\'', '.----.'], ['"',  '.-..-.'], [',', '--..--']] 
# the beginning of the morse code encryption function, takes a message for parameter
def morse_code(words):
    # set morse to a single space
    morse = ' '
    # searches for new variable letters inside words, creates flag variable, compares each letter
    # in the message to each subest in code list and if letter in subset, sets morse to be code
    # plus a space for the next letter, flag is true if loop finishes, otherwise is false and
    # tells user of invalid character
    for letters in words:
        flag = False
        for each in code_list:
            if letters in each:
                morse += each[1] + ' '
                flag = True
    if flag == False:
        print('Sorry, your entire message could not be encrypted due to a certain character! Below is the rest of your words in Morse!')
       
    # returns the morse message   
    return  morse

# beginning of output function used to collect user input        
def user_input():
    # requests user's input for message
    user_input = input('Please write the sentence you wish converted to Morse Code: \n')
    # returns input in uppercase if possible
    return user_input.upper()

# beginning of main function
def main():
    # prints out starting welcome message with options
    print('Welcome to Morse Code Hub! \n', 'Type; :q: to quit this menu!')
    # sets variable q1 to a single space
    q1 = ' '
    # sets first loop to as long as q1 is not :q:
    while q1 != [':Q:']:
        # prompts user for message input
        q1 = user_input()
        # if message is not :q:, continues with message being converted through morse code 
        # encryption function, and continues printing out finished encryption
        if q1 != ':Q:':
            q1 = morse_code(q1)  
            print(q1)
        # otherwise if message is :q:, prints goodbye message and breaks loop  
        else:
            print('Goodbye, thanks for using Morse Code Hub!')
            break
    
main()