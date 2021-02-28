'''
CS 5001 
Lab 5
Fall 2019
'''

english = ['hello', 'friend', 'hey', 'awful', 'wow','reward', 'song', 'money', 'board', 'cocktail', 'bathroom', 'friends', 'cheat', 'flag','boy', 'girl', 'my', 'take', 'sink', 'telescope', 'clean', 'you'] 
pirate = ['ahoy', 'matey', 'avast', 'bilge-sucking', 'blimey', 'booty', 'chanty', 'dubloon', 'plank', 'grogg', 'head', 'hearties', 'hornswaggle', 'jack', 'lad', 'lass', 'me', 'plunder', 'scuttle', 'spyglass', 'swob', 'ye']



def translator(words):
    translated = ''
    translate = {}
    for i in range(len(english)):
        translate[english[i]] = pirate[i]

    for word in words:
        if word in translate.keys():
            translated += translate[word] + ' '
        else:
            translated += words + ' '
    return translated


def main():

    print("Ahoy maties! Ready to learn how to speak pirate? Type in yer phrase belo' and see how the kinds o' the sea say it!")

    user_inp = ''

    while True:

        user_inp = input()
        
        if user_inp == 'arr':
            break

        user_inp = user_inp.split()
        translated = translator(user_inp)
        print(translated)
    
    print("Ye better be speakin pirate now, scallywag!")    

main()