'''
    CS5001
    Fall 2019
    Homework 7 / Final Project
    ALIGN Quest
    Old-School Adventure game to gain more experience with Classes,
    Objects, Files, Lists, Program Decomposition, and almost
    everything else we touched on in the course

    This file contains the starter code for the game's Rooms, Puzzles and
    Monsters. Left to:do for the student: Build out the Item class.
    The rest of the framework can be extended, but works as-is
'''

class Game():
    def __init__(self):
        self.rooms = {}
        self.items = {}
        self.puzzles_n_monsters = {}

    def read_items(self, file):
        infile = open(file,'r')
        useless = infile.readline()
        for line in infile:
            line = line.split('|')
            item = Item(line[0], line[1], line[2], line[3], line[4], line[5])
            self.items[item.name] = item
        infile.close()

    def read_rooms(self, file):
        infile = open(file,'r')
        useless = infile.readline()
        for line in infile:
            line = line.split('|')
            room = Room(line[0], line[1], line[2], line[3], line[7])
            if line[6] in self.items.keys():
                room.add_item(self.items[line[6]])
            self.rooms[room.number] = room 
            self.rooms[room.number].monsters.append(line[5])
            self.rooms[room.number].puzzles.append(line[4])
        infile.close()
        self.inventory = []
        self.carry_weight = 0
        self.current_room = self.rooms['1']

# name|description|active|affects target|solution|target|effect|can attack|attack
    def read_puzzles_n_monsters(self, file):
        infile = open(file,'r')
        useless = infile.readline()
        for line in infile:
            line = line.split('|')
            if line[7] == '*':
                puz = Puzzle(line[0], line[1], line[5], line[2], line[3], line[4], line[6])
                self.puzzles_n_monsters[puz.name] = puz
            else:
                puz = Monster(line[0], line[1], line[5], line[2], line[3], line[4], line[6], line[7], line[8])
                self.puzzles_n_monsters[puz.name] = puz
        infile.close()


    def link_puz_n_rooms(self):

        for k, v in self.puzzles_n_monsters.items():
            for c, i in self.rooms.items():
                if k in i.puzzles:
                    if 'Room' in v.target:            
                        element = v.target.split()
                        v.target = self.rooms[element[1]]
                        self.rooms[element[1]].add_puzzle(v)
                        self.rooms[element[1]].puzzles.pop(0)
                elif k in i.monsters:
                    if 'Room' in v.target:
                        element = v.target.split()
                        v.target = self.rooms[element[1]]
                        self.rooms[element[1]].add_monster(v)
                        self.rooms[element[1]].monsters.pop(0)


