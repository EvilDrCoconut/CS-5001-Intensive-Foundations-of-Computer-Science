'''
Luke Parkhurst
CS 5001
HW 5
Fall 2019
'''
'''
TEST CASES:
Test Case 1: Input 3: Success on Luck
Test Case 2: Input 2: Success on Luck
Test Case 3: Input 7: Success on Luck
Test Case 4: Input 8: Success on Luck
'''
# below are the three tower names
a = 'Duck'; b = 'Luck'; c = 'Buck'

# import the needed files for the program
from hanoi_viz import initialize_towers
from hanoi_viz import move_disk

# start of the move tower function, requires all three towers' names, the towers dictionary, and number of disks as paramter
def move_tower(source, target, middle, towers, num_disks):
    
    # if statement for if the number of disks is greater than 0, than to move from source to target
    # this will continue until disks on the source and target are empty and the middle tower is filled
    if num_disks >= 0:
        move_tower(source, middle, target, towers, num_disks - 1) # if greater than 0 to move from source to middle
        move_disk(source, target, towers) # utilizes the move disk function to move the disks between towers
        move_tower(middle, target, source, towers, num_disks - 1) # moves disk from middle to target

# beginning of the main function
def main():
    
    # creates a list of allowed number of disks a user may request
    allowed_disks = [1, 2, 3, 4, 5, 6, 7, 8]
    num_disks = 0 # sets number of disks to 0
    while num_disks not in allowed_disks: # creates loop to start user prompt as long as user prompt not in allowed_disks
        try: # sets a try function to help catch value errors
            print('Please choose a number between 1 and 8!') # tells user how many they may choose
            num_disks = int(input('How many disks are on the starting tower? (Only allowed 1 to 8 disks!) ')) # requests user's number
        except ValueError: # creates a Value Error exception if user puts in anything but a number
            print('Please pick a number between 1 to 8, dummy!') # reminds them the options
            num_disks = int(input('How many disks are on the starting tower? (Only allowed 1 to 8 disks!) '))
    towers = initialize_towers(num_disks, a, b, c) # initiliazes the towers function to create towers dictionary, saves it to towers constant
    move_tower(a, b, c, towers, num_disks) # calls upon the created move towers function to intiliaze overall program

main() # calls main