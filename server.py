from flask import Flask, request
import View.views as views
from Model.Game import Game
from Model.Team import Team
from Model.Player import Player
from Controller.Controller import Controller

app = Flask(__name__)

controller = Controller()

@app.route('/')
def index():
    return views.homePage(controller.getGames())


@app.route('/players/')
def players_page():
    return views.playersPage(controller.getPlayers())


@app.route('/players/add_player/', methods=['GET'])
def add_players_page():
    return views.addPlayerPage(controller.getPlayers())


@app.route('/players/add_player/', methods=['POST'])
def add_player_to_list():
    player = Player(request.form['player_name'], float(request.form['skill_level']), float(request.form['skill_level'])/5)
    controller.getPlayers().append(player)
    return views.addPlayerPage(controller.getPlayers())


@app.route('/player/<string:name>')
def player_page(name):
    print(name)
    player = controller.getPlayerByName(name)
    return views.playerPage(player)


@app.route('/games/')
def create_games():
    controller.createGames()
    return views.gamesPage(controller.getGames())


@app.route('/games/', methods=['POST'])
def update_games():
    for i in range(len(controller.getGames())):
        t1_score = request.form[f't1_score_{i}']
        t2_score = request.form[f't2_score_{i}']
        controller.getGames()[i].setTeamScores(t1_score, t2_score)
        controller.updateRatings(controller.getGames()[i])

    return views.gamesPageScores(controller.getGames())


if __name__ == '__main__':
    app.run(debug=True)