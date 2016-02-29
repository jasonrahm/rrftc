from flask_wtf import Form
from wtforms import StringField, SubmitField, PasswordField, IntegerField, validators, DateField, HiddenField, \
    TextAreaField, SelectField, BooleanField
from wtforms_sqlalchemy.fields import QuerySelectField

from models import Team, Scout, Competition, CompetitionTeam


class MatchScoutingForm(Form):
    competition = QuerySelectField(query_factory=lambda: Competition.query.all(), get_label='Name')
    team = QuerySelectField(query_factory=lambda: Team.query.all(), get_label='Number')
    scout = QuerySelectField(query_factory=lambda: Scout.query.all(), get_label='Name')
    match = IntegerField('Match Number?', [validators.DataRequired('Please enter the match number')], default=1)
    move = BooleanField('Did the robot move?', default=False)
    a_climbers = BooleanField('Deliver climbers?', default=False)
    beacon = BooleanField('Push Beacon?', default=False)
    a_park = SelectField('Highest Parking Level?', choices=[(0, 'Can\'t Park'),
                                                          (1, 'Floor/Partial Low'),
                                                          (2, 'Low Zone'),
                                                          (3, 'Mid Zone'),
                                                          (4, 'High Zone')], coerce=int)
    t_climbers = BooleanField('Deliver climbers?', default=False)
    score = BooleanField('Did the robot score?', default=False)
    cycles = SelectField('How many scoring cycles?', choices=[(0, '0'),
                                                               (1, '1'),
                                                               (2, '2'),
                                                               (3, '3'),
                                                               (4, '4'),
                                                               (5, '5'),
                                                               (6, '6')], coerce=int)
    scorelow = BooleanField('Score in low zone?', default=False)
    scoremid = BooleanField('Score in mid zone?', default=False)
    scorehigh = BooleanField('Score in high zone?', default=False)
    lowclimber = BooleanField('Release low climber?', default=False)
    midclimber = BooleanField('Release mid climber?', default=False)
    highclimber = BooleanField('Release high climber?', default=False)
    t_park = SelectField('Highest Parking Level?', choices=[(0, 'Can\'t Park'),
                                                            (1, 'Floor/Partial Low'),
                                                            (2, 'Low Zone'),
                                                            (3, 'Mid Zone'),
                                                            (4, 'High Zone')], coerce=int)
    hang = BooleanField('Did the robot hang?', default=False)
    allclear = BooleanField('Did the robot trigger the all clear?', default=False)
    comments = TextAreaField('General Comments')

    submit = SubmitField('Add Report')

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if not Form.validate(self):
            return False
        else:
            return True


