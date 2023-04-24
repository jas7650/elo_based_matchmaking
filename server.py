from flask import Flask, request
import View.views as views
from Model.Game import Game
from Model.Team import Team
from Model.Player import Player
import Controller.elo_system as elo_system
from Controller.controller import Controller

app = Flask(__name__)

controller = Controller()

@app.route('/')
def index():
    return views.homePage()


@app.route('/players/')
def players_page():
    return views.playersPage(controller.getPlayers())


@app.route('/players/add_player/', methods=['GET'])
def add_players_page():
    return views.addPlayerPage()


@app.route('/players/add_player/', methods=['POST'])
def add_player_to_list():
    player = Player(request.form['player_name'], float(request.form['skill_level']), float(request.form['skill_level'])/5)
    controller.getPlayers().append(player)
    return views.addPlayerPage()


@app.route('/player/<string:name>')
def player_page(name):
    print(name)
    player = getPlayerByName(name)
    return views.playerPage(player)


@app.route('/games/')
def create_games():
    controller.setGames(elo_system.createGames(controller.getPlayers()))
    return views.gamesPage(controller.getGames())


@app.route('/games/', methods=['POST'])
def update_games():
    t1_scores = request.form['t1_score']
    t2_scores = request.form['t2_score']
    controller.getGames()[0].setTeamScores(t1_scores, t2_scores)
    return views.gamesPageScores(controller.getGames())


def getPlayerByName(name : str):
    for player in controller.getPlayers():
        if player.getName() == name:
            return player


if __name__ == '__main__':
    # views.renderPages()
    app.run(debug=True)