'''
Luke Parkhurst
CS 5001
Lab 7
'''

def friends():
    infile = open('dwarves.txt', 'r')     
    dwarves = {}     
    for lines in infile:         
        lines = lines.split() # make a list out of the blank separated string         
        dwarves[lines[0]] = lines[1:] # we have at least the dwarf username     
    infile.close() # close the file     
    #return dwarves
    print(dwarves)
def main():
    friends()

main()