class PitScoutingForm(Form):
    competition = QuerySelectField(query_factory=lambda: Competition.query.all(), get_label='Name')
    team = QuerySelectField(query_factory=lambda: Team.query.all(), get_label='Number')
    scout = QuerySelectField(query_factory=lambda: Scout.query.all(), get_label='Name')
    auto_offense = BooleanField('Autonomous?', default=False)
    auto_defense = BooleanField('Defensive Autonomous?', default=False)
    a_climbers = BooleanField('Deliver Climbers?', default=False)
    a_climbers_acc = SelectField('Climber Accuracy', choices=[(0, '0%'),
                                                              (1, '1% - 25%'),
                                                              (2, '26% - 50%'),
                                                              (3, '51% - 75%'),
                                                              (4, '76% - 100%')], coerce=int)
    beacon = BooleanField('Push Beacon?', default=False)
    a_floorpark = BooleanField('Park on Floor?', default=False)
    a_lowpark = BooleanField('Park on Low Zone?', default=False)
    a_midpark = BooleanField('Park on Mid Zone?', default=False)
    a_midpark_acc = SelectField('Mid Park Accuracy', choices=[(0, '0%'),
                                                              (1, '1% - 25%'),
                                                              (2, '26% - 50%'),
                                                              (3, '51% - 75%'),
                                                              (4, '76% - 100%')], coerce=int)
    a_highpark = BooleanField('Park on High Zone?', default=False)
    a_highpark_acc = SelectField('High Park Accuracy', choices=[(0, '0%'),
                                                              (1, '1% - 25%'),
                                                              (2, '26% - 50%'),
                                                              (3, '51% - 75%'),
                                                              (4, '76% - 100%')], coerce=int)
    cycles = SelectField('Debris Scoring Cycles', choices=[(0,'0'),
                                                           (1,'1'),
                                                           (2,'2'),
                                                           (3,'3'),
                                                           (4,'4'),
                                                           (5,'5'),
                                                           (6,'6')], coerce=int)
    scorelow = BooleanField('Score in Low Zone?', default=False)
    scoremid = BooleanField('Score in Mid Zone?', default=False)
    scorehigh = BooleanField('Score in High Zone?', default=False)
    t_climbers = BooleanField('Deliver Climbers?', default=False)
    t_climbers_acc = SelectField('Climber Accuracy', choices=[(0, '0%'),
                                                              (1, '1% - 25%'),
                                                              (2, '26% - 50%'),
                                                              (3, '51% - 75%'),
                                                              (4, '76% - 100%')], coerce=int)
    lowclimber = BooleanField('Release Low Climber?', default=False)
    lowclimber_acc = SelectField('Low Climber Accuracy', choices=[(0, '0%'),
                                                              (1, '1% - 25%'),
                                                              (2, '26% - 50%'),
                                                              (3, '51% - 75%'),
                                                              (4, '76% - 100%')], coerce=int)
    midclimber = BooleanField('Release Mid Climber?', default=False)
    midclimber_acc = SelectField('Mid Climber Accuracy', choices=[(0, '0%'),
                                                              (1, '1% - 25%'),
                                                              (2, '26% - 50%'),
                                                              (3, '51% - 75%'),
                                                              (4, '76% - 100%')], coerce=int)
    highclimber = BooleanField('Release High Climber?', default=False)
    highclimber_acc = SelectField('High Climber Accuracy', choices=[(0, '0%'),
                                                              (1, '1% - 25%'),
                                                              (2, '26% - 50%'),
                                                              (3, '51% - 75%'),
                                                              (4, '76% - 100%')], coerce=int)
    t_floorpark = BooleanField('Park on Floor?', default=False)
    t_lowpark = BooleanField('Park on Low Zone?', default=False)
    t_midpark = BooleanField('Park on Mid Zone?', default=False)
    t_midpark_acc = SelectField('Mid Park Accuracy', choices=[(0, '0%'),
                                                              (1, '1% - 25%'),
                                                              (2, '26% - 50%'),
                                                              (3, '51% - 75%'),
                                                              (4, '76% - 100%')], coerce=int)
    t_highpark = BooleanField('Park on High Zone?', default=False)
    t_highpark_acc = SelectField('High Park Accuracy', choices=[(0, '0%'),
                                                              (1, '1% - 25%'),
                                                              (2, '26% - 50%'),
                                                              (3, '51% - 75%'),
                                                              (4, '76% - 100%')], coerce=int)
    hang = BooleanField('Can it Hang?', default=False)
    allclear = BooleanField('Trigger All Clear?', default=False)
    comments = TextAreaField('General Comments')
    watchlist = BooleanField('Add to Watch List?', default=False)

    submit = SubmitField('Add Pit Scouting Report')

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if not Form.validate(self):
            return False
        else:
            return True


class MatchReportingForm(Form):
    competition = QuerySelectField(query_factory=lambda: Competition.query.all(), get_label='Name')
    move = SelectField('Did the robot move?', choices=[(0,'Ignore'),(1,'Not Important'),(3,'Important'),(9,'Critical')], coerce=int)
    a_climbers = SelectField('Deliver climbers?', choices=[(1,'1'),(3,'3'),(9,'9')], coerce=int)
    beacon = SelectField('Push beacon?', choices=[(1,'1'),(3,'3'),(9,'9')], coerce=int)
    a_park = SelectField('Highest parking level?', choices=[(1,'1'),(3,'3'),(9,'9')], coerce=int)
    t_climbers = SelectField('Deliver climbers?', choices=[(1,'1'),(3,'3'),(9,'9')], coerce=int)
    score = SelectField('Did the robot score?', choices=[(1,'1'),(3,'3'),(9,'9')], coerce=int)
    cycles = SelectField('How many scoring cycles?', choices=[(1,'1'),(3,'3'),(9,'9')], coerce=int)
    scorelow = SelectField('Score in the low zone?', choices=[(1,'1'),(3,'3'),(9,'9')], coerce=int)
    scoremid = SelectField('Score in the mid zone?', choices=[(1,'1'),(3,'3'),(9,'9')], coerce=int)
    scorehigh = SelectField('Score in the high zone?', choices=[(1,'1'),(3,'3'),(9,'9')], coerce=int)
    lowclimber = SelectField('Release low climber?', choices=[(1,'1'),(3,'3'),(9,'9')], coerce=int)
    midclimber = SelectField('Release mid climber?', choices=[(1,'1'),(3,'3'),(9,'9')], coerce=int)
    highclimber = SelectField('Release high climber?', choices=[(1,'1'),(3,'3'),(9,'9')], coerce=int)
    t_park = SelectField('Highest parking level?', choices=[(1,'1'),(3,'3'),(9,'9')], coerce=int)
    hang = SelectField('Did the robot hang?', choices=[(1,'1'),(3,'3'),(9,'9')], coerce=int)
    allclear = SelectField('Did the robot trigger the all clear?', choices=[(1,'1'),(3,'3'),(9,'9')], coerce=int)

    submit = SubmitField('Get Report')

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if not Form.validate(self):
            return False
        else:
            return True


