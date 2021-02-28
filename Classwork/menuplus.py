def menu(message, options='123'):
    answer = input(message)
    answer = answer.upper # converts to uppercase for comparison
    if(answer[0] in options.upper()): # compare first letter if they enter more
        return answer, True
    return answer, False

def main():

    print('banana'[0])
    print('banana'[-1])
    print('banana'[-2])
    for each in 'banana':
        print(each)
    
    for i in range(5):
        print(i)
    for i in range(3, 6):
        print(i)
    for i in range(1, 21,3):
        print(i)

    '''
    question = ('How do you stay active?\n', '1: Running\n', '2: Bird Watching\n', '3: Swimming\n')
    answer, success = menu(question)
    print('You selected: ', answer)
    if(success):
        print('We were successful in understanding!')
    '''

main()
