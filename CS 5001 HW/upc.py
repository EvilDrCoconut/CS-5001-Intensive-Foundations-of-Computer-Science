'''
Luke Parkhurst
CS 5001
Fall 2019
HW 4
'''
'''
TEST CASE:
Test Case 1: 0820182993       returns True
Test Case 2: 870030109100     returns False
Test Case 3: 25074009185780   returns False
Test Case 4: 0000000000000    returns False
'''


# beginning of the is_valid_upc function, takes a list for argument
def is_valid_upc(lst):

    # checks to see if length of list is 2 or less, returns false if it is
    if len(lst) < 2:
        return False
    
    # sets contant i to equal every other list element starting from end of list
    i = lst[::-2]
    i = sum(i) # sums all of these elements together

    # sets constant b to equal every other element in list starting from second to last element
    b = lst[-2::-2] 
    e = 0 # sets a constant to help with mulitplication of b
    
    for each in b: # iterates each through list b
        e += each * 3 # multiples each by 3 and adds to constant e
    b = e # sets b to equal e after to maintain consistency


    if (i + b) == 0: # if the sum of i and b now are 0, returns false
        return False

    valid = (i + b) % 10   # creates a constant called valid and takes modulos 10 of the sum of i and b

    if valid == 0: # if valid equals 0, returns true
        return True
    else: # if valid is not equal to 0, returns false
        return False