# This line splits the read_files funciton from game functions _______________________________________________

    def can_you_move(self, inp = ''):
        room_lst = self.current_room.adjacent_rooms
        room_lst = room_lst.split()
        room_lst = (int(i) for i in room_lst)
        room_lst = list(room_lst)
        if inp == 'N':
            if room_lst[0] > 0:
                number = self.current_room.number
                self.rooms[number] = self.current_room
                self.current_room = self.rooms[str(room_lst[0])]
                return self.current_room
            elif room_lst[0] < 0:
                print('You must solve the puzzle to continue!')
            elif room_lst[0] == 0:
                print('A wall stands in your way.')
        
        if inp == 'S':
            if room_lst[1] > 0:
                number = self.current_room.number
                self.rooms[number] = self.current_room
                self.current_room = self.rooms[str(room_lst[1])]
                return self.current_room
            elif room_lst[1] < 0:
                print('You must solve the puzzle to continue!')
            elif room_lst[1] == 0:
                print('A wall stands in your way.')
        
        if inp == 'E':
            if room_lst[2] > 0:
                number = self.current_room.number
                self.rooms[number] = self.current_room
                self.current_room = self.rooms[str(room_lst[2])]
                return self.current_room
            elif room_lst[2] < 0:
                print('You must solve the puzzle to continue!')
            elif room_lst[2] == 0:
                print('A wall stands in your way.')

        if inp == 'W':
            if room_lst[3] > 0:
                number = self.current_room.number
                self.rooms[number] = self.current_room
                self.current_room = self.rooms[str(room_lst[3])]
                return self.current_room
            elif room_lst[3] < 0:
                print('You must solve the puzzle to continue!')
            elif room_lst[3] == 0:
                print('A wall stands in your way.')
        if inp == '':
            print('Issue has arisen')
    

    def check_inventory(self):
        inventory_lst = []
        for i in self.inventory:
            inventory_lst.append(i.name)
        print(inventory_lst)

    def drop(self):
        inventory_lst = []
        for i in self.inventory:
            inventory_lst.append(i.name.upper())
        print(inventory_lst)
        inp = input('What item do you wish to drop? ')
        inp = inp.upper()
        if inp not in inventory_lst:
            print('That is not in your inventory!')
        else:
            for i in self.inventory:
                check = i.name.upper()
                weight = int(i.weight)
                if check == inp:
                    self.inventory.remove(i)
                    self.carry_weight =- weight
                    self.current_room.items.append(i)
                else:
                    print('ERROR: check code')

    def look_at(self):
        room_name = self.current_room.name.upper()
        puzzle_name = ''; monster_name = ''; viewing_lst = []
        if self.current_room.puzzles != []: 
            puzzle = self.current_room.puzzles
            puzzle_name = puzzle.name.upper()
        if self.current_room.monsters != []: 
            monster = self.current_room.monsters
            monster_name = monster.name.upper()
        viewing_lst.append(room_name)
        if monster_name != '':
            viewing_lst.append(monster_name)
        if puzzle_name != '':
            viewing_lst.append(puzzle_name)
        for i in self.inventory:
            viewing_lst.append(i.name)
        for i in self.current_room.items:
            viewing_lst.append(i.name)
        print(viewing_lst)
        inp = input('What do you want to look at? ')
        if inp == '':
            inp = 'nope'
            print('No time to look at something now...')
        inp = inp.upper()
        if inp == room_name:
            print(self.current_room.description)
        elif inp == puzzle_name:
            print(self.current_room.puzzle.description)
        elif inp == monster_name:
            print(self.current_room.monster.description)
        else:
            for i in self.inventory:
                if inp == i.name.upper():
                    print(i.description)
            for i in self.current_room.items:
                if inp == i.name.upper():
                    print(i.description)
                else:
                    print('This is not around for you to look at!')

    def menu(self):
        allowed_cmmds = ['N','S','E','W','I','L','U','T','D','Q']
        inp = ''
        
        while inp not in allowed_cmmds:
            inp = input('Enter N, S, E, W to move in that direction. \n I for iventory, L to look at something, U to use item \n T to take an item, D to drop an item \n or Q to quit and exit the game \n')
            inp = inp.upper()
            if inp not in allowed_cmmds:
                print('Not an option!')
            else:
                return inp

    def quitting(self):
        ranking = {}
        ranking[12000] = 'Computer Scientist'
        ranking[3000] = 'Computer Programmer'
        ranking[1000] = 'Computer User'
        ranking[1] = "New Guy"
        score = 0
        for i in self.inventory:
            score =+ int(i.value)
        if score > 12000:
            score = 12000
        elif score > 3000:
            score = 3000
        elif score > 1000:
            score = 1000
        else:
            score = 1
    
        print('Congratulations player! Your score is ', score, '. Your rank is: ', ranking[score])

