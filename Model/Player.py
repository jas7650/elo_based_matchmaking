

class Player(object):

    def __init__(self, name, mu, sigma):
        self.name = name
        self.mu = mu
        self.sigma = sigma

    def getName(self):
        return self.name
    
    def getMu(self):
        return self.mu
    
    def getSigma(self):
        return self.sigma
