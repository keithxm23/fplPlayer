# Utility functions to work with arrays of 'Games'

def points(games, teamname):
    total_points = 0
    for g in games:
        if teamname not in [g.hometeam, g.awayteam]:
            print teamname + ' not featured in game: ' + g.hometeam + ' vs ' \
                    +  g.awayteam
        elif teamname == g.hometeam:
            if g.fthg > g.ftag:
                total_points += 3
            elif g.fthg == g.ftag:
                total_points += 1
        else:
            if g.ftag > g.fthg:
                total_points += 3
            elif g.ftag == g.fthg:
                total_points += 1
    return total_points


def points_dropped(games, teamname):
    total_points = 0
    for g in games:
        if teamname not in [g.hometeam, g.awayteam]:
            print teamname + ' not featured in game: ' + g.hometeam + ' vs ' \
                    +  g.awayteam
        elif teamname == g.hometeam:
            if g.fthg < g.ftag:
                total_points += 3
            elif g.fthg == g.ftag:
                total_points += 2
        else:
            if g.ftag < g.fthg:
                total_points += 3
            elif g.ftag == g.fthg:
                total_points += 2
    return total_points
