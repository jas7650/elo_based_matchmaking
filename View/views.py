import dominate
from dominate.tags import *
from Model.Player import Player


def homePage(games : list, players : list):
    doc = dominate.document(title='Home Page')

    with doc.head:
        style("""
        table, tr, td {
            border: 1px solid black;
            border-collapse: collapse;
        }
        """
        )

    with doc:
        h1("Home Page")
        button(a("Add Player", href="/add_player/"))
        button(a("Create Games", href="/games"))

        h1("Players")
        list = ul()
        for player in players:
            list.add(li(button(a(player.getName(), href=f"/player/{player.getName()}"), id=player.getName())))

        h1("Game History")
        t = table()
        row = tr()
        row.add(td("Team One"))
        row.add(td("Score"))
        row.add(td("Team Two"))
        t.add(row)
        for game in games:
            if game.getPlayed() == True:
                row = tr()
                row.add(td(f"{game.getTeamOneNames()[0]}, {game.getTeamOneNames()[1]}"))
                row.add(td(f"{game.getTeamOneScore()}-{game.getTeamTwoScore()}"))
                row.add(td(f"{game.getTeamTwoNames()[0]}, {game.getTeamTwoNames()[1]}"))
                t.add(row)

    return doc.render()


def playerPage(player : Player):
    doc = dominate.document(title=f"{player.getName()} Stats")

    with doc:
        h1(f"Showing stats for {player.getName()}")
        h3(f"Skill Level: {player.getMu()}")
        button(a("Delete Player", href=f"/player/{player.getName()}", method="post"))
        button(a("Return Home", href="/"))

    return doc.render()


def addPlayerPage(players : list):
    doc = dominate.document(title=f"Add Player")

    with doc.head:
        style("""
        table, tr, td {
            border: 1px solid black;
            border-collapse: collapse;
        }
        """
        )

    with doc:
        h1("Add Player Page")

        f = form(action="/add_player/", method="post")
        with f:
            t = table()
            row = tr()
            row.add(td("Player Name"))
            row.add(td(input_(type="text", name="player_name")))
            t.add(row)
            
            row = tr()
            row.add(td("Player Skill"))
            row.add(td(input_(type="text", name="skill_level")))
            t.add(row)

            input_(type="submit", name="form", value="Submit")

        h1("Existing Players")
        list = ul()
        for player in players:
            list.add(li(button(a(player.getName(), href=f"/player/{player.getName()}"), id=player.getName())))
        br()
        button(a("Return to home", href="/"))

    return doc.render()


def gamesPage(games : list):
    doc = dominate.document(title=f"Add Player")

    with doc.head:
        style("""
        table, tr, td {
            border: 1px solid black;
            border-collapse: collapse;
        }
        """
        )

    with doc:
        h1("Games Page")

        f = form(action="/", method="post")
        with f:
            t = table()
            row = tr()
            row.add(td("Team One:"))
            row.add(td("Team One Score:"))
            row.add(td("Team Two:"))
            row.add(td("Team Two Score:"))
            t.add(row)
            for i in range(len(games)):
                game = games[i]
                if game.getPlayed() == False:
                    row = tr()

                    t1 = game.getTeamOneNames()
                    row.add(td(f"{t1[0]}, {t1[1]}"))
                    row.add(td(input_(type="text", name=f"t1_score_{i}")))

                    t2 = game.getTeamTwoNames()
                    row.add(td(f"{t2[0]}, {t2[1]}"))
                    row.add(td(input_(type="text", name=f"t2_score_{i}")))
                    t.add(row)
                    br()
            input_(type="submit", name="form", value="Submit")

        br()
        button(a("Return to home", href="/"))

    return doc.render()
