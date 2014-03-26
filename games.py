import csv
from datetime import datetime
from team import Team

class Games:


    # TODO should be able to handle multiple csv files and
    # load them all to same self.games attribute
    def __init__(self, csvfile):
        with open(csvfile, 'r') as f:
            reader = csv.reader(f)
            header = reader.next()
            self.games = [Game(row, header) for row in reader]

    def of_team(self, teamname):
        return [g for g in self.games if Team(teamname) in [g.hometeam, g.awayteam]]


    def of_team_at_home(self, teamname):
        return [g for g in self.games if teamname == g.hometeam]
   

    def of_team_at_away(self, teamname):
        return [g for g in self.games if teamname == g.awayteam]



class Game:

    def __init__(self, row, header):
        for (key, value) in zip(header, row):
            try:
                val = int(value)
            except ValueError:
                val = value
            self.__dict__[''.join(e for e in key.lower() if e.isalnum())] = val
        self.date = datetime.strptime(self.date, '%d/%m/%y')
        self.hometeam = Team(self.hometeam)
        self.awayteam = Team(self.awayteam)
        
        if self.fthg > self.ftag:
            self.homepoints = 3
            self.awaypoints = 0
        elif self.fthg == self.ftag:
            self.homepoints = 1
            self.awaypoints = 1
        else:
            self.homepoints = 0
            self.awaypoints = 3

    def points_for(self, teamname):
        if teamname == self.hometeam:
            return self.homepoints
        elif teamname == self.awayteam:
            return self.awaypoints
        else:
            raise Exception(str(teamname)+" does not partake in this game")

    def __repr__(self):
        return str(self.date)+' '+self.hometeam.name+' vs '+self.awayteam.name
