import math
import trueskill
import random
from Model.Game import Game
from Model.Team import Team
from Model.Player import Player

def getPlayerRatingByName(name : str, players : list):
    for player in players:
        if player[0] == name:
            return player[1]
        

# def simulateGames(games : list):
#     players = {}
#     for game in games:
#         r1 = game[0][0][1]
#         r2 = game[0][1][1]
#         r3 = game[1][0][1]
#         r4 = game[1][1][1]
#         t1 = [r1, r2]
#         t2 = [r3, r4]
#         (players[game[0][0][0]], players[game[0][1][0]]), (players[game[1][0][0]], players[game[1][1][0]]) = trueskill.rate([t1, t2], ranks=getRandomRanks())
#     return players


def createGames(players : list):
    games = []
    players = sortPlayersBySkill(players)
    teams = createTeams(players)

    teams = sortTeamsBySkill(teams)
    for i in range(0, len(teams)-1, 2):
        game = Game(teams[i], teams[i+1])
        games.append(game)
    return games


def getRandomRanks():
    num = random.randint(0, 1)
    if num == 0:
        return [0, 1]
    return [1, 0]


def getAverageSkill(team : Team):
    return (team.getPlayerOne().getMu() + team.getPlayerTwo().getMu())


def createTeams(players : list):
    players_copy = players.copy()
    teams = []
    for i in range(int(len(players)/2)):
        team = getRandomTeam(players_copy)
        players_copy.remove(team.getPlayerOne())
        players_copy.remove(team.getPlayerTwo())
        teams.append(team)
    return teams


def getRandomTeam(players : list):
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


def sortPlayersBySkill(players : list):
    return sorted(players, key=lambda item: item.getMu(), reverse=True)


def sortTeamsBySkill(teams : list):
    return sorted(teams, key=lambda item: item.getAverageSkillLevel(), reverse=True)
