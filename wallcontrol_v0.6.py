#v0.3 Read randomize display and selection all working
#v0.4 Evaluation of groups and sorting of solved groups now working (inline)
#v0.5 Reolution of unsolved groups working improved finish of game. 
#       Known bug on garbage collection play again does not work 

#control program for connecting walls


#create class WallGame

class WallGame:

    clueList = []
    groupList = ["A","B","C","D"]
    wallSolved = "n"
    selectedCount = 0
    cluesSolvedPos = 0
    
    #number = 1
    
    

    def __init__(self,wallFileName):
        self.wallFileName = wallFileName
        

    def createClues(self):
       
        positionList = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
        descClueCount = 15


        self.wallFile = open(wallFileName,"r")
        
        for groupCount in range(0,4):
            for groupPosCount in range(0,4):
                randomNumber = random.randint(0,descClueCount)
                randomPosition = positionList[randomNumber]
                del positionList[randomNumber]
                descClueCount = descClueCount - 1
                self.clueList.append(Clue(randomPosition,self.wallFile.readline().rstrip("\n"),self.groupList[groupCount],groupPosCount))
      
        

    def createGroups(self):

        for groupCount in range(0,4):
            groupCode = (self.groupList[groupCount])
            groupCode = Group(groupCode,self.wallFile.readline().rstrip("\n"))
#            print (groupCode.groupID)
#            print (groupCode.solved)
#            print (groupCode.solvedOrder)
#            print (groupCode.connexion)


    def deleteGroups(self):

        print ("in deleteGroups")
        print (wallGameCode)
        for groupCount in range(0,4):
            groupCode = (self.groupList[groupCount])
            del groupCode

    def deleteClues(self):

        print ("in deleteClues")
        print (wallGameCode)
        for item in self.clueList:
            del item 

   

    def displayWall(self):

        self.clueList.sort()
        

        for a in range(0,16):
            selectedMarker = " "
            if self.clueList[a].selected == "y":
                selectedMarker = "*"
            solvedMarker = " "
            if self.clueList[a].solved == "y":
                solvedMarker = "S"
            print(self.clueList[a].position, self.clueList[a].text, selectedMarker, solvedMarker)

        print(" ")

    def evaluateGroup(self):

        groupIsCorrect = "y"
        firstSelectedClue = "y"
        
        for item in self.clueList:
            if item.selected == "y":
                if firstSelectedClue == "y":
                    firstSelectedClue = "n"
                    groupToCheck = item.clueGroup
                if groupToCheck != item.clueGroup:
                    groupIsCorrect = "n"

        if groupIsCorrect == "n":
            print("that is not a group")
            print(" ")
            for item in self.clueList:
                item.selected = "n"
            self.selectedCount = 0    
        else:
            print("you've found a group")
            print(" ")
            self.resolveGroup(groupToCheck)
            if self.cluesSolvedPos > 11:
                self.resolveAllRemainingGroups()
                print("You've solved the wall!")
                print(" ")
                self.wallSolved == "y"

    def resolveGroup(self,groupToResolve):

            for i in range(0,4):
                for item in self.clueList:
                    if item.clueGroup == groupToResolve and i == item.numberInGroup: 
                        clueMovedFrom = item.position
                        item.position = self.cluesSolvedPos + i
                        item.solved = "y"
                        self.clueList[self.cluesSolvedPos + i].position = clueMovedFrom
                        self.clueList.sort()
            self.cluesSolvedPos = self.cluesSolvedPos + 4
            for item in self.clueList:
                item.selected = "n"
            self.selectedCount = 0

            

    def resolveAllRemainingGroups(self):

        groupsToResolve = ["A","B","C","D"]

        for i in range(0,9,4):
            if self.clueList[i].solved == "y":
                groupsToResolve.remove(self.clueList[i].clueGroup)

        for group in groupsToResolve:
            self.resolveGroup(group)      
 
        for clue in self.clueList:
            clue.selected = "n"
            
        self.wallSolved = "y"
    
    def playGame(self):

        validNumericCommands = ["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15"]
        validAlphaCommands = ["r"]
        validCommands = validNumericCommands + validAlphaCommands
        

        
        
        self.createClues()
        self.createGroups()

        while self.wallSolved == "n":

            self.displayWall()

            print(self.selectedCount)
            print(" ")

            userCommand = input("clue to select, or R to Resolve the Wall")
            if userCommand.lower() in validCommands:
                if userCommand in validNumericCommands:
                    if self.clueList[int(userCommand)].solved == "n":
                        if self.clueList[int(userCommand)].selected == "n":
                            self.clueList[int(userCommand)].selected = "y"
                            self.selectedCount = self.selectedCount + 1
                            if self.selectedCount > 3:
                                self.evaluateGroup()
                                
                        else:
                            self.clueList[int(userCommand)].selected = "n"
                            self.selectedCount = self.selectedCount - 1
                    else:
                        print("clue already in a solved group")
                        print(" ")
                else:
                    if userCommand.lower() == "r":
                        print("I will resove the wall - you just see if I don't")
                        print(" ")
                        self.resolveAllRemainingGroups()
                    else:
                        print("Nuclear meltdwon - unknown alpha command")
                        print(" ")
            else:
                print("You plum. Try again.")
                print(" ")

        self.displayWall()
            
        

#create class "Clue"
class Clue:

    selected = "n"
    solved = "n"

    def __init__(self,position,text,clueGroup,numberInGroup):
        self.position = position
        self.text = text
        self.clueGroup = clueGroup
        self.numberInGroup = numberInGroup

    def __eq__(self, other):
        return self.position == other.position
    
    def __lt__(self, other):
        return self.position < other.position

    def __del__(self):  
        print("Destructor called, Example deleted.")  





#create class "Group"

class Group:

    solved = "n"
    solvedOrder = 0

    def __init__(self,groupID,connexion):
        self.groupID = groupID
        self.connexion = connexion 




import random


#Read control file
wallGameControlFile = "wallGameControlFile.txt"
wallControlFile = open(wallGameControlFile,"r")
wallFileName = wallControlFile.readline().rstrip("\n")

#play the game 

playGame = "y"
gameNumber = 1


while playGame == "y":

    wallGameCode = ("Game" + str(gameNumber))
    print ("Game" + str(gameNumber))
    print ("wallGameCode=", wallGameCode)
    print (" ")
    
    wallGameCode = WallGame(wallFileName)
    print ("wallGameCode=", wallGameCode)
    print (" ")


#Here we are playing the game - call the functions in wallGame to do this
    wallGameCode.playGame()

#!!!delete all objects associated with the game call delete functions in wallgame
    wallGameCode.deleteClues()
    wallGameCode.deleteGroups()
    
    del wallGameCode
        
    playAgain = input("Would you like to play again?")
    
    if playAgain.lower() != "y" and playAgain.lower() != "yes":
        playGame = "n"
    else:
        playGame = "y"
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


    
