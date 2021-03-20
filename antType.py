antTypeList = []

def getAntTypeList():
    return antTypeList

def getAntTypeFromColor(color):
    """
    Récupère le AntType en fonction de la couleur fournie
    """
    for antType in getAntTypeList():
        if antType[0] == color:
            return antType

def getBehaviorFromColor(antType, color):
    """
    Retourne la rotation de la fourmi en fonction de la couleur fournie (couleur de la case sur laquelle elle se trouve)
    return G or D
    """
    if color == "white":
        return antType[1][0]

    for i in range(len(getAntTypeList())):
        if getAntTypeList()[i][0] == color:
            return antType[1][i + 1]

def initAntType(fileName):
    file = open(fileName, "r")
    antTypes = []
    for line in file:
        dataLine = line.split(sep = ':')
        colorAnt = dataLine[0]
        behaviorAnt = list(dataLine[1].rstrip())
        antTypes += [(colorAnt, behaviorAnt)]
    global antTypeList
    antTypeList = antTypes
