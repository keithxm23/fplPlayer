
class Team:

    TEAMS = [
            ('Arsenal','ARS',),
            ('Liverpool','LIV',),
            ('Norwich','NOR',),
            ('Sunderland','SUN',),
            ('Aston Villa','AVL',),
            ('Stoke','STK','Stoke City',),
            ('Everton','EVE',),
            ('Fulham','FUL',),
            ('Swansea','SWA',),
            ('Man United','MUN','Man Utd',),
            ('Southampton','SOU',),
            ('West Brom','WBA',),
            ('West Ham','WHU',),
            ('Cardiff','CAR','Cardiff City',),
            ('Chelsea','CHE',),
            ('Hull','HUL','Hull City',),
            ('Crystal Palace','CRY',),
            ('Tottenham','TOT',),
            ('Man City','MCI',),
            ('Newcastle','NEW',),
            ]

    def __init__(self, name):
        if not any(name in names for names in self.TEAMS):
            errormsg = name+ " is not a valid team name."
            raise ValueError(errormsg)
        self.name = name

    def __eq__(self, other):
        for names in self.TEAMS:
            if self.name in names and other.name in names:
                return True
        return False

    def __repr__(self):
        return self.name
