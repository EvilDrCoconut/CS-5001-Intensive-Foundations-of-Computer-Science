'''
CS 5003
Lab 2
Fall 2019
'''
def menu(question):
    print(question)
    steak = input('Your answer: A or B: ')
    user_answer = steak.upper()
   
    if user_answer != 'A' and user_answer != 'B':
        print('Please type in the letter corresponding with your answer!')
        user_answer = 'A'
    
    print('You selected: ', user_answer)
    return user_answer


def main():
    print("Let's have a fun questionnaire! What type of sandwich are you!?")
    print('________________________________________________________________________')

    q1 = ('How do you like your cookies?\n' + 'A: Soft!\n' + 'B: Crunchy!\n')
    a1 = menu(q1)

    q2 = ('What type of life do you live?\n' + 'A: Regular\n' + 'B: Spicy\n')
    a2 = menu(q2)

    q3 = ('How do you make decisions?\n' + 'A: Rigid Schedule\n' + 'B: Go with the flow\n')
    a3 = menu(q3)
    
    answer = a1 + a2 + a3
    
    if answer == 'AAA':
        print("You are a ham sandwich!")
    elif answer == 'AAA':
        print('You are a italian sandwich!')
    elif answer == 'ABB':
        print("You are a burrito!")
    elif answer == 'BBB':
        print("You are a acuautlly a taco!")
    elif answer == 'BBA':
        print("You are a grilled cheese!")
    elif answer == 'BAA':
        print("Pumpernickle turkey sandwich!")
    elif answer == 'ABA':
        print("Might actually be Keanu Reeves...")

main()