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
    MatchNumber = db.Column(db.Integer, nullable=False)
    DidRobotMove = db.Column(db.Boolean, nullable=False)
    DeliverClimbers = db.Column(db.Boolean, nullable=False)
    PushBeacon = db.Column(db.Boolean, nullable=False)
    ParkingLevel = db.Column(db.Integer, nullable=False)
    DidRobotScoreCycles = db.Column(db.Boolean, nullable=False)
    HowManyCycles = db.Column(db.Integer, nullable=False)
    ScoreLowZone = db.Column(db.Boolean, nullable=False)
    ScoreMidZone = db.Column(db.Boolean, nullable=False)
    ScoreHighZone = db.Column(db.Boolean, nullable=False)
    ReleaseLowClimber = db.Column(db.Boolean, nullable=False)
    ReleaseMidClimber = db.Column(db.Boolean, nullable=False)
    ReleaseHighClimber = db.Column(db.Boolean, nullable=False)
    DidRobotHang = db.Column(db.Boolean, nullable=False)
    DidRobotTriggerClimbers = db.Column(db.Boolean, nullable=False)
    DidRobotWin = db.Column(db.Boolean, nullable=False)
    CreateDate = db.Column(db.DateTime, nullable=False)
    LastModifiedDate = db.Column(db.DateTime, nullable=False)

    Competition1 = db.relationship(u'Competition')
    Scout1 = db.relationship(u'Scout')
    Team1 = db.relationship(u'Team')

    def __init__(self,
                 scout,
                 team,
                 comp,
                 match,
                 move,
                 climbers,
                 beacon,
                 park,
                 score,
                 cycles,
                 scorelow,
                 scoremid,
                 scorehigh,
                 lowclimber,
                 midclimber,
                 highclimber,
                 hang,
                 trigger,
                 win,
                 createdate=time.strftime('%Y-%m-%d %H:%M:%S'),
                 moddate=time.strftime('%Y-%m-%d %H:%M:%S')):
        self.Scout = scout
        self.Team = team
        self.Competition = comp
        self.MatchNumber = match
        self.DidRobotMove = move
        self.DeliverClimbers = climbers
        self.PushBeacon = beacon
        self.ParkingLevel = park
        self.DidRobotScoreCycles = score
        self.HowManyCycles = cycles
        self.ScoreLowZone = scorelow
        self.ScoreMidZone = scoremid
        self.ScoreHighZone = scorehigh
        self.ReleaseLowClimber = lowclimber
        self.ReleaseMidClimber = midclimber
        self.ReleaseHighClimber = highclimber
        self.DidRobotHang = hang
        self.DidRobotTriggerClimbers = trigger
        self.DidRobotWin = win
        self.CreateDate = createdate
        self.LastModifiedDate = moddate

    def __repr__(self):
        return '<Match Scouting Report %r>' % self.id


