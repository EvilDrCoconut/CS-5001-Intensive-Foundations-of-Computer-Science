'''
    a simple command line for python where we handle command line args
'''

import sys

def main():
 print('number of arguments is ', len(sys.argv))
 print("The arguments were ")
 for each in sys.argv:
     print(each)

main()