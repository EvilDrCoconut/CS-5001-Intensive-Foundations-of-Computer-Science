def main():




    s = ['peter', 'piper', 'picked', 'a', 'peck', 'of', 'peppers']
    ''.join(s)
    print(s)

    v = [10, 12, 20, 5]
    v.sort()
    print(v)

    v[0] = 6
    print(v)

    print(s[1:3])
    print(len(s))
    print(s[::1])
    print(s[::-1]) # :: turns in backwards

    print('banana'[::-1])
    print('banana'[2::-1]) # where to start, go backwards to beginning

    #a = 1
    b = -1
    #c = 5
    print('banana'[::b])

    v2 = [1,2,2,3,4]
    print(v2)
    v2.remove(2) # removes the first 2
    print(v2)

    r = [8] * 5
    print(r)
    my_list = [i for i in range(5)]
    print(my_list)
    my_list = [i for i in range(1, 5)]
    print(my_list)

    answer = input('What is your sentence? ')
    print(answer)
    print(answer.split())



main()