class PitReportingForm(Form):
    competition = QuerySelectField(query_factory=lambda: Competition.query.all(), get_label='Name')
    auto_offense = SelectField('Autonomous?', choices=[(1,'1'),(3,'3'),(9,'9')], coerce=int)
    auto_defense = SelectField('Defensive Autonomous?', choices=[(1,'1'),(3,'3'),(9,'9')], coerce=int)
    a_climbers = SelectField('Deliver Climbers?', choices=[(1,'1'),(3,'3'),(9,'9')], coerce=int)
    beacon = SelectField('Push Beacon?', choices=[(1,'1'),(3,'3'),(9,'9')], coerce=int)
    a_floorpark = SelectField('Park on Floor?', choices=[(1,'1'),(3,'3'),(9,'9')], coerce=int)
    a_lowpark = SelectField('Park on Low Zone?', choices=[(1,'1'),(3,'3'),(9,'9')], coerce=int)
    a_midpark = SelectField('Park on Mid Zone?', choices=[(1,'1'),(3,'3'),(9,'9')], coerce=int)
    a_highpark = SelectField('Park on High Zone?', choices=[(1,'1'),(3,'3'),(9,'9')], coerce=int)
    cycles = SelectField('Debris Scoring Cycles', choices=[(1,'1'),(3,'3'),(9,'9')], coerce=int)
    scorelow = SelectField('Score in Low Zone?', choices=[(1,'1'),(3,'3'),(9,'9')], coerce=int)
    scoremid = SelectField('Score in Mid Zone?', choices=[(1,'1'),(3,'3'),(9,'9')], coerce=int)
    scorehigh = SelectField('Score in High Zone?', choices=[(1,'1'),(3,'3'),(9,'9')], coerce=int)
    t_climbers = SelectField('Deliver Climbers?', choices=[(1,'1'),(3,'3'),(9,'9')], coerce=int)
    lowclimber = SelectField('Release Low Climber', choices=[(1,'1'),(3,'3'),(9,'9')], coerce=int)
    midclimber = SelectField('Release Mid Climber?', choices=[(1,'1'),(3,'3'),(9,'9')], coerce=int)
    highclimber = SelectField('Release High Climber?', choices=[(1,'1'),(3,'3'),(9,'9')], coerce=int)
    t_floorpark = SelectField('Park on Floor?', choices=[(1,'1'),(3,'3'),(9,'9')], coerce=int)
    t_lowpark = SelectField('Park on Low Zone?', choices=[(1,'1'),(3,'3'),(9,'9')], coerce=int)
    t_midpark = SelectField('Park on Mid Zone?', choices=[(1,'1'),(3,'3'),(9,'9')], coerce=int)
    t_highpark = SelectField('Park on High Zone?', choices=[(1,'1'),(3,'3'),(9,'9')], coerce=int)
    hang = SelectField('Can it Hang?', choices=[(1,'1'),(3,'3'),(9,'9')], coerce=int)
    allclear = SelectField('Trigger All Clear?', choices=[(1,'1'),(3,'3'),(9,'9')], coerce=int)

    submit = SubmitField('Get Report')

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if not Form.validate(self):
            return False
        else:
            return True


class CompetitionTeamForm(Form):
    competition = HiddenField('Competition')
    team = QuerySelectField(query_factory=lambda: Team.query.all(), get_label='Number')
    submit = SubmitField('Add Team')

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if not Form.validate(self):
            return False

        checkteam = CompetitionTeam.query.filter_by(Teams=self.team.data.id).first()
        if checkteam:
            self.team.errors.append("Team is already part of this competition")
            return False
        else:
            return True


class SigninForm(Form):
    username = StringField('Username', [validators.DataRequired('Please enter your username.')])
    password = PasswordField('Password', [validators.DataRequired('Please enter your password.')])
    submit = SubmitField('Sign In')

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if not Form.validate(self):
            return False

        if self.username.data.lower() == 'admin' and self.password.data == 'admin':
            return True
        else:
            self.username.errors.append('Invalid username or password')
            return False


class CompetitionForm(Form):
    name = StringField('Name', [validators.DataRequired('Please enter the competition name.')])
    date = DateField('Date', [validators.DataRequired('Please enter the competition date.')], format='%Y-%m-%d')
    location = StringField('Location', [validators.DataRequired('Please enter the competition location.')])
    submit = SubmitField('Add Competition')

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if not Form.validate(self):
            return False
        else:
            return True


class ScoutForm(Form):
    name = StringField('Name', [validators.DataRequired('Please enter the scout\'s name.')])
    submit = SubmitField('Add Scout')

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if not Form.validate(self):
            return False
        else:
            return True


class TeamForm(Form):
    number = IntegerField('Number', [validators.DataRequired('Please enter the team number.')])
    name = StringField('Name', [validators.DataRequired('Please enter the team name.')])
    website = StringField('Website', [validators.DataRequired('Please enter the team website')], default='http://')
    submit = SubmitField('Add Team')

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if not Form.validate(self):
            return False

        checkteam = Team.query.filter_by(Number=self.number.data).first()
        if checkteam:
            self.number.errors.append("Team is already in the system.")
            return False
        else:
            return True