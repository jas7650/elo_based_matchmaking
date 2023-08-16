from Model.Game import Game
from Model.Team import Team
from Model.Player import Player
import random
import trueskill


class Group(object):

    def __init__(self, name : str):
        self.players = {}
        self.games = []
        self.name = name
        self.previous_teams = [[], []]
        self.previous_sit = []
        self.current_sit = []


    def setGroupName(self, name : str):
        self.name = name


    def getGroupName(self):
        return self.name


    def addPlayer(self, player : Player):
        if player.getName() not in self.players.keys():
            self.players[player.getName()] = player


    def getPlayers(self):
        return self.sortPlayersBySkill(self.players)
    

    def getNumPlayers(self):
        return len(self.players.items())
    

    def getPlayer(self, name : str):
        return self.players[name]


    def removePlayer(self, name : str):
        player = self.getPlayerByName(name)
        self.players.remove(player)


    def getGames(self):
        return self.games
    

    def getNumGames(self):
        numGames = 0
        for game in self.games:
            if game.getPlayed() == True:
                numGames += 1
        return numGames
    

    def shiftInTeamsList(self, teams : list):
        self.previous_teams[1] = self.previous_teams[0]
        self.previous_teams[0] = teams


    def getTeamExisted(self, team : Team):
        for list in self.previous_teams:
            for t in list:
                names = team.getPlayerNames()
                if names[0] in t.getPlayerNames() and names[1] in t.getPlayerNames():
                    return True
        return False


    def updateRatings(self, game : Game):
        p1 = self.players[game.getTeamOne()[0]]
        p2 = self.players[game.getTeamOne()[1]]
        p3 = self.players[game.getTeamTwo()[0]]
        p4 = self.players[game.getTeamTwo()[1]]
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
        p1.addResult(game)
        p2.addResult(game)
        p3.addResult(game)
        p4.addResult(game)

# Priorities:
# 1) Creating competitive games with variety
# 2) Ensuring that no one spends too much time sitting during a session

# Process:
# 1) Sort players by skill level
# 2) Iterate from the top to the bottom, creating teams by selecting the highest ranked
#    player remaining, then selecting a random player within a small range of the player. 
# 3) Create a team for players that just sat first, to ensure that they don't sit 
#    multiple times in a row. Can do so, by choosing a player that is within a range 
#    better or worse than the player of interest. 
# 4) After teams have been assigned for each player that just sat, attempt to generate teams
#    for the rest of the players. 
# 5) For each team, check if team existed in the last 2 rounds of games. Try a new team if 
#    the team did exist recently.
# 6) Try each combination of teams given the players that have not been assigned a team yet. 
#    If no combination passes, back up to the previous team and try to create a new combination
#    that works.


    def createGames(self):
        players = self.sortPlayersBySkill(self.players)
        teams = self.createTeams(players)
        self.shiftInTeamsList(teams)

        teams = self.sortTeamsBySkill(teams)
        for i in range(0, len(teams)-1, 2):
            t1 = [teams[i].getPlayerOne().getName(), teams[i].getPlayerTwo().getName()]
            t2 = [teams[i+1].getPlayerOne().getName(), teams[i+1].getPlayerTwo().getName()]
            game = Game(t1, t2)
            self.games.append(game)


    def createTeams(self, players : list):
        players_copy = players.copy()
        teams = []
        for i in range(int(len(players)/2)):
            attempts = 0
            team = self.getRandomTeam(players_copy)
            while self.getTeamExisted(team) == True and attempts < 10:
                team = self.getRandomTeam(players_copy)
                attempts += 1
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


    def sortPlayersBySkill(self, players : dict):
        return sorted(players.values(), key=lambda item: item.getMu(), reverse=True)


    def sortTeamsBySkill(self, teams : list):
        return sorted(teams, key=lambda item: item.getAverageSkillLevel(), reverse=True)
