
class Game(object):
    def __init__(self, teamOne : list, teamTwo : list):
        self.teamOne = teamOne
        self.teamTwo = teamTwo
        self.t1_score = 0
        self.t2_score = 0
        self.played = False
    
    def getTeamOne(self):
        return self.teamOne
    
    def getTeamTwo(self):
        return self.teamTwo
    
    def setPlayed(self):
        self.played = True

    def getPlayed(self):
        return self.played
    
    def setScore(self, score : list):
        self.t1_score = score[0]
        self.t2_score = score[1]

    def getTeamOneScore(self):
        return self.t1_score
    
    def getTeamTwoScore(self):
        return self.t2_score

    def getResult(self):
        if self.t1_score > self.t2_score:
            return [0, 1]
        return [1, 0]
