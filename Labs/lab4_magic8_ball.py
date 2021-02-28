'''
CS 5001 
Fall Semester
Lab 4
'''
import random
import sys

responses = ['As I see it, yes.', ' Ask again later.', 'Better not tell you now.', 'Cannot predict now.', 'Concentrate and ask again.', 'Don’t count on it.', 'It is certain.', 'It is decidedly so.', 'Most likely.', 'My reply is no.', 'My sources say no.', 'Outlook not so good.', 'Outlook good.', 'Reply hazy, try again.', 'Signs point to yes.', 'Very doubtful.', 'Without a doubt.', 'Yes.', 'Yes – definitely.', 'You may rely on it.'] 

def word_muncher():
    word = random.randint(0, (len(responses) - 1))
    return responses[word]

def main():

    user_inp = ' '
    
    while user_inp != '':

        user_inp = input("What's your question, mortal? \n")
        
        print(word_muncher())
    

main()