import random
from clue import Clue
from group import Group

class WallGame:


    #number = 1
    
    def __init__(self,wallFileName):
        self.wallFileName = wallFileName
        self.clueList = []
        self.groupList = ["A","B","C","D"]
        self.wallSolved = False
        self.selectedCount = 0
        self.cluesSolvedPos = 0
        
    def createClues(self):
        positionList = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
        descClueCount = 15
        self.wallFile = open(self.wallFileName,"r")
        
        for groupCount in range(0,4):
            for groupPosCount in range(0,4):
                randomNumber = random.randint(0,descClueCount)
                randomPosition = positionList[randomNumber]
                del positionList[randomNumber]
                descClueCount -= 1
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
        print (self)
        for groupCount in range(0,4):
            groupCode = (self.groupList[groupCount])
            del groupCode

    def deleteClues(self):
        print ("in deleteClues")
        print (self)
        for item in self.clueList:
            del item

   

    def displayWall(self):
        self.clueList.sort()
        
        for _clue in range(0, len(self.clueList)):
            selectedMarker = " "
            if self.clueList[_clue].selected == "y":
                selectedMarker = "*"
            solvedMarker = " "
            if self.clueList[_clue].solved == "y":
                solvedMarker = "S"
            print(self.clueList[_clue].position, self.clueList[_clue].text, selectedMarker, solvedMarker)

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
                self.wallSolved == True

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
            
        self.wallSolved = True
    
    def playGame(self):

        validNumericCommands = ["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15"]
        validAlphaCommands = ["r"]
        validCommands = validNumericCommands + validAlphaCommands
        
        self.createClues()
        self.createGroups()

        while self.wallSolved == False:
            self.displayWall()

            print('Clues selected: ' + str(self.selectedCount))
            print(" ")

            userCommand = input("Input clue number to select it or R to Resolve the Wall:\n")
            if userCommand.lower() not in validCommands:
                print("You plum. Try again.\n")
            
            if userCommand.lower() == "r":
                print("I will resove the wall - you just see if I don't\n")
                self.resolveAllRemainingGroups()
                self.displayWall()
                return

            if userCommand in validNumericCommands:
                if self.clueList[int(userCommand)].solved == "y":
                    print("clue already in a solved group\n")
                elif self.clueList[int(userCommand)].selected == "n":
                    self.clueList[int(userCommand)].selected = "y"
                    self.selectedCount = self.selectedCount + 1
                    if self.selectedCount > 3:
                        self.evaluateGroup()
                else:
                    self.clueList[int(userCommand)].selected = "n"
                    self.selectedCount = self.selectedCount - 1
            else:
                    print("Nuclear meltdwon - unknown alpha command\n")
            
            self.displayWall()