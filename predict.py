from gameutils import points
from fplplayers import Data
d = Data('data.json')

from games import Games
g = Games('E0.csv')

predictedpoints = {}
finalpoints = []
currentpoints = []
for team, fixtures in d.fixturestoplay.items():
    predictedpoints[team] = 0
    for f in fixtures:
        if f.playedat == 'A':
            for gm in g.of_team_at_home(team):
                if f.opponent == gm.awayteam:
                    predictedpoints[team] += gm.homepoints
                    #print team+ ' scored '+str(gm.homepoints)+' against '+gm.awayteam.name
                    break
        else:
            for gm in g.of_team_at_away(team):
                if f.opponent == gm.hometeam:
                    predictedpoints[team] += gm.awaypoints
                    #print team+ ' scored '+str(gm.awaypoints)+' against '+gm.hometeam.name
                    break

    finalpoints.append((team, predictedpoints[team] +
        points(g.of_team(team),team), points(g.of_team(team),team)))

finalpoints.sort(key=lambda x: x[1],reverse=True)

tmp = finalpoints[1]
finalpoints[1] = finalpoints [0]
finalpoints[0] = tmp

# Now for the plotting fun
import numpy as np
import matplotlib.pyplot as plt

N = 20
ind = np.arange(N)
width = 0.35

fig, ax = plt.subplots()
rects1 = ax.bar(ind, [x[1] for x in finalpoints], width, color='r')
rects2 = ax.bar(ind+width, [x[2] for x in finalpoints], width, color='b')

ax.set_ylabel('Points')
ax.set_title('Predicted points by past reverse fixtures')
ax.set_xticks(ind+width)
ax.set_xticklabels(tuple([x[0] for x in finalpoints]), rotation='vertical')

ax.legend((rects1[0], rects2[0]), ('Predicted', 'Current'))

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2.,1.01*height,
                '%d'%int(height), ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

plt.show()







