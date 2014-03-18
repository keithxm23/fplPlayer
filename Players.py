import simplejson as json

class Players:

    # Instantiate with path to json file
    def __init__(self, jsonfile):
        f = open(jsonfile, 'r')
        self.players = [Player(p) for p in json.load(f)]

    # List all players
    def all(self):
        return self.players

    # Returns a set of all team names
    ## a => available
    ## d => maybe injured
    ## i => injured
    ## n => not allowed (on loan)
    ## s => suspended
    ## u => unavailable
    def all_teams(self):
        return set([p['team_name'] for p in self.players])
    
    # Returns a set of all player status values
    def all_statuses(self):
        return set([p['status'] for p in self.players])

    # List players 'of' team xyz(ManU?)
    def of(self, team):
        return [p for p in self.players if p['team_name'] == team]



class Player:

    def __init__(self, playerdict):
        self.fixtures = [Fixture(f) for f in
                playerdict['fixture_history']['all']]
        self.name = playerdict['web_name']

class Fixture:

    def __init__(self, fixture):
        self.date = fixture[0]
        self.gameweek = fixture[1] # Gameweek
        self.opponent = fixture[2].split()[0][0:3] # Opponent, 3 letter code
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

