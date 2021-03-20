import pocketgl

windowsHeight = 600 # hauteur
windowsWidth = 800 # largeur

caseAmountX = 1
caseAmountY = 1
lineSize = 1
colSize = 1


def initGL(title, caseX, caseY):
    pocketgl.init_window(title, windowsWidth, windowsHeight)
    global caseAmountX, caseAmountY, lineSize, colSize
    caseAmountX = caseX
    caseAmountY = caseY
    lineSize = windowsWidth // caseX
    colSize = windowsHeight // caseY
    _drawGrid()

def _drawGrid():
    pocketgl.current_color("green")
    # draw lines
    for col in range(0, windowsHeight, colSize):
        pocketgl.line(0, col, windowsWidth, col)
    # draw columns
    for line in range(0, windowsWidth, lineSize):
        pocketgl.line(line, 0, line, windowsHeight)

def updateGraphics(grid):
    pocketgl.clear_screen()
    for x in range(grid.getXLength()):
        for y in range(grid.getYLength()):
            pocketgl.current_color(grid.getValue(x, y))
            pocketgl.box(lineSize * y, colSize * x, lineSize * (y + 1), colSize * (x + 1))
    _drawGrid()
    pocketgl.refresh()
