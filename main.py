import random
from clue import Clue
from group import Group
from wallgame import WallGame


#Read control file
wallGameControlFile = "wallGameControlFile.txt"
wallControlFile = open(wallGameControlFile,"r")
wallFileName = wallControlFile.readline().rstrip("\n")

#play the game 

playGame = True
gameNumber = 0


while playGame:

    gameNumber += 1

    wallGameInstance = WallGame(wallFileName)
    print ("wallGameCode=", wallGameInstance)
    print (" ")


#Here we are playing the game - call the functions in wallGame to do this
    wallGameInstance.playGame()

#!!!delete all objects associated with the game call delete functions in wallgame
    # del wallGameInstance

    playAgain = 'x'
    valid = ['y', 'n']
    while playAgain not in valid:
        playAgain = input("Would you like to play again? y/n")

    if playAgain == 'n':
        playGame = False
    else:
        playGame = True
        gameNumber = gameNumber + 1
        print("1 = Next wall in control file")
        print("2 = Play same wall again")
        validInput = "n"
        while validInput == "n":
            playAgaintype = input("enter your selection")
            if playAgaintype == "1":
                validInput = "y"
                wallFileName = wallControlFile.readline()
            elif playAgaintype == "2":
                validInput = "y"           
            else:    
                print("you are as impressive as an otter trying to solve a Rubik's cube.")
                print("Enter 1 or 2, dumbo.")
    

print ("You have finished playing with my walls.")
print ("Come back soon.")
print ("...")
print ("...")
print ("...")
print ("I miss you.")



#Display group definitions exit.


    
