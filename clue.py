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