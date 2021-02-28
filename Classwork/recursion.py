# recursion is used to have a function to call upon itself until desired outcome
# sometimes recursion loops are quicker or easier to set up than while loops

def countdown(n):
    if n <= 0: #base case, stops when true
        print('blastoff')
    else:
        print(n)
        countdown(n-1) # call ourselves with smaller space

lst = [18, 25, 72, 5]

def sum_list(lst): # recursion loop that adds values in a list
    if (len(lst) == 1):
        return lst[0]
    else:
        return lst[0] + sum_list(lst[1:])



def main():
    countdown(5)
    print(sum_list(lst))


main()