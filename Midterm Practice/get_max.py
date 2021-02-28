'''
Luke Parkhurst
CS 5001
Midterm Practice
Fall 2019
'''

def get_max(lst):

    if len(lst) == 0:
        return 0

    i = lst[0]

    for t in lst:
        if i < t:
            i = t
    return i

def main():

    lsta = [1, 4, 9, -18]
    print(get_max(lsta))

    lstb = []
    print(get_max(lstb))

    lstc = [-1, -18, -5, -250, -1]
    print(get_max(lstc))

main()