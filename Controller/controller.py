from Model.Game import Game
from Model.Team import Team
from Model.Player import Player


class Controller(object):

    def __init__(self):
        self.players = []
        self.games = []


    def setPlayers(self, players : list):
        self.players = players

    def getPlayers(self):
        return self.players
    
    def setGames(self, games : list):
        self.games = games

    def getGames(self):
        return self.games
