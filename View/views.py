import dominate
from dominate.tags import *
from Model.Player import Player


def homePage():
    doc = dominate.document(title='Home Page')

    with doc:
        h1("Home Page")
        button(a("Players", href="/players"))
        button(a("Create Games", href="/games"))

    return doc.render()


def playersPage(players : list):
    doc = dominate.document(title="Players Page")

    with doc:
        h1("Players")
        list = ul()
        for player in players:
            list.add(li(button(a(player.getName(), href=f"/player/{player.getName()}"), id=player.getName())))
        button(a("Add Player", href="/players/add_player/"))
        button(a("Return to home", href="/"))

    return doc.render()


def playerPage(player : Player):
    doc = dominate.document(title=f"{player.getName()} Stats")

    with doc:
        h1(f"Showing stats for {player.getName()}")
        h3(f"Skill Level: {player.getMu()}")

        button(a("Return to players page", href="/players/"))
        button(a("Return to home", href="/"))

    return doc.render()


def addPlayerPage():
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

        f = form(action="/players/add_player/", method="post")
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

        br()
        button(a("Return to players page", href="/players/"))
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

        f = form(action="/games/", method="post")
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
        button(a("Return to players page", href="/players/"))
        br()
        button(a("Return to home", href="/"))

    return doc.render()


def gamesPageScores(games : list):
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

        f = form(action="/games/", method="post")
        with f:
            t = table()
            row = tr()
            row.add(td("Team One:"))
            row.add(td("Team One Score:"))
            row.add(td("Team Two:"))
            row.add(td("Team Two Score:"))
            t.add(row)
            for game in games:
                row = tr()

                t1 = game.getTeamOneNames()
                row.add(td(f"{t1[0]}, {t1[1]}"))
                row.add(td(game.getTeamOneScore()))

                t2 = game.getTeamTwoNames()
                row.add(td(f"{t2[0]}, {t2[1]}"))
                row.add(td(game.getTeamTwoScore()))
                t.add(row)
                br()

        br()
        button(a("Return to players page", href="/players/"))
        br()
        button(a("Return to home", href="/"))

    return doc.render()
