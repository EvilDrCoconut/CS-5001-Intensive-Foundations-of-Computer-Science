'''
CS 5001
Fall 2019
HW 2 - Defining functions
'''
'''
TEST RESULTS:
Absolute:
Test 1: input: 3, expected value: 3, output received: 3
Test 2: input: 0, expected value: 0, output received: 0
Test 3: input: -2, expected value: 2, output received: 2
Test 4: input: -999, expected value: 999, output received: 999

Manhattan:
Test 1: input: 3,3,6,6; expected value: 6, output received: 6
Test 2: input: 2,5,1,8; expected value: 2, output received: 2
Test 3: input: 4,2,-3,-2; expected value: 11, output received: 11
Test 4: input: -3,-5,-2,-7; expected value: 1, output received: 1

Euclidean:
Test 1: input: 3,3,6,6; expected value: 4.24, output received: 4.243
Test 2: input: 2,5,1,8; expected value: 3.16, output received: 3.162
Test 3: input: 4,2,-3,-2; expected value: 8.06, output received: 8.062
Test 4: input: -3,-5,-2,-7; expected value: 2.236, output received: 2.236
'''

# Below is the beginning of the absolute function
# collects parameter which is the question asking for user's number
def absolute(input):

# checks to see if user input is less than zero, than multiplies by -1 if it is    
# returns user input after proper adjustment 
    if 0 > input:
        return float(input * (-1))
    else:
        return input   
# completed in 5 lines


# Below is the beginning of the manhattan function, collects the 4 parameters
def manhattan(x1, y1, x2, y2):
    
# calculates the block distance by taking the two sets of x, y coordinates
    block_distance = absolute(float((x2 - x1) + (y2 - y1)))

# returns the calculated block distance
    return block_distance
# done in 2 lines

# Below is the beginning of the euclidean function, it collects both coordinate pairs first
def euclidean(x1, y1, x2, y2):

# here it calulcates the euclidean distance utilizing the absolute function if needed
# this is done by taking adding the differences of the squared coordinates, then square rooting it all
    distance = round(absolute(float((((x2 - x1) **2) + ((y2 - y1) **2)) **.5)), 6)

# now it returns the distance
    return distance
# done in 3 lines

'''
This chunk here is for general testing purposes
'''

def main():
    print('Choose from the following menu\n', 'Absolute: abs\n', 'Manhattan: man\n', 'Euclidean: euc')
    userquestions = input('Your choose: ')

    if userquestions == 'abs':
        print('Number: ?',)
        a1 = absolute(float(input()))
        print(a1)
    

    elif userquestions == 'man':
        print('Please insert first x1, y1 coordinates: ')
        x1 = float(input('x1?: '))
        y1 = float(input('y1?: '))

        print('Please insert second x2, y2 coordinates: ')
        x2 = float(input('x2?: '))
        y2 = float(input('y2?: '))

        distance = manhattan(x1, y1, x2, y2)

        print('The distance is', distance, 'blocks away!')
    
    elif userquestions == 'euc':
        print('Please insert first x1, y1 coordinates: ')
        x1 = float(input('x1?: '))
        y1 = float(input('y1?: '))

        print('Please insert second x2, y2 coordinates: ')
        x2 = float(input('x2?: '))
        y2 = float(input('y2?: '))

        distance = euclidean(x1,y1, x2, y2)

        print('The euclidean distance to second coordinates is', distance, 'blocks away!')

main()