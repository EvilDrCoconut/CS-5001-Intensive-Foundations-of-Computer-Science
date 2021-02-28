'''
CS 5003 Recitation
Fall semester 2019
Lab 3 Part 1
'''
'''
TEST CASES:
Test Case 1: Expected: , Actual: 
Test Case 2: Expected: , Actual: 
Test Case 3: Expected: , Actual: 
Test Case 4: Expected: , Actual: 
'''
def is_palindrome(word):

    reversed_word = ""

    for letter in word:
        reversed_word = letter + reversed_word
    print(reversed_word)

    if reversed_word == word:
        print('True!')
    elif reversed_word != word:
        print('False!')

def main():
    is_palindrome('racecar')

main()