#    def puzzle_solver(self):
 #       for i current_room.puzzles:
  #          if i.active == True:
   #             des = 


    def take(self):
        inventory_lst = []
        for i in self.current_room.items:
            inventory_lst.append(i.name.upper())
        print(inventory_lst)
        inp = input('What do you want to take with you? ')
        inp = inp.upper()
        if inp not in inventory_lst:
            print('That is not an item in here!')
        else:
            for i in self.current_room.items:
                check = i.name.upper()
                if check == inp:
                        item = i
            weight = int(item.weight)
            weight_check = self.carry_weight + weight
            if weight > 11:
                print('This is to heavy to take with you!')
            elif weight_check > 10:
                print('This item would overburden you, drop some stuff first!')
            else:
                self.inventory.append(item)
                self.carry_weight =+ weight
                self.current_room.items.remove(item)

    def use_item(self):
        inven_lst = []
        inven_lst_room = []
        for i in self.inventory:
            inven_lst.append(i.name.upper())
        for i in self.current_room.items:
            inven_lst_room.append(i.name.upper())
        print('Items in inventory: ', inven_lst, 'Items in room: ', inven_lst_room)
        inp = input('What item do you want to use? ')
        inp = inp.upper()
        if inp not in inven_lst and inp not in inven_lst_room:
            print('That is not in your inventory or the room!')
        else:
            if inp in inven_lst:
                for i in self.inventory:
                    check = i.name.upper()
                    if check == inp:
                        i.use()
                        print('It appears this item has ', i.use_remaining, 'uses left...')
                    else:
                        print('Error has arisen: item not in inventory')
            elif inp in inven_lst_room:
                for i in self.current_room.items:
                    check = i.name.upper()
                    if check == inp:
                        i.use()
                        print('It appears this item has ', i.use_remaining, 'uses left...')
                    else:
                        print('Error has arisen: item not in room')

    def game_launch(self):
        self.read_items('aquest_items.txt')
        self.read_rooms('aquest_rooms.txt')
        self.read_puzzles_n_monsters('puzzles_n_monsters.txt')
        self.link_puz_n_rooms()

        inp = ''
        print('Welcome to AlignQuest! Solve your way out of this Mansion!')
        print("Opening the gates to a courtyard, you enter into the mansion's grounds. The cold iron gate clanking close behind you")
        
        while inp != 'Q':
            if self.current_room.monsters[0] != 'None':
                self.current_room.contextual_description2()
            elif self.current_room.puzzles[0] != 'None':
                self.current_room.contextual_description()
            else:    
                print(self.current_room.description)
            inp = self.menu()

            if inp in ['N','S','E','W']:
                self.can_you_move(inp)
            elif inp == 'I':
                self.check_inventory()
            elif inp == 'L':
                self.look_at()
            elif inp == 'U':
                self.use_item()
            elif inp == 'T':
                self.take()
            elif inp == 'D':
                self.drop()
            elif inp == 'Q':
                self.quitting()
            else:
                print('ISSUE: check code')
    

# this line seperates game functions from class objects ___________________________________________________________




'''
    class: Room
    Description:
    This class encapsulates all of the behavior for the "areas" in our
    virtual world. A room is a general idea; rooms might be anywhere
    the player can explore by stepping into them (e.g. closets, boxes)
    Each room has a description and can contain items. Some rooms
    may have a puzzle to solve or a "monster" (our monsters are cute,
    furry animals or toys) that protect the room. If a monster or puzzle
    is present, the user must "deactivate" said puzzle/monster before
    the full room description is presented to them
'''
    
class Room(Game):
    def __init__(self, number = 0, name = 'n/a',
                 description = 'trapped!', adjacent = [], picture = ''):
        self.name = name
        self.number = number
        self.description = description
        self.adjacent_rooms = adjacent
        self.picture = picture
        self.items = []
        self.puzzles = []
        self.monsters = []
    def add_item(self, item): # add an item to the room
        self.items.append(item)
    def add_puzzle(self, puzzle): # add a puzzle to the room
        self.puzzles.append(puzzle)
    def add_monster(self, monster): # add a monster to the room
        self.monsters.append(monster)
    def has_items(self):            # answer if the room has items or not
        return not (len(self.items) == 0)
    def has_puzzle(self):           # does the room have puzzles?
        return not (len(self.puzzles) == 0)
    def has_monsters(self):         # answer if monster is in the room
        return not (len(self.monsters) == 0)
    def reverse_effects(self):      # reverse effects of puzzle/monster
        for i in range(len(self.adjacent_rooms)):
            if self.adjacent_rooms[i] < 0: # blocked by a puzzle or monster
                self.adjacent_rooms[i] = 0 - self.adjacent_rooms[i] # make it open
    def contextual_description(self):
        if self.has_puzzle(): # puzzle blocks regular description. 
            for each in self.puzzles:
                if each == 'None':
                    pass
                elif (each.target == self and
                    each.active and
                    each.affects_target):
                    return each.do_effect()
        # if no puzzles/monsters are active, return regular description
        return self.description 
    def contextual_description2(self):
        if self.has_monsters(): # puzzle blocks regular description. 
            for each in self.monsters:
                if type(each) == str:
                    pass
                elif (each.target == self and
                    each.active and
                    each.affects_target):
                    return each.do_effect()
        # if no puzzles/monsters are active, return regular description
        return self.description 
    def __str__(self):
        return (str(self.number) + ':' + self.name + ':' + self.description)

