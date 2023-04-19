import math
import trueskill
import random


def main():
    playerNames = ["Justin Shaytar", "Sam McCune", "Nolan Marolf", "Isaac Staats", "Alex Newton", "John Putney", "Dustin Grant", "Ian Lane"]
    players_dict = {}
    
    for player in playerNames:
        players_dict[player] = trueskill.Rating()
    players = sortPlayersBySkill(players_dict)

    for i in range(50):
        print(f"Iteration: {i}")

        teams = createTeams(players)
        games = createGames(teams)
        print("Games")
        for game in games:
            printGame(game)
        players_dict = simulateGames(games)
        players = sortPlayersBySkill(players_dict)

        print("Players")
        for player in players:
            print(player)
        print()


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
        (players[game[0][0][0]], players[game[0][1][0]]), (players[game[1][0][0]], players[game[1][1][0]]) = trueskill.rate([t1, t2], ranks=getRandomRanks())
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


def getRandomRanks():
    num = random.randint(0, 1)
    if num == 0:
        return [0, 1]
    return [1, 0]


def getAverageSkill(team : list):
    return (team[0][1].mu + team[1][1].mu)/2.0


def createTeams(players : list):
    players_copy = players.copy()
    nums_list = list(range(len(players)))
    teams = []
    for i in range(int(len(players)/2)):
        team = getTeam(players_copy)
        players_copy.remove(team[0])
        players_copy.remove(team[1])
        teams.append(team)
    return teams


def getTeam(players : list):
    if len(players) >= 4:
        return [players[0], players[random.randint(1, 3)]]
    else:
        return [players[0], players[random.randint(1, len(players)-1)]]


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


# def getScaledValue(value : float):
#     return value/6.0


if __name__ == "__main__":
    main()
