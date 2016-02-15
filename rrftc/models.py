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


class MatchScouting(db.Model):
    __tablename__ = 'MatchScouting'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Scout = db.Column(db.ForeignKey(u'Scouts.id'), nullable=False, index=True)
    Team = db.Column(db.ForeignKey(u'Teams.id'), nullable=False, index=True)
    Competition = db.Column(db.ForeignKey(u'Competitions.id'), nullable=False, index=True)
    DidRobotMove = db.Column(db.Boolean, nullable=False)
    DidRobotWin = db.Column(db.Boolean, nullable=False)
    DidRobotScoreCycles = db.Column(db.Boolean, nullable=False)
    HowManyCycles = db.Column(db.Integer, nullable=False)
    DidRobotHang = db.Column(db.Boolean, nullable=False)
    DidRobotTriggerClimbers = db.Column(db.Boolean, nullable=False)
    CreateDate = db.Column(db.DateTime, nullable=False)
    LastModifiedDate = db.Column(db.DateTime, nullable=False)

    Competition1 = db.relationship(u'Competition')
    Scout1 = db.relationship(u'Scout')
    Team1 = db.relationship(u'Team')

    def __init__(self,
                 scout,
                 team,
                 comp,
                 move,
                 win,
                 score,
                 cycles,
                 hang,
                 trigger,
                 createdate=time.strftime('%Y-%m-%d %H:%M:%S'),
                 moddate=time.strftime('%Y-%m-%d %H:%M:%S')):
        self.Scout = scout
        self.Team = team
        self.Competition = comp
        self.DidRobotMove = move
        self.DidRobotWin = win
        self.DidRobotScoreCycles = score
        self.HowManyCycles = cycles
        self.DidRobotHang = hang
        self.DidRobotTriggerClimbers = trigger
        self.CreateDate = createdate
        self.LastModifiedDate = moddate

    def __repr__(self):
        return '<Match Scouting Report %r>' % self.id


class Scouting(db.Model):
    __tablename__ = 'Scouting'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Scout = db.Column(db.ForeignKey(u'Scouts.id'), nullable=False, index=True)
    Team = db.Column(db.ForeignKey(u'Teams.id'), nullable=False, index=True)
    Competition = db.Column(db.ForeignKey(u'Competitions.id'), nullable=False, index=True)
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
    WatchList = db.Column(db.Boolean, nullable=False)
    CreateDate = db.Column(db.DateTime, nullable=False)
    LastModifiedDate = db.Column(db.DateTime, nullable=False)

    Competition1 = db.relationship(u'Competition')
    Scout1 = db.relationship(u'Scout')
    Team1 = db.relationship(u'Team')

    def __init__(self,
                 scout,
                 team,
                 comp,
                 autonomous,
                 pushbeacon,
                 deliverclimbers,
                 lclimber,
                 mclimber,
                 hclimber,
                 fpark,
                 lpark,
                 mpark,
                 hpark,
                 highestzone,
                 scoredebris,
                 ldebris,
                 mdebris,
                 hdebris,
                 avgdebris,
                 debrismethod,
                 hang,
                 allclear,
                 spof,
                 comments,
                 watchlist,
                 createdate=time.strftime('%Y-%m-%d %H:%M:%S'),
                 moddate=time.strftime('%Y-%m-%d %H:%M:%S')):
        self.Scout = scout
        self.Team = team
        self.Competition = comp
        self.IsAutonomous = autonomous
        self.CanPushBeacon = pushbeacon
        self.CanDeliverClimbers = deliverclimbers
        self.DeliverClimberLow = lclimber
        self.DeliverClimberMid = mclimber
        self.DeliverClimberHigh = hclimber
        self.CanParkOnFloor = fpark
        self.CanParkOnLowZone = lpark
        self.CanParkOnMidZone = mpark
        self.CanParkOnHighZone = hpark
        self.HighestZoneClimbed = highestzone
        self.CanScoreDebris = scoredebris
        self.CanScoreInLowZone = ldebris
        self.CanScoreInMidZone = mdebris
        self.CanScoreInHighZone = hdebris
        self.DebrisAverageScore = avgdebris
        self.DebrisScoringMethod = debrismethod
        self.CanHang = hang
        self.CanTriggerAllClearSignal = allclear
        self.PossiblePointsOfFailure = spof
        self.GeneralComments = comments
        self.WatchList = watchlist
        self.CreateDate = createdate
        self.LastModifiedDate = moddate

    def __repr__(self):
        return '<Scouting Report %r>' % self.id


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