'''
    class: Item
    Description:
    This class encapsulates all of the behavior for the "things" in our
    rooms. Items can be collected by the player by Taking them during
    their quest. Items also have a description that players can see when
    they Look at the item. Players can also Drop or Use items
    For this prototype, puzzles and monsters CAN be attached to items
    (just like rooms) but the framework doesn't fully support the
    resolution of solutions for those puzzles on objects yet.
    reverse_effects() is future work, so you can leave it as a "pass"
    in your code
'''
# TO:DO - STUDENTS FLESH THIS OUT
class Item:
    def __init__(self, number = 0, name = 'n/a',
                 description = '', weight = 0, value = 0, use = 0):
        self.name = name
        self.number = number
        self.description = description
        self.weight = weight
        self.value = value
        self.use_remaining = use
        self.puzzle = ''

    # does the item have any use left, or is it used up?
    def has_use_remaining(self):
        check = int(self.use_remaining)
        if check > 0:
            True
        else:
            False
        # if the item's use_remaining > 0, return True otherwise False

    '''
    # placeholder. pass on doing this
    def reverse_effects(self):
        pass # to:do for version 2
    '''
    
    # answer if the Item has a puzzle or not
    def has_puzzle(self):
        if self.puzzle == '': 
            return False 
        else:
            return True
    
    # try to use the item (on a puzzle or monster)
    def use(self):
        uses_left = self.has_use_remaining
        if uses_left == True:
            uses = self.use_remaining
            uses =- 1
            self.use_remaining = str(uses)
            return self.name, True
        else:
            return self.name, False
        # if the item has some uses remaining (e.g. use_remaining > 0)
        # then decrement use_remaining by 1 AND
        # return a 2-tuple with the item name and True
        # otherwise, return a 2-tuple with item name and False

'''
    class: Puzzle
    Description:
    This class encapsulates all of the behavior for the challenges in our
    rooms. Puzzle is a general term...right now it's not some hard problem
    to solve, but currently the use of some ITEM to "neutralize" the problem
    or monster the player encounters. E.g. a glass of water might neutralize
    a FIRE puzzle
    If puzzles are active, they occlude the regular description of a room
    Items neutralize puzzles and deactivate them
'''
class Puzzle:
    def __init__(self, name = 'n/a',description = '', target = '',
                 active = True, affects_target = False,
                 solution = '', effect = ''):
        self.name = name
        self.description = description
        self.active = active
        self.affects_target = affects_target
        self.solution = solution
        self.target = target
        self.effect = effect
    def activate(self):
        self.active = True
    def deactivate(self):
        self.active = False
    def is_active(self):
        return self.active
    def do_effect(self):
        return self.effect
    def try_to_solve(self, solution):
        if solution.upper() == self.solution.upper():
            self.deactivate()
            return True
        return False

'''
    class: Monster
    Description:
    This class is a subtype of Puzzle that can "attack" the user.
    All of our monsters are soft and furry creatures so they can't
    really hurt the user (no need for inducing PTSD in a computer game)
    Like their superclass, they occlude the regular room description
    until they are neutralized
'''
class Monster(Puzzle):
    def __init__(self, name = 'n/a',description = '', target = '',
                 active = True, affects_target = False,
                 solution = '', effect = '',
                 can_attack = True, attack = 'Cotton Balls'):
        super().__init__(name, description, target,
                         active, affects_target, solution, effect)
        self.can_attack = can_attack
        self.attack = attack
    def do_effect(self):
        return self.effect + '\n' + self.do_attack()
    def do_attack(self):
        return self.name + ' ' + self.attack
    def defeated(self):
        return 'The ' + self.name + ' has been defeated. It is not moving.'
