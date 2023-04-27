from flask import Flask, request, redirect, url_for, render_template
from Model.Game import Game
from Model.Team import Team
from Model.Player import Player
from Controller.Controller import Controller

app = Flask(__name__)

controller = Controller()

@app.route('/', methods = ['GET'])
def home_page():
    if request.method == 'GET':
        return render_template('home.html', players=controller.getPlayers(), games=controller.getGames())  


@app.route('/add_player/', methods=['GET', 'POST'])
def add_players_page():
    if request.method == 'POST':
        player = Player(request.form['player_name'], float(request.form['skill_level']), float(request.form['skill_level'])/5)
        if controller.getPlayerByName(player.getName()) == None:
            controller.getPlayers().append(player)
    return render_template('add_player.html', players=controller.getPlayers())


@app.route('/player/<string:name>/', methods=['GET', 'POST'])
def player_page(name):
    if request.method == 'GET':
        player = controller.getPlayerByName(name)
        return render_template('player.html', player=player, games=controller.getGames())
    elif request.method == 'POST':
        controller.removePlayer(name)
        return redirect(url_for('home_page'))


@app.route('/games/', methods = ['GET', 'POST'])
def games_page():
    if request.method == 'GET':
        controller.createGames()
        return render_template('games.html', games=controller.getGames())
    elif request.method == 'POST':
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
        return redirect(url_for('home_page'))


if __name__ == '__main__':
    app.run(debug=True)