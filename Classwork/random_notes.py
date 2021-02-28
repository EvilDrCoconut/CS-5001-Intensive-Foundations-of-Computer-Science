# random notes
# when setting global variables, must use global to call upon it in a function for overwriting
# if set outside of functions and main(), it is automatically a global operator
cat = 2 #this is now a global variable

def san():
    dog = 2
    return dog


def main():
#    global dog = 0
    print(san())


main()