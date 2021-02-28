'''
Luke Parkhurst
CS 5001
Midterm Practice Q1
Fall 2019
'''

def counting_occurences(lst, i):
    j = 0
    
    for h in lst:
        if h == i:
            j += 1

    return j

def main():

    a = [3, 3, 4, 5, 1, 2]
    i = 2
    print(counting_occurences(a, i))

    b = [3, 3, 4, 5, 1, 2]
    i = 3
    print(counting_occurences(b, i))

    c = [5, 5, 5, 5, 1]
    i = 2
    print(counting_occurences(c, i))

main()