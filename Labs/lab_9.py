'''
Luke Parkhurst
CS 5001
Lab 9
Fall 2019
'''
class Room():
    def __init__(self, number = 0, name = 'n/a', description = 'trapped!', adjacent = [], picture = ''):         
        self.name = name         
        self.number = number         
        self.description = description         
        self.adjacent_rooms = adjacent         
        self.picture = picture         
        self.items = []         
        self.puzzles = []         
        self.monsters = []     
    def add_item(self, item):         
        self.items.append(self, item)     
    def add_puzzle(self, puzzle):         
        self.items.append(puzzle)     
    def add_monster(self, monster):         
        self.monsters.append(monster)     
    def has_items(self):         
        return not (len(self.items) == 0)     
    def __str__(self):        
         return (str(self.number) + ':' + self.name) 

def rooms_init():
    infile = open('5001 CS Foundations/Labs/aquest_rooms.txt', 'r')
    room1 = ['Room 0', 'Room 1', 'Room 2', 'Room 3', 'Room 4', 'Room 5']
    lines = [infile.readline()]
    rooms = {}
    for i in range(6):
        print(lines) 

#    for key in rooms:
 #       print(key)
    return rooms

def main():
    rooms = rooms_init()
    # start = rooms['Room 1']

   # print(start)

main()#