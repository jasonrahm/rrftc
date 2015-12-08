from flask_sqlalchemy import SQLAlchemy
import time

db = SQLAlchemy()

class CompetitionTeam(db.Model):
    __tablename__ = 'CompetitionTeams'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Competitions = db.Column(db.ForeignKey(u'Competitions.id'), nullable=False, index=True)
    Teams = db.Column(db.ForeignKey(u'Teams.id'), nullable=False, index=True)
    CreateDate = db.Column(db.DateTime, nullable=False)

    Competition = db.relationship(u'Competition')
    Team = db.relationship(u'Team')

    def __init__(self, competitions, teams, createdate=time.strftime('%Y-%m-%d %H:%M:%S')):
        self.Competitions = competitions
        self.Teams = teams
        self.CreateDate = createdate


    def __repr__(self):
        return '<CompetitionTeam %r %r %r>' % (self.id, self.Competitions, self.Teams)


class Competition(db.Model):
    __tablename__ = 'Competitions'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Name = db.Column(db.String(120), nullable=False)
    Date = db.Column(db.Date, nullable=False)
    Location = db.Column(db.String(120))
    CreateDate = db.Column(db.DateTime, nullable=False)
    LastModifiedDate = db.Column(db.DateTime, nullable=False)

    def __init__(self, name, date, location, createdate=time.strftime('%Y-%m-%d %H:%M:%S'), moddate=time.strftime('%Y-%m-%d %H:%M:%S')):
        self.Name = name
        self.Date = date
        self.Location = location
        self.CreateDate = createdate
        self.LastModifiedDate = moddate

    def __repr__(self):
        return '<Competition %r>' % self.id


class Match(db.Model):
    __tablename__ = 'Matches'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Competition = db.Column(db.ForeignKey(u'Competitions.id'), nullable=False, index=True)
    BlueTeam1 = db.Column(db.ForeignKey(u'Teams.id'), nullable=False, index=True)
    BlueTeam2 = db.Column(db.ForeignKey(u'Teams.id'), nullable=False, index=True)
    RedTeam1 = db.Column(db.ForeignKey(u'Teams.id'), nullable=False, index=True)
    RedTeam2 = db.Column(db.ForeignKey(u'Teams.id'), nullable=False, index=True)

    Team = db.relationship(u'Team', primaryjoin='Match.BlueTeam1 == Team.id')
    Team1 = db.relationship(u'Team', primaryjoin='Match.BlueTeam2 == Team.id')
    Competition1 = db.relationship(u'Competition')
    Team2 = db.relationship(u'Team', primaryjoin='Match.RedTeam1 == Team.id')
    Team3 = db.relationship(u'Team', primaryjoin='Match.RedTeam2 == Team.id')

    def __init__(self, competition, blueteam1, blueteam2, redteam1, redteam2):
        self.Competition = competition
        self.BlueTeam1 = blueteam1
        self.BlueTeam2 = blueteam2
        self.RedTeam1 = redteam1
        self.RedTeam2 = redteam2

    def __repr__(self):
        return '<Match %r>' % self.id


class Scouting(db.Model):
    __tablename__ = 'Scouting'

    id = db.Column(db.Boolean, primary_key=True, autoincrement=True)
    Scout = db.Column(db.ForeignKey(u'Scouts.id'), nullable=False, index=True)
    Team = db.Column(db.ForeignKey(u'Teams.id'), nullable=False, index=True)
    Competition = db.Column(db.ForeignKey(u'Competitions.id'), nullable=False, index=True)
    RobotWeight = db.Column(db.Float, nullable=False)
    RobotHeight = db.Column(db.Float, nullable=False)
    IsAutonomous = db.Column(db.Boolean, nullable=False)
    CanPushBeacon = db.Column(db.Boolean, nullable=False)
    CanDeliverClimbers = db.Column(db.Boolean, nullable=False)
    DeliverClimberLow = db.Column(db.Boolean, nullable=False)
    DeliverClimberMid = db.Column(db.Boolean, nullable=False)
    DeliverClimberHigh = db.Column(db.Boolean, nullable=False)
    CanParkOnFloor = db.Column(db.Boolean, nullable=False)
    CanParkOnLowZone = db.Column(db.Boolean, nullable=False)
    CanParkOnMidZone = db.Column(db.Boolean, nullable=False)
    CanParkOnHighZone = db.Column(db.Boolean, nullable=False)
    HighestZoneClimbed = db.Column(db.String(120), nullable=False)
    CanScoreDebris = db.Column(db.Boolean, nullable=False)
    CanScoreInLowZone = db.Column(db.Boolean, nullable=False)
    CanScoreInMidZone = db.Column(db.Boolean, nullable=False)
    CanScoreInHighZone = db.Column(db.Boolean, nullable=False)
    DebrisAverageScore = db.Column(db.Integer, nullable=False)
    DebrisScoringMethod = db.Column(db.String(120), nullable=False)
    CanHang = db.Column(db.Boolean, nullable=False)
    CanTriggerAllClearSignal = db.Column(db.Boolean, nullable=False)
    PossiblePointsOfFailure = db.Column(db.Text, nullable=False)
    GeneralComments = db.Column(db.Text, nullable=False)
    CreateDate = db.Column(db.DateTime, nullable=False)
    LastModifiedDate = db.Column(db.DateTime, nullable=False)

    Competition1 = db.relationship(u'Competition')
    Scout1 = db.relationship(u'Scout')
    Team1 = db.relationship(u'Team')


class Scout(db.Model):
    __tablename__ = 'Scouts'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Name = db.Column(db.String(120), nullable=False)
    CreateDate = db.Column(db.DateTime, nullable=False)
    LastModifiedDate = db.Column(db.DateTime, nullable=False)

    def __init__(self,
                 name,
                 createdate=time.strftime('%Y-%m-%d %H:%M:%S'),
                 moddate=time.strftime('%Y-%m-%d %H:%M:%S')):
        self.Name = name
        self.CreateDate = createdate
        self.LastModifiedDate = moddate

    def __repr__(self):
        return '<Scout %r>' % self.id


class Team(db.Model):
    __tablename__ = 'Teams'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Number = db.Column(db.Integer, nullable=False)
    Name = db.Column(db.String(120), nullable=False)
    Website = db.Column(db.String(120))
    CreateDate = db.Column(db.DateTime, nullable=False)
    LastModifiedDate = db.Column(db.DateTime, nullable=False)

    def __init__(self,
                 number,
                 name,
                 website,
                 createdate=time.strftime('%Y-%m-%d %H:%M:%S'),
                 moddate=time.strftime('%Y-%m-%d %H:%M:%S')):
        self.Number = number
        self.Name = name
        self.Website = website
        self.CreateDate = createdate
        self.LastModifiedDate = moddate

    def __repr__(self):
        return '<Team %r %r %r>' % (self.id, self.Number, self.Name)