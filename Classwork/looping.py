
def main():
    i = 0
    while i < 5:
        print(i)
        i += 1
    
    my_list = [1, 5, 'hello', 'world']
    print(my_list[2])

    for each in my_list:
        print(each)

    if 'hello' in my_list:
        print(True)

    if 'jello' not in my_list:
        print(False)

    my_list.append('goodbye')
    print(my_list)
    for each in my_list:
        print(each)

    my_list += ['another']
    print(my_list)
    
    my_list.append(['another'])
    print(my_list)

    (my_list[1]) = 'what'
    print(my_list)

    my_list.insert(2, 'cs5001')
    print(my_list)

    print(my_list[-1])
    print(my_list[-1][0])
    print(my_list[-1][0][-1])


main()