class PitScouting(db.Model):
    __tablename__ = 'PitScouting'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Competition = db.Column(db.ForeignKey(u'Competitions.id'), nullable=False, index=True)
    Team = db.Column(db.ForeignKey(u'Teams.id'), nullable=False, index=True)
    Scout = db.Column(db.ForeignKey(u'Scouts.id'), nullable=False, index=True)
    #autonomous
    CanDoAutonomous = db.Column(db.Boolean, nullable=False)
    DefensiveAutonomous = db.Column(db.Boolean, nullable=False)
    a_CanDeliverClimbers = db.Column(db.Boolean, nullable=False)
    a_CanDeliverClimbers_accuracy = db.Column(db.Integer, nullable=False)
    CanPushBeacon = db.Column(db.Boolean, nullable=False)
    a_CanParkFloor = db.Column(db.Boolean, nullable=False)
    a_CanParkLow = db.Column(db.Boolean, nullable=False)
    a_CanParkMid = db.Column(db.Boolean, nullable=False)
    a_CanParkMid_accuracy = db.Column(db.Integer, nullable=False)
    a_CanParkHigh = db.Column(db.Boolean, nullable=False)
    a_CanParkHigh_accuracy = db.Column(db.Integer, nullable=False)
    #teleop
    DebrisScoringCycles = db.Column(db.Integer, nullable=False)
    CanScoreLow = db.Column(db.Boolean, nullable=False)
    CanScoreMid = db.Column(db.Boolean, nullable=False)
    CanScoreHigh = db.Column(db.Boolean, nullable=False)
    t_CanDeliverClimbers = db.Column(db.Boolean, nullable=False)
    t_CanDeliverClimbers_accuracy = db.Column(db.Integer, nullable=False)
    CanReleaseLowClimber = db.Column(db.Boolean, nullable=False)
    CanReleaseLowClimber_accuracy = db.Column(db.Integer, nullable=False)
    CanReleaseMidClimber = db.Column(db.Boolean, nullable=False)
    CanReleaseMidClimber_accuracy = db.Column(db.Integer, nullable=False)
    CanReleaseHighClimber = db.Column(db.Boolean, nullable=False)
    CanReleaseHighClimber_accuracy = db.Column(db.Integer, nullable=False)
    t_CanParkFloor = db.Column(db.Boolean, nullable=False)
    t_CanParkLow = db.Column(db.Boolean, nullable=False)
    t_CanParkMid = db.Column(db.Boolean, nullable=False)
    t_CanParkMid_accuracy = db.Column(db.Integer, nullable=False)
    t_CanParkHigh = db.Column(db.Boolean, nullable=False)
    t_CanParkHigh_accuracy = db.Column(db.Integer, nullable=False)
    #endgame
    CanHang = db.Column(db.Boolean, nullable=False)
    CanTriggerAllClear = db.Column(db.Boolean, nullable=False)
    #general
    Comments = db.Column(db.Text, nullable=False)
    AddToWatchList = db.Column(db.Boolean, nullable=False)
    #timestamps
    CreateDate = db.Column(db.DateTime, nullable=False)
    LastModifiedDate = db.Column(db.DateTime, nullable=False)
    #relational table info
    Team1 = db.relationship(u'Team')
    Competition1 = db.relationship(u'Competition')
    Scout1 = db.relationship(u'Scout')

    def __init__(self,
                 comp,
                 team,
                 scout,
                 auto_offense,
                 auto_defense,
                 a_climbers,
                 a_climbers_acc,
                 beacon,
                 a_floorpark,
                 a_lowpark,
                 a_midpark,
                 a_midpark_acc,
                 a_highpark,
                 a_highpark_acc,
                 cycles,
                 scorelow,
                 scoremid,
                 scorehigh,
                 t_climbers,
                 t_climbers_acc,
                 lowclimber,
                 lowclimber_acc,
                 midclimber,
                 midclimber_acc,
                 highclimber,
                 highclimber_acc,
                 t_floorpark,
                 t_lowpark,
                 t_midpark,
                 t_midpark_acc,
                 t_highpark,
                 t_highpark_acc,
                 hang,
                 allclear,
                 comments,
                 watchlist,
                 createdate=time.strftime('%Y-%m-%d %H:%M:%S'),
                 moddate=time.strftime('%Y-%m-%d %H:%M:%S')):
        self.Competition = comp
        self.Team = team
        self.Scout = scout
        self.CanDoAutonomous = auto_offense
        self.DefensiveAutonomous = auto_defense
        self.a_CanDeliverClimbers = a_climbers
        self.a_CanDeliverClimbers_accuracy = a_climbers_acc
        self.CanPushBeacon = beacon
        self.a_CanParkFloor = a_floorpark
        self.a_CanParkLow = a_lowpark
        self.a_CanParkMid = a_midpark
        self.a_CanParkMid_accuracy = a_midpark_acc
        self.a_CanParkHigh = a_highpark
        self.a_CanParkHigh_accuracy = a_highpark_acc
        self.DebrisScoringCycles = cycles
        self.CanScoreLow = scorelow
        self.CanScoreMid = scoremid
        self.CanScoreHigh = scorehigh
        self.t_CanDeliverClimbers = t_climbers
        self.t_CanDeliverClimbers_accuracy = t_climbers_acc
        self.CanReleaseLowClimber = lowclimber
        self.CanReleaseLowClimber_accuracy = lowclimber_acc
        self.CanReleaseMidClimber = midclimber
        self.CanReleaseMidClimber_accuracy = midclimber_acc
        self.CanReleaseHighClimber = highclimber
        self.CanReleaseHighClimber_accuracy = highclimber_acc
        self.t_CanParkFloor = t_floorpark
        self.t_CanParkLow = t_lowpark
        self.t_CanParkMid = t_midpark
        self.t_CanParkMid_accuracy = t_midpark_acc
        self.t_CanParkHigh = t_highpark
        self.t_CanParkHigh_accuracy = t_highpark_acc
        self.CanHang = hang
        self.CanTriggerAllClear = allclear
        self.Comments = comments
        self.AddToWatchList = watchlist
        self.CreateDate = createdate
        self.LastModifiedDate = moddate

    def __repr__(self):
        return '<Pit Scouting Report %r>' % self.id


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