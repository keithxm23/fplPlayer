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
        return [g for g in self.games if teamname in [g.hometeam, g.awayteam]]


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
        self.__dict__['date'] = datetime.strptime(self.date, '%d/%m/%y')
        self.__dict__['hometeam'] = Team(self.hometeam)
        self.__dict__['awayteam'] = Team(self.awayteam)

    def __setattr__(self, name, value):
        raise "Game is a read-only class"
