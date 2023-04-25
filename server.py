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
    return views.homePage(controller.getGames(), controller.getPlayers())

@app.route('/', methods=['POST'])
def update_games():
    for i in range(len(controller.getGames())):
        game = controller.getGames()[i]
        if game.getPlayed() == False:
            t1_score = request.form[f't1_score_{i}']
            t2_score = request.form[f't2_score_{i}']
            print(t1_score)
            if t1_score != "" and t2_score != "":
                game.setTeamScores(t1_score, t2_score)
                game.setPlayed()
                controller.updateRatings(game)
    return views.homePage(controller.getGames(), controller.getPlayers())


@app.route('/add_player/', methods=['GET'])
def add_players_page():
    return views.addPlayerPage(controller.getPlayers())


@app.route('/add_player/', methods=['POST'])
def add_player_to_list():
    player = Player(request.form['player_name'], float(request.form['skill_level']), float(request.form['skill_level'])/5)
    if controller.getPlayerByName(player.getName()) == None:
        controller.getPlayers().append(player)
    return views.addPlayerPage(controller.getPlayers())


@app.route('/player/<string:name>', methods=['GET'])
def player_page_get(name):
    player = controller.getPlayerByName(name)
    return views.playerPage(player)


@app.route('/player/<string:name>', methods=['POST'])
def player_page_post(name):
    controller.removePlayer(name)
    return views.playerPage(None)


@app.route('/games/')
def create_games():
    controller.createGames()
    return views.gamesPage(controller.getGames())


if __name__ == '__main__':
    app.run(debug=True)