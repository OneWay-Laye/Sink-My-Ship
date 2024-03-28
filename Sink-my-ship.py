# This is the start of sink my ship
#This will import the functions used in the file.
from SMS_Functions import shipLocations

# This will be the main fuction
def main():
    playerName = input("Enter Your name to get started!: ")
    MISSTOTAL = 20
    shotSpaces = []
    shipLoc = []
    shipLocations(shipLoc)
    print(shipLoc)

    
main()
