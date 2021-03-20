import antType

ants = []

def getAnts():
    return ants

class Ant:

    def __init__(self, color, x, y):
        self.x = x
        self.y = y
        self.type = antType.getAntTypeFromColor(color)
        self.orientation = 0
        global ants
        ants += [self]

    def getType(self):
        return self.type

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getOrientation(self):
        return self.orientation

    def updateOrientation(self, direction):
        """
        direction = 'G' or 'D'
        """
        if direction == 'G':
            self.orientation -= 90
        elif direction == 'D':
            self.orientation += 90
        else:
            print("Unknow direction !")
        self.orientation %= 360

    def walk(self, grid):
        type = self.type
        direction = antType.getBehaviorFromColor(type, grid.getValue(self.getX(), self.getY()))
        self.updateOrientation(direction)

        if self.orientation == 0:
            self.y += 1
        elif self.orientation == 90:
            self.x += 1
        elif self.orientation == 180:
            self.y -= 1
        elif self.orientation == 270:
            self.x -= 1
