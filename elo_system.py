import math
import trueskill
import random

ADVANCED = 4.0

CONTENDER_ONE = 4.5
CONTENDER_TWO = 4.5+(.5/3.0)
CONTENDER_THREE = 4.5+(.5/3.0)*2.0

PREMIER_ONE = 5.0
PREMIER_TW0 = 5.25
PREMIER_THREE = 5.5
PRO = 5.75


def main():
    playerNames = ["Justin Shaytar", "Sam McCune", "Nolan Marolf", "Isaac Staats", "Alex Newton", "John Putney", "Dustin Grant", "Ian Lane"]
    players_dict = {}
    for i in range(len(playerNames)):
        players_dict[playerNames[i]] = trueskill.Rating(mu=i)

    for i in range(5):
        players = sortPlayersBySkill(players_dict)
        print("Players")
        for player in players:
            print(player)
        print()

        teams = createTeams(players)

        print("Teams")
        for team in teams:
            print(f"Player One: {team[0][0]}, Player Two: {team[1][0]}")
        print()
        games = createGames(teams)
        print("Games")
        for game in games:
            printGame(game)
        players_dict = simulateGames(games)


def getPlayerRatingByName(name : str, players : list):
    for player in players:
        if player[0] == name:
            return player[1]
        

def simulateGames(games : list):
    players = {}
    for game in games:
        r1 = game[0][0][1]
        r2 = game[0][1][1]
        r3 = game[1][0][1]
        r4 = game[1][1][1]
        t1 = [r1, r2]
        t2 = [r3, r4]
        (players[game[0][0][0]], players[game[0][1][0]]) = trueskill.rate([t1, t2], ranks=[0,1])
    return players


def createGames(teams : list):
    games = []
    for team in teams:
        team.append(getAverageSkill(team))
    teams = sortTeamsBySkill(teams)
    for i in range(0, len(teams)-1, 2):
        game = [teams[i], teams[i+1]]
        games.append(game)
    return games


def getAverageSkill(team : list):
    return (team[0][1].mu + team[1][1].mu)/2.0


def createTeams(players : list):
    nums_list = list(range(len(players)))
    teams = []
    for i in range(int(len(players)/2)):
        index = random.randint(0, len(nums_list)-1)
        p1 = players[nums_list[index]]
        nums_list.remove(nums_list[index])

        index = random.randint(0, len(nums_list)-1)
        p2 = players[nums_list[index]]
        nums_list.remove(nums_list[index])
        teams.append([p1, p2])
    return teams


def sortPlayersBySkill(players : dict):
    return sorted(players.items(), key=lambda item: item[1], reverse=True)


def sortTeamsBySkill(teams : list):
    return sorted(teams, key=lambda item: item[2], reverse=True)


def printGame(game : list):
    print("Team One")
    print(f"Player One: {game[0][0]}")
    print(f"Player Two: {game[0][1]}")
    print("Team Two")
    print(f"Player Three: {game[1][0]}")
    print(f"Player Four: {game[1][1]}")
    print()


# def main():
#     playerNames = ["Justin Shaytar", "Sam McCune", "Nolan Marolf", "Isaac Staats", "Alex Newton", "John Putney", "Dustin Grant", "Ian Lane"]
#     players_dict = {}
#     players = []

#     for player in playerNames:
#         players_dict[player] = trueskill.Rating()

#     players = mergeSort(list(players_dict.items()))
#     players = sorted(players_dict, key=)
#     for player in players:
#         print(player)
#     print()
#     for i in range(3):        
#         t1 = [players[0][1], players[1][1]]
#         t2 = [players[2][1], players[3][1]]
#         t3 = [players[4][1], players[5][1]]
#         t4 = [players[6][1], players[7][1]]
#         (players_dict[players[0][0]], players_dict[players[1][0]]), (players_dict[players[2][0]], players_dict[players[3][0]]) = trueskill.rate([t1, t2], ranks=[0,1])
#         (players_dict[players[4][0]], players_dict[players[5][0]]), (players_dict[players[6][0]], players_dict[players[7][0]]) = trueskill.rate([t3, t4], ranks=[0,1])
        
#         players = mergeSort(list(players_dict.items()))
#         for player in players:
#             print(f"Player: {player}, Scaled: {getScaledValue(player[1].mu)}, Division: {getDivision(getScaledValue(player[1].mu))}")
#         print()


# def getScaledValue(value : float):
#     return value/6.0


# def getDivision(value : float):
#     if value >= PRO:
#         return "Pro"
#     if value >= PREMIER_THREE:
#         return "Premier 3"
#     if value >= PREMIER_TW0:
#         return "Premier 2"
#     if value >= PREMIER_ONE:
#         return "Premier 1"
#     if value >= CONTENDER_THREE:
#         return "Contender 3"
#     if value >= CONTENDER_TWO:
#         return "Contender 2"
#     if value >= CONTENDER_ONE:
#         return "Contender 1"
#     return "Advanced"


if __name__ == "__main__":
    main()
