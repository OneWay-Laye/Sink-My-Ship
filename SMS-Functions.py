# This will be the page that all of my functions are stored on
def shipLocations():
    shipLoc = []
    def getShipLoc():
        infile = open('ship.txt', 'r')
        for line in infile:
            ship = line.rstrip()
            ship = ship.split(',')
            shipLoc.append(ship)
            
    def nameShips(listOfShip):
        for ship in listOfShip:
            shipSize = len(ship)
            shipSizeStr = str(shipSize)
            ship.insert(0,"SHIP"+shipSizeStr)
    getShipLoc()
    nameShips(shipLoc)
    print(shipLoc)
        

# def printBoard():

# def checkChoice():

# def gameOver():

shipLocations()
