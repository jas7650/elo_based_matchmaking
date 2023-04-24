import Model.Player

class Team(object):
    
    def __init__(self, playerOne, playerTwo):
        self.playerOne = playerOne
        self.playerTwo = playerTwo

    def getPlayerOne(self):
        return self.playerOne
    
    def getPlayerTwo(self):
        return self.playerTwo
    
    def getPlayers(self):
        return [self.playerOne, self.playerTwo]

    def getAverageSkillLevel(self):
        return (self.playerOne.getMu() + self.playerTwo.getMu())/2.0
    
    def getNames(self):
        return [self.getPlayerOne().getName(), self.getPlayerTwo().getName()]
    