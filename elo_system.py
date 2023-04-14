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
        player = playerNames[i]
        mu = i
        players_dict[player] = trueskill.Rating(mu=mu)

    for i in range(5):
        teams = createTeams(players_dict)

        for team in teams:
            print(f"Player One: {team[0]}, Player Two: {team[1]}")
        print()
        games = createGames(teams)
        # players_list = list(players_dict)
        # for player in players_dict:
        #     print(f"Player: {player}, Rating: {players_dict[player]}")
        # print()
        # players_dict = sortPlayersBySkill(players_dict)

    # for player in players_dict:
    #     print(f"Player: {player}, Rating: {players_dict[player]}")
    #     print()


def createGames(teams : list):
    for team in teams:
        teams.append(getAverageSkill(team))


def getAverageSkill(team : list):
    return (team[0].mu + team[1].mu)/2.0


def createTeams(players_dict : dict):
    nums_list = list(range(len(players_dict)))
    players = list(players_dict)
    teams = []
    for i in range(int(len(players_dict)/2)):
        index = random.randint(0, len(nums_list)-1)
        p1 = players[nums_list[index]]
        nums_list.remove(nums_list[index])

        index = random.randint(0, len(nums_list)-1)
        p2 = players[nums_list[index]]
        nums_list.remove(nums_list[index])
        teams.append([p1, p2])
    return teams


def sortPlayersBySkill(players : dict):
    return dict(sorted(players.items(), key=lambda item: item[1], reverse=True))


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


# def mergeSort(players : list):
#     if len(players) == 0:
#         return []
#     elif len(players) == 1:
#         return [players[0]]
#     else:
#         index = math.floor(int(len(players)/2))
#         left = mergeSort(players[:index])
#         right =  mergeSort(players[index:])
#         return merge(left, right)
    

# def merge(left : list, right : list):
#     l = 0
#     r = 0
#     sorted_list = []
#     while l < len(left) and r < len(right):
#         if left[l][1].mu < right[r][1].mu:
#             sorted_list.append(right[r])
#             r += 1
#         else:
#             sorted_list.append(left[l])
#             l += 1
#     while l < len(left):
#         sorted_list.append(left[l])
#         l += 1
#     while r < len(right):
#         sorted_list.append(right[r])
#         r += 1
#     return sorted_list


if __name__ == "__main__":
    main()
