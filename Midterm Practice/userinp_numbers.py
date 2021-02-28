'''
Luke Parkhurst
CS 5001
Midterm Practice Q2
Fall 2019
'''

def main():

    userinp = ''
    lst = []
    avg = ''

    while userinp != '-99':
        userinp = input('Enter a number ' )
        if userinp == '-99':
            avg = (int(i) for i in lst)
            print(len(lst))
            print((sum(avg) / len(lst)))
        lst.append(userinp)
        


main()