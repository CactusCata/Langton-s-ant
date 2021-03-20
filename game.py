import graphics
import pocketgl
import grid
import ant, antType
import time

"""
Améliorations:
    - Ajouter un compteur de coup + % de chaque couleur
    - Nombre de col et ligne dynamique
    - Optimisation de l'affichage
"""

def antsWalks(grid):
    for a in ant.getAnts():
        x = a.getX()
        y = a.getY()
        colorAnt = a.getType()[0]
        colorCase = grid.getValue(x, y)

        a.walk(grid)
        if colorCase != colorAnt:
            grid.setValue(x, y, colorAnt) # setColor on last tile
        else:
            grid.setValue(x, y, "white")
    graphics.updateGraphics(grid)

def spawnAnt(color, x, y):
    ant.Ant(color, x, y)

if __name__ == '__main__':
    caseX = 40
    caseY = 40

    grid = grid.Grid(caseX, caseY)
    grid.fillGrid('white')
    antType.initAntType("antType.txt")
    spawnAnt("red", 25, 25)
    spawnAnt("blue", 20, 15)
    spawnAnt("yellow", 15, 20)
    spawnAnt("green", 20, 25)
    graphics.initGL("Fourmi de Langton", caseX, caseY)

    walkTimeNeeded = 10000
    timePerWalk = 0.00000002 # in seconds
    while walkTimeNeeded != 0:
        walkTimeNeeded -= 1
        time.sleep(timePerWalk)
        antsWalks(grid)

    pocketgl.main_loop()
