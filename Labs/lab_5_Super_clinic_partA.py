'''
CS 5001
Lab 5 Part 2
Fall 2019
'''

patients1 = ['TONY STARK', 'STEPHEN STRANGE', 'BRUCE BANNER', 'CLARK KENT'] 
ailments1 = ['heart problems', 'arthritis in hands', 'anger management', 'allergies - kryptonite']

patients = {}
ailments = {}

for i in range(len(ailments1)):
    patients[patients1[i]] = {}
    superhero_dict = patients[patients1[i]]
    superhero_dict['ailments'] = ailments1[i]





#ailmentsforTS = patients[patients1[0]]
#ailmentsforTS['ailments'] = ailments1[0]



#patients ['TONY STARK'] = ailments
#patients ['STEPHEN STRANGE'] = ailments
#patients ['BRUCE BANNER'] = ailments
#patients ['CLARK KENT'] = ailments


def main():
    print('Welcome to Super Hero Medical Databases: Authroized Personal left, have fun! Type EXIT to close menu')

    user_inp = ''


    #for k in patients.keys():
     #   print(k + " has " + patients[k])

    while user_inp != 'EXIT':
        
        user_inp = input('Please choose a patient to see their records. Patients are: \n TONY STARK \n STEPHEN STRANGE \n BRUCE BANNER \n CLARK KENT \n' )
        user_inp = user_inp.upper()

        if user_inp in patients1:
            ailment = patients[user_inp]['ailments']
            print(ailment)
            '''
            for superhero in patients.keys():
                print("Looking at " + patient)
                for condition in patients[superhero].keys():
                    print(superhero + ": condition ="+ condition + '. info ='+ patients[superhero][condition])
            for condition in patients[user_inp].keys():
                print(user_inp + " condition =" + condition + '. info = ')    
                print(patients[user_inp][condition])
            '''



main()