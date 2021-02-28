'''
Luke Parkhurst
CS 5001
Fall 2019
'''
length = 0

class Shape:
    def __init__(self):
        self.name = 'Generic Shape'
    def draw(self):
        print("I don't know how to draw")
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length
        self.color = 'yellow'
    def draw(self):
        print('+_______+\nl l\n_______\n')
    def area(self):
        return self.length ** 2
    def __str__(self): # asking to state themselves, says something through a string
        return 'SQUARE'
    def __eq__(self, other): # asking if equal to another
        if self.length == other.length:
            return True
        return False    

class Pot:
    def sing(self):
        print("Pot")

class TeaPot(Pot): # overiding from the hierarchy
    def sing(self): # override
        print("I'm a little Tea", end=" ")
        super().sing()


# ________________________________________________________________________________________________________
def main():
    s = Shape()
    sq = Square(10)
    print(s.area())
    s.draw
    print(sq.area())
    sq.draw
    print(sq)
    sq2 = Square(10)
    print(sq == sq2)

def main2():
    print('_________________________________________________________________')
    p = Pot()
    p.sing()
    q = Pot()
    q.sing()
    tp = TeaPot()
    tp.sing()
    p.sing()

main()
main2()