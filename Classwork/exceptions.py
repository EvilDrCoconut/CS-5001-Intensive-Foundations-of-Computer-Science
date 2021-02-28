'''
Luke Parkhurst
CS 5001
Fall 2019
'''

def example():
    try:
        infile = open('file is not here')
        print(infile)
    except:
        print('dog')

def better_way():
    val = input('Give an integer: ')
    try:
        val = int(val)
        return val
    except ValueError:
        print(val, 'is not an integer')
    # use raise ValueError to create an error message if you want to show error
    # raise ValueError('You done goofed')

 # use finally to run chunk of code no matter what happens
# finally: print('Yup') :::::: The previous code will run no matter what happens, this happens after error arises
def better_way2():
    val = input('Give an integer: ')
    try:
        val = int(val)
        return val
    except ValueError:
        print(val, 'is not an integer')
    finally: print('finally clause: Yup')

def better_way3():
    val = input('Give an integer: ')
    try:
        val = int(val)
        return val
    except ValueError as big_error:
        print(big_error)
    # use the 'except error as' :::: to help show the errors

def better_way4():
    val = input('Give an integer: ')
    try:
        val = int(val)
        val = 10 / val
        return val
    except ValueError:
        print(val, 'is not an integer')
    except ZeroDivisionError:
        print('Divided by zero')
    # use division by zero error to help catch errors

def main():

    better_way()
    better_way2()
    better_way3()
    better_way4()

main()