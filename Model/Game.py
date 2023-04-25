from Model.Team import Team

class Game(object):
    def __init__(self, teamOne, teamTwo):
        self.teamOne = teamOne
        self.teamTwo = teamTwo
        self.t1_score = 0
        self.t2_score = 0
        self.played = False
    
    def getTeamOne(self):
        return self.teamOne
    
    def getTeamTwo(self):
        return self.teamTwo
    
    def getTeamOneNames(self):
        return self.teamOne.getNames()
    
    def getTeamTwoNames(self):
        return self.teamTwo.getNames()
    
    def setPlayed(self):
        self.played = True

    def getPlayed(self):
        return self.played
    
    def setTeamScores(self, t1_score : int, t2_score : int):
        self.t1_score = t1_score
        self.t2_score = t2_score

    def getTeamOneScore(self):
        return self.t1_score
    
    def getTeamTwoScore(self):
        return self.t2_score

    def getResult(self):
        if self.t1_score > self.t2_score:
            return [0, 1]
        return [1, 0]
