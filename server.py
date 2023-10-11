from flask import Flask, request, redirect, url_for, render_template
from Model.Game import Game
from Model.Team import Team
from Model.Player import Player
from Controller.Controller import Controller
from Model.Group import Group
from pymongo import MongoClient

app = Flask(__name__)

global controller

@app.route('/', methods = ['GET'])
def home_page():
    if request.method == 'GET':
        return render_template('home.html', groups=list(controller.getGroups().values()))  


@app.route('/group/<string:name>/add_player/', methods=['GET', 'POST'])
def add_players_page(name):
    group = controller.getGroup(name)
    if request.method == 'POST':
        skill_level = getSkillLevel(request.form['skill_level'])
        player = Player(request.form['player_name'], skill_level, skill_level/5)
        group.addPlayer(player)
        create_player(player, group.getGroupName())
    return render_template('add_player.html', players=group.getPlayers(), group=group, groups=list(controller.getGroups().values()))


@app.route('/group/<string:group_name>/player/<string:player_name>/', methods=['GET', 'POST'])
def player_page(group_name, player_name):
    group = controller.getGroup(group_name)
    if request.method == 'GET':
        player = group.getPlayer(player_name)
        return render_template('player.html', player=player, games=group.getGames(), group=group, groups=list(controller.getGroups().values()))
    elif request.method == 'POST':
        delete_player(group.getPlayer(player_name), group_name)
        group.removePlayer(player_name)
        return redirect(url_for('groups_page', name=group_name))


@app.route('/group/<string:name>/games/', methods = ['GET', 'POST'])
def games_page(name):
    group = controller.getGroup(name)
    if request.method == 'GET':
        group.createGames()
        return render_template('games.html', games=group.getGames(), name=name, groups=list(controller.getGroups().values()))
    elif request.method == 'POST':
        for i in range(len(group.getGames())):
            game = group.getGames()[i]
            if game.getPlayed() == False:
                t1_score = request.form[f't1_score_{i}']
                t2_score = request.form[f't2_score_{i}']
                if t1_score != "" and t2_score != "":
                    game.setScore([t1_score, t2_score])
                    game.setPlayed()
                    group.updateRatings(game)
        return redirect(url_for('groups_page', name=name))


@app.route('/create_group/', methods=['GET', 'POST'])
def create_group_page():
    if request.method == 'GET':
        return render_template('create_group.html', groups=list(controller.getGroups().values()))
    elif request.method == 'POST':
        group_name = request.form['group_name']
        controller.createGroup(group_name)
        return redirect(url_for('groups_page', name=group_name))


@app.route('/group/<string:name>/', methods=['GET', 'POST'])
def groups_page(name):
    group = controller.getGroup(name)
    return render_template('group.html', group=controller.getGroup(name), players=group.getPlayers(), games=group.getGames(), groups=list(controller.getGroups().values()))


def get_database():
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb+srv://justinshaytar:Myla349139money@cluster0.dch1den.mongodb.net/"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database for our example (we will use the same database throughout the tutorial
    return client['matchmaking_db']


def insert_values(player_names, group_name):
    dbname = get_database()
    collection_name = dbname[group_name]
    first_names = ['Justin', 'Alex', 'Sam', 'Isaac']
    last_names = ['Shaytar', 'Newton', 'McCune', 'Staats']
    mus = ['6.0', '5.25', '5.0', '4.75']
    # sigmas = ['6.0', '5.25', '5.0', '4.75']

    for i in range(len(first_names)):
        if f"{first_names[i]} {last_names[i]}" not in player_names:
            player = {
            "player_first_name" : f"{first_names[i]}",
            "player_last_name" : f"{last_names[i]}",
            "mu" : f"{mus[i]}"
            }
            collection_name.insert_one(player)


def delete_player(player : Player, group_name):
    dbname = get_database()
    collection_name = dbname[group_name]
    collection_name.delete_one({"player_first_name" : f"{player.getName().split()[0]}", "player_last_name" : f"{player.getName().split()[1]}", "mu" : f"{player.getMuRounded()}"})


def create_player(player : Player, group_name : str):
    db_name = get_database()
    collection = db_name[group_name]
    collection.insert_one({"player_first_name" : f"{player.getName().split()[0]}", "player_last_name" : f"{player.getName().split()[1]}", "mu" : f"{player.getMuRounded()}"})


def get_players(group_name):
    return get_database()[group_name].find()


def getSkillLevel(option : str):
    if option == "Pro":
        return float(6.0)
    elif option == "Premier I":
        return float(5.0)
    elif option == "Premier II":
        return float(5.25)
    elif option == "Premier III":
        return float(5.5)
    elif option == "Contender I":
        return float(4.5)
    elif option == "Contender II":
        return float(4.67)
    elif option == "Contender III":
        return float(4.82)
    elif option == "Advanced I":
        return float(4.0)
    elif option == "Advanced II":
        return float(4.17)
    elif option == "Advanced III":
        return float(4.34)
    elif option == "Intermediate I":
        return float(3.0)
    elif option == "Intermediate II":
        return float(3.33)
    elif option == "Intermediate III":
        return float(3.67)
    else:
        return float(2.0)


if __name__ == '__main__':
    controller = Controller()

    db = get_database()
    groups = db['groups'].find()
    for group in groups:
        controller.createGroup(group['group_name'])
        players = db[group['group_name']].find()
        games = db[f"{group['group_name']} Games"].find()
        for player in players:
            player_object = Player(f"{player['player_first_name']} {player['player_last_name']}", float(player['mu']), 1.0)
            controller.getGroup(group['group_name']).addPlayer(player_object)
        for game in games:
            team_one = [game['player_one'], game['player_two']]
            team_two = [game['player_three'], game['player_four']]
            game_object = Game(team_one, team_two)
            game_object.setScore([int(game['team_one_score']), int(game['team_two_score'])])
            game_object.setPlayed()
            controller.addGame(game_object, group['group_name'])

    app.run(debug=True)
