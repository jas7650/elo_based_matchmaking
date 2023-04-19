import trueskill
import random
import sheet_utils
import argparse


def main():

    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter)
    mode_parser = parser.add_mutually_exclusive_group(required=True)
    mode_parser.add_argument(
        '-s',
        dest='simulate',
        default=False,
        action='store_true',
        required=False,
        help="Option to run simulation of games"
    )
    mode_parser.add_argument(
        '-g',
        dest='create_games',
        default=False,
        action='store_true',
        required=False,
        help="Option to generate games based on existing list of players"
    )
    args = parser.parse_args()
    if args.simulate == True:
        simulate()
    if args.create_games == True:
        generateMatches()


def simulate():
    wb = sheet_utils.getWorkBook("elo_database.xlsx")
    sheet = sheet_utils.getSheetByName(wb, "Data")
    playerNames = sheet_utils.getColumnData(sheet, 1)
    mus = sheet_utils.getColumnData(sheet, 2)
    sigmas = sheet_utils.getColumnData(sheet, 3)

    wb = sheet_utils.removeSheets(wb)

    players_dict = {}
    
    for i in range(len(playerNames)):
        players_dict[playerNames[i]] = trueskill.Rating(mu=float(mus[i]), sigma=float(sigmas[i]))
    players = sortPlayersBySkill(players_dict)

    for i in range(50):
        print(f"Iteration: {i}")

        games = createGames(players)
        print("Games")
        for game in games:
            printGame(game)
        players_dict = simulateGames(games)
        players = sortPlayersBySkill(players_dict)

        print("Players")
        for player in players:
            print(player)
        print()

    writePlayersToSheet(wb, players)


def generateMatches():
    wb = sheet_utils.getWorkBook("elo_database.xlsx")
    sheet = sheet_utils.getSheetByName(wb, "Data")
    playerNames = sheet_utils.getColumnData(sheet, 1)
    mus = sheet_utils.getColumnData(sheet, 2)
    sigmas = sheet_utils.getColumnData(sheet, 3)

    players_dict = {}
    
    for i in range(len(playerNames)):
        players_dict[playerNames[i]] = trueskill.Rating(mu=float(mus[i]), sigma=float(sigmas[i]))
    players = sortPlayersBySkill(players_dict)

    print("Players")
    for player in players:
        print(player)
    print()

    games = createGames(players)
    print("Games")
    for game in games:
        printGame(game)


def writePlayersToSheet(wb, players : list):
    playerNames = ["Player"]
    mus = ["Mu"]
    sigmas = ["Sigma"]
    for player in players:
        playerNames.append(player[0])
        mus.append(player[1].mu)
        sigmas.append(player[1].sigma)
    data = [playerNames, mus, sigmas]
    sheet_utils.writeToSheet(data, wb, "Data")
    sheet_utils.saveWorkBook(wb, "elo_database.xlsx")


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


def createGames(players : list):
    games = []
    teams = []
    players_copy = players.copy()

    for i in range(int(len(players)/4)):
        people = []
        for j in range(4):
            player = players_copy[random.randint(0, getUpperLimit(players_copy, j))]
            people.append(player)
            players_copy.remove(player)
        team = []
        team.append(people[random.randint(0, 3)])
        people.remove(team[0])
        team.append(people[random.randint(0, 2)])
        people.remove(team[1])
        teams.append(team)

        team = []
        team.append(people[0])
        team.append(people[1])
        teams.append(team)


    for team in teams:
        team.append(getAverageSkill(team))
    teams = sortTeamsBySkill(teams)
    for i in range(0, len(teams)-1, 2):
        game = [teams[i], teams[i+1]]
        games.append(game)
    return games


def getUpperLimit(list : list, iteration : int):
    if len(list) <= 5:
        return len(list)-1
    else:
        return 5-iteration


def getRandomRanks():
    num = random.randint(0, 1)
    if num == 0:
        return [0, 1]
    return [1, 0]


def getAverageSkill(team : list):
    return (team[0][1].mu + team[1][1].mu)/2.0


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
