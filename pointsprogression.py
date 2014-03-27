from fplplayers import Data
from games import Games

d = Data('data.json')
g = Games('E0.csv')

#all_teams = list(d.all_teams())
all_teams = ['Arsenal', 'Chelsea', 'Liverpool', 'Man City']#, 'Man Utd', 'Everton', 'Tottenham',]


temp_points_progressions = [g.of_team(t).points_progression_for(t) for t in all_teams]

points_progressions = []
for p in temp_points_progressions:
    points_progressions.append([0,] + p)

import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
ax.set_ylabel('Points')
ax.set_xlabel('Gameweek')
ax.set_title('Points progression')
ax.set_xticks(np.arange(38)+1)
ax.set_yticks(np.arange(0,114,3))
#ax.legend TODO
lines = []
for team, points in zip(all_teams, points_progressions):
    lines.append(ax.plot(np.arange(len(points)), points))

ax.legend( tuple([line[0] for line in lines]), tuple(all_teams), loc=4)
ax.yaxis.grid(color='gray')
ax.xaxis.grid(color='gray')
ax.set_axisbelow(True)
plt.show()
