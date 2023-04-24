import trueskill

class Player(object):

    def __init__(self, name, mu, sigma):
        self.name = name
        self.rating = trueskill.Rating(mu=mu, sigma=sigma)

    def getName(self):
        return self.name
    
    def setRating(self, rating : trueskill.Rating):
        self.rating = rating
    
    def getRating(self):
        return self.rating
    
    def getMu(self):
        return self.rating.mu
    
    def setMu(self, mu : float):
        self.rating.mu = mu
    
    def getSigma(self):
        return self.rating
    
    def setSigma(self, sigma : float):
        self.rating.sigma = sigma
