import trueskill
from Model.Game import Game

class Player(object):

    def __init__(self, name, mu, sigma):
        self.name = name
        self.rating = trueskill.Rating(mu=mu, sigma=sigma)
        self.wins = 0
        self.losses = 0
        self.games = []

    def addResult(self, game : Game):
        self.games.append(game)
        t1_score = game.getTeamOneScore()
        t2_score = game.getTeamTwoScore()
        if self.name in game.getTeamOne():
            if t1_score > t2_score:
                self.wins += 1
            elif t2_score > t1_score:
                self.losses += 1
        else:
            if t2_score > t1_score:
                self.wins += 1
            elif t1_score > t2_score:
                self.losses += 1

    def getGames(self):
        return self.games
    
    def getWins(self):
        return self.wins
    
    def getLosses(self):
        return self.losses

    def getName(self):
        return self.name
    
    def setRating(self, rating : trueskill.Rating):
        self.rating = rating
    
    def getRating(self):
        return self.rating
    
    def getMu(self):
        return self.rating.mu
    
    def getMuRounded(self):
        return round(self.rating.mu, 2)
    
    def setMu(self, mu : float):
        self.rating.mu = mu
    
    def getSigma(self):
        return self.rating
    
    def setSigma(self, sigma : float):
        self.rating.sigma = sigma

    def getRecord(self):
        return f"{self.wins} - {self.losses}"
