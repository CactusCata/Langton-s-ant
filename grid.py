class Grid:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        grid = []
        for line in range(x):
            arrayCol = []
            for col in range(y):
                arrayCol += ["?"]
            grid += [arrayCol]
        self.grid = grid

    def getGrid(self):
        return self.grid

    def getXLength(self):
        return self.x

    def getYLength(self):
        return self.y

    def correctCoordinates(self, x, y):
        return 0 <= x < self.x and 0 <= y < self.y

    def fillGrid(self, value):
        for x in range(self.x):
            for y in range(self.y):
                self.setValue(x, y, value)

    def setValue(self, x, y, value):
        if self.correctCoordinates(x, y):
            self.getGrid()[x][y] = value

    def getValue(self, x, y):
        if self.correctCoordinates(x, y):
            return self.getGrid()[x][y]

    def getPercentageOfValue(self, value):
        total = self.x * self.y
        count = 0
        for x in range(self.x):
            for y in range(self.y):
                if self.getValue(x, y) == value:
                    count += 1
        return 100 * amount / count
