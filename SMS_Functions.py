# This will be the page that all of my functions are stored on
def shipLocations(playerName,shipLoc):
    #shipLoc = []
    def getShipLoc():
        try:
            infile = open('ship.txt', 'r')
            for line in infile:
                ship = line.rstrip()
                ship = ship.split(',')
                shipLoc.append(ship)
        except FileNotFoundError:
            print(f"Captin {playerName}, The radar is broken! The ship file was not found!")
            # Comeback to this. the gameOver function needs to be ran here.
            
    def nameShips(listOfShip):
        for ship in listOfShip:
            shipSize = len(ship)
            shipSizeStr = str(shipSize)
            ship.insert(0,"SHIP"+shipSizeStr)
    getShipLoc()
    nameShips(shipLoc)
        

# def printBoard():

# def checkChoice():

# def gameOver():

