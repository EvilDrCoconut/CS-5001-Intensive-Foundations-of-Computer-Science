'''
CS 5003 Recitation
Fall 2019
Lab 3
'''

positive = ['fabulous', 'awesome', 'superb', 'excellent', 'exceptional', 'amazing', 'acceptable', 'visionary', 'best', 'profound', 'good', 'great', 'nice', 'rad', 'sick', 'ground-breaking', 'breathtaking', 'bodacious', 'entertaining', 'fun']
negative = ['bad', 'trash', 'insulting', 'cancerous', 'boring',  'disappointing', 'abysmal', 'awful', 'terrible', 'suck', 'sucked', 'waste', 'horrible', 'nightmare', 'yucky', 'tasteless', 'blase', 'money', 'worst', 'formulaic']


def analysis(words):
    
    i = 0

    for word in words:
        word = word.lower()


        if word in positive:
            i += 1
        elif word in negative:
            i -= 1
    return i
    

'''
def main():
    print(analysis(['fabulous', 'terrible', 'bad', 'bad',]))
    

main()
'''