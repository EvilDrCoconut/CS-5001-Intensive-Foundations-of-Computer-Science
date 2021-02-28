'''
Luke Parkhurst
CS 5001
Midterm Practice
Fall 2019
'''
import random

def chain_product(a, b):

    prod = 1

    for i in range(a, (b + 1)):
        if i % 2 == 1:
            prod *= i

    return prod

def snake_eyes(a):

    j = 0
    k = 0

    while k !=  a:
        t = random.randint(1, 6)
        x = random.randint(1, 6)
        print(t, x)
        if t == x == 1:
            j += 1
        k += 1
    print('Number of snake eye pairs: ', j)



    


def main():
    i = 6

    if i % 2 == 0:
        print('spoop')
    elif i % 3 == 0:
        print('boop')
    else:
        print('bloop')

    if i % 2 == 0:
        print('spoop')
    if i % 3 == 0:
        print('boop')
    else:
        print('bloop')


    i = 4
    if i % 2 == 0:
        print('spoop')
    if i % 3 == 0:
        print('boop')
    else:
        print('bloop')

    print(chain_product(1, 7))


    # below is a type error, when printing lst[i], it attempts to index slice strings, not integers
    #lst = ['0', '1', '2'] 
    #for i in lst: 
    #    print(lst[i]) 

    # below is an index error, when attempting to print lst[i], it reads as print index 4, but index only
    # goes from 0 to 2
    #lst = [4, 2, 3] 
    #for i in lst: 
    #    print(lst[i]) 

    # to fix first mistake, have i converted to integer
    lst = ['0', '1', '2'] 
    for i in lst:
        i = int(i) 
        print(lst[i]) 

    # for second mistake, tell it to only print i
    lst = [4, 2, 3] 
    for i in lst: 
        print(i) 

    # j = 5, but as j % 2 hits, it brings it to 4, which is then 3 due to j -= 1 at the end
    j = 5 
    while j >= 0: 
        print(2 ** j) 
        if j % 2 == 1: 
            j -= 1 
        j -= 1 

    t =   [1, 4, 7, 9, 2, 8] 

    for i in range(len(t)):
        if t[i] % 2 == 1:
            t[i] -= 1
        elif t[i] % 2 == 0:
            t[i] += 1
    print(t)

    snake_eyes(3)

main()