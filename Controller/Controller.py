from Model.Game import Game
from Model.Team import Team
from Model.Player import Player
import random
import trueskill


class Controller(object):

    def __init__(self):
        self.players = self.initPlayers()
        self.games = []

    def initPlayers(self):
        playerNames = ["Justin Shaytar", "Donald Fung", "Nolan Marolf", "Josh Hutko", "Isaac Staats", "Alex Newton", "David Rowlands", "Spencer Argenna"]
        mus = [5.5, 5.4, 5.3, 5.2, 5.1, 5.0, 4.9, 4.8]
        players = []
        for i in range(len(playerNames)):
            player = Player(playerNames[i], mus[i], mus[i]/4)
            players.append(player)
        return players


    def getPlayerByName(self, name : str):
        for player in self.players:
            if player.getName() == name:
                return player

    def setPlayers(self, players : list):
        self.players = players

    def getPlayers(self):
        return self.players
    
    def removePlayer(self, name : str):
        player = self.getPlayerByName(name)
        self.players = self.getPlayers().remove(player)
    
    def getGames(self):
        return self.games
    
    def updateRatings(self, game : Game):
        p1 = self.getPlayerByName(game.getTeamOne().getPlayerOne().getName())
        p2 = self.getPlayerByName(game.getTeamOne().getPlayerTwo().getName())
        p3 = self.getPlayerByName(game.getTeamTwo().getPlayerOne().getName())
        p4 = self.getPlayerByName(game.getTeamTwo().getPlayerTwo().getName())
        r1 = p1.getRating()
        r2 = p2.getRating()
        r3 = p3.getRating()
        r4 = p4.getRating()
        t1 = [r1, r2]
        t2 = [r3, r4]
        (r1, r2), (r3, r4) = trueskill.rate([t1, t2], ranks=game.getResult())
        p1.setRating(r1)
        p2.setRating(r2)
        p3.setRating(r3)
        p4.setRating(r4)

    
    def createGames(self):
        players = self.sortPlayersBySkill(self.players)
        teams = self.createTeams(players)

        teams = self.sortTeamsBySkill(teams)
        for i in range(0, len(teams)-1, 2):
            game = Game(teams[i], teams[i+1])
            self.games.append(game)


    def createTeams(self, players : list):
        players_copy = players.copy()
        teams = []
        for i in range(int(len(players)/2)):
            team = self.getRandomTeam(players_copy)
            players_copy.remove(team.getPlayerOne())
            players_copy.remove(team.getPlayerTwo())
            teams.append(team)
        return teams


    def getRandomTeam(self, players : list):
        if len(players) >= 4:
            p1 = players[0]
            p2 = players[random.randint(1, 3)]
            team = Team(p1, p2)
            return team
        else:
            p1 = players[0]
            p2 = players[random.randint(1, len(players)-1)]
            team = Team(p1, p2)
            return team
        

    def getAverageSkill(self, team : Team):
        return (team.getPlayerOne().getMu() + team.getPlayerTwo().getMu())


    def sortPlayersBySkill(self, players : list):
        return sorted(players, key=lambda item: item.getMu(), reverse=True)


    def sortTeamsBySkill(self, teams : list):
        return sorted(teams, key=lambda item: item.getAverageSkillLevel(), reverse=True)
