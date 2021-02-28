'''
Luke Parkhurst
CS 5001 Intesive Foundations
Fall 2019
HW 3 Morse Code
'''
'''
TEST CASES:
Test Case 1: Input: hello world                                                             Output:  .... . .-.. .-.. --- / .-- --- .-. .-.. -..
Test Case 2: Input: banana phone                                                            Output:  -... .- -. .- -. .- / .--. .... --- -. .
Test Case 3: Input:  -.-. .- - / -- .- -. / -.. --- --. / ..-. .. ... ....                  Output:  C A T   M A N   D O G   F I S H
Test Case 4: Input:  ... --- .-.. .. -.. / .--. --- - .- - --- . / ... --- -.-. -.- ...     Output:  S O L I D   P O T A T O E   S O C K S
'''
# the code list contains all needed characters
code_list = [[' ',  '/'], ['A', '.-'], ['B', '-...'], ['C', '-.-.'], ['D', '-..'], ['E',  '.'], ['F', '..-.'], ['G', '--.'], ['H', '....'], ['I', '..'], ['J', '.---'], ['K', '-.-'], ['L', '.-..'], ['M', '--'], ['N', '-.'], ['O', '---'], ['P', '.--.'], ['Q', '--.-'], ['R', '.-.'], ['S', '...'], ['T', '-'], ['U', '..-'], ['V', '...-'], ['W', '.--'], ['X', '-..-'], ['Y', '-.--'], ['Z', '--..'], ['0', '-----'], ['1', '.----'], ['2', '..---'], ['3', '...--'], ['4', '....-'], ['5', '.....'], ['6', '-....'], ['7', '--...'], ['8',  '---..'], ['9', '----.'], ['?', '..--..'], ['!', '-.-.--'], ['\'', '.----.'], ['"',  '.-..-.'], [',', '--..--']] 

# the beginning of the morse code encryption function, takes a message for parameter
def morse_code(words):
    # set morse to a single space
    morse = ' '

    # searches for new variable letters inside words, creates flag variable, compares each letter
    # in the message to each subest in code list and if letter in subset, sets morse to be code
    # plus a space for the next code piece, flag is true if loop finishes, otherwise is false and
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


# beginning of alpha code decryption function, takes morse code message for parameter
def alpha_code(words):
    #sets words to start with and extra space to get last character
    words += ' '
    # sets a new variable, alpha, to a single space
    alpha = ' '

    # searches for new variable, letters, inside words which is now properly split, 
    # creates flag variable, compares each morse code piece (letter) in the message 
    # to each subest in code list, and if morse code piece is in subset, sets morse code piece 
    # to character and adds it to alpha, flag is true if loop finishes, 
    # otherwise is false and tells user of invalid character
    for letters in words.split():
        flag = False
        for each in code_list:
            if letters in each:
                alpha += each[0] + ' '
                flag = True
    if flag == False:
        print('Sorry, your entire message could not be encrypted due to a certain character! Below is the rest of your words in Morse!')

    # returns alpha, the completed line of letters   
    return  alpha

# beginning of output function used to collect user input        
def user_input():
    # requests user's input for message
    user_input = input('Please write the sentence you wish converted: Type ":q:" to return to menu\n')
    # returns input in uppercase if possible
    return user_input.upper()

# beginning of the main function
def main():
    # prints out starting welcome message with options
    print('Welcome to Morse Code Hub! \n', 'Type: "Encrypt" to turn message to Morse Code! \n', 'Type: "Decrypt" to turn a Morse Code message back to alphanumeric! \n','Type; ":q:" to quit this menu!')
    # sets variable user input to empty string
    user_inp = ''
    # creates loop for as long as user input isn't :Q:
    while user_inp != ':Q:':
        # prompts user for input, creats it into string, puts into upper case
        user_inp = input(str()).upper()

        # creates a list of accepted strings, if user input is not in list, tell's them to rewrite
        if user_inp not in ['ENCRYPT', 'DECRYPT', ':Q:']:
            print("Sorry, I didn't understand what you typed, please type 'Encrypt', 'Decrypt', or ':q:'!")
        # sets variable q1 to empty string    
        q1 = ''
        # creates loop for when user input is encrypt
        while user_inp == 'ENCRYPT':
            # prompts for user input
            q1 = user_input()
            # if user input is not :Q:, runs morse code funtion and prints message to morse code 
            # before continuing the cycle
            if q1 != ':Q:':
                q1 = morse_code(q1)  
                print(q1)
                continue
            # if user input is :q: creates homescreen with menu options
            else:
                print('Welcome to Morse Code Hub! \n', 'Type: "Encrypt" to turn message to Morse Code! \n', 'Type: "Decrypt" to turn a Morse Code message back to alphanumeric! \n','Type; ":q:" to quit this menu!')
                user_inp = input(str()).upper()
            
            # if user input is originally :q:, breaks loop and returns with menu options   
            if user_inp == ':Q:':
            
                break
            # creates a list of accepted strings, if user input is not in list, tell's them to rewrite
            print('Welcome to Morse Code Hub! \n', 'Type: "Encrypt" to turn message to Morse Code! \n', 'Type: "Decrypt" to turn a Morse Code message back to alphanumeric! \n','Type; ":q:" to quit this menu!')
            if user_inp not in ['ENCRYPT', 'DECRYPT', ':Q:']:
                print("Sorry, I didn't understand what you typed, please type 'Encrypt', 'Decrypt', or ':q:'!")
        
        # creates variable q2 with an empty string value
        q2 = ''
        
        # creates a loop for as long as user input is decrypt
        while user_inp == 'DECRYPT':
            # prompts for user input
            q2 = user_input()
            
            # if user input is not :Q:, runs alpha code funtion and prints morse code to message 
            # before continuing the cycle            
            if q2 != ':Q:':
                q2 = alpha_code(q2)  
                print(q2)
                continue
            # if user input is :q: creates homescreen with menu options            
            else:
                print('Welcome to Morse Code Hub! \n', 'Type: "Encrypt" to turn message to Morse Code! \n', 'Type: "Decrypt" to turn a Morse Code message back to alphanumeric! \n','Type; ":q:" to quit this menu!')
                user_inp = input(str()).upper()

            # if user input is originally :q:, breaks loop and returns with menu options                   
            if user_inp == ':Q:':
                break
            
            # creates a list of accepted strings, if user input is not in list, tell's them to rewrite
            print('Welcome to Morse Code Hub! \n', 'Type: "Encrypt" to turn message to Morse Code! \n', 'Type: "Decrypt" to turn a Morse Code message back to alphanumeric! \n','Type; ":q:" to quit this menu!')
            if user_inp not in ['ENCRYPT', 'DECRYPT', ':Q:']:
                print("Sorry, I didn't understand what you typed, please type 'Encrypt', 'Decrypt', or ':q:'!")

        # if user input is :Q: anytime throuhgout main terminal screen, breaks loop with goodbye message 
        if user_inp == ':Q:':   
            break
    print('Goodbye, thanks for using Morse Code Hub!') 

main()