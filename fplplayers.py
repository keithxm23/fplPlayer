import simplejson as json
from games import Game
from team import Team
from datetime import datetime

class Data:

    # Instantiate with path to json file
    def __init__(self, jsonfile):
        #with open(csvfile, 'r') as f:
        #    self.games = [Game(g) for g in csvfile.readlines(f)]
        

        with  open(jsonfile, 'r') as f:
            self.players = [Player(p) for p in json.load(f)]


    # List all players
    def all(self):
        return self.players

    # Returns a set of all team names
    def all_teams(self):
        return set([p['team_name'] for p in self.players])
    
    # Returns a set of all player status values
    ## a => available
    ## d => maybe injured
    ## i => injured
    ## n => not allowed (on loan)
    ## s => suspended
    ## u => unavailable
    def all_statuses(self):
        return set([p['status'] for p in self.players])

    # List players 'of' team xyz(ManU?)
    def of(self, team):
        return [p for p in self.players if p['team_name'] == team]



class Player:

    def __init__(self, playerdict):
        #print 'Initializing player: '+ playerdict['web_name']
        self.fixtures = [Fixture(f, occured=True) for f in
                playerdict['fixture_history']['all']]
        self.web_name = playerdict['web_name'].encode('utf-8')
        self.first_name = playerdict['first_name'].encode('utf-8')
        self.second_name = playerdict['second_name'].encode('utf-8')
        self.team_name = Team(playerdict['team_name'])
        self.fixtures.extend([Fixture(f, occured=False) for f in  playerdict['fixtures']['all'] if len(f[0]) > 2]) 

    def __repr__(self):
        return self.web_name

class Fixture:

    def __init__(self, fixture, occured):
        self.occured = occured # whether fixture has occured or not 
        self.date = fixture[0][:-5]
        if not self.occured:
            self.opponent = Team(fixture[2][:-4])
            self.gameweek = fixture[1].split()[1]
            self.playedat = fixture[2][-2]
        else:
            self.gameweek = fixture[1] # Gameweek
            self.opponent = Team(fixture[2].split()[0][0:3]) # Opponent, 3 letter code
            self.playedat = fixture[2].split()[0][4] # played at Home, Away
            self.goalsfor = fixture[2].split()[1].split('-')[0] # goals for
            self.goalsallowed = fixture[2].split()[1].split('-')[1] # goals allowed
            self.minutesplayed = fixture[3]
            self.goals = fixture[4]
            self.assists = fixture[5]
            self.cleansheets = fixture[6]
            self.conceded = fixture[7]
            self.owngoals = fixture[8]
            self.penaltiessaved = fixture[9]
            self.penalitesmissed = fixture[10]
            self.yellows = fixture[11]
            self.reds = fixture[12]
            self.saves = fixture[13]
            self.bonuspoints = fixture[14]
            self.esp = fixture[15] # EA Sports PPI
            self.bps = fixture[16] # Bonus Points System
            self.nettransfers = fixture[17]
            self.value = fixture[18]
            self.points = fixture[19]

    def __repr__(self):
        return str(self.date)+" "+self.opponent.name
