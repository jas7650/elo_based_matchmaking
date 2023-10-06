from Model.Game import Game
from Model.Team import Team
from Model.Player import Player
from Model.Group import Group
import random


class Controller(object):

    def __init__(self):
        self.groups = {}


    def createGroup(self, name : str):
        self.groups[name] = Group(name)


    def getGroup(self, name : str):
        return self.groups[name]


    def addGame(self, game : Game, group : str):
        self.getGroup(group).addGame(game)


    def getGroups(self):
        return self.groups
