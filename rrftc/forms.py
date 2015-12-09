from flask_wtf import Form
from wtforms import StringField, SubmitField, PasswordField, IntegerField, validators, DateField, HiddenField, TextAreaField, SelectField, BooleanField
from wtforms_sqlalchemy.fields import QuerySelectField

from models import Team, Scout, Competition
'''
from models import Team, Scout, Competition

def active_competitions():
    return Competition.query.all()

def active_scouts():
    return Scout.query.all()

def active_teams():
    return Team.query.all()
'''

class ScoutingForm(Form):
    competition = QuerySelectField(query_factory=lambda: Competition.query.all(), get_label='Name')
    team = QuerySelectField(query_factory=lambda: Team.query.all(), get_label='Number')
    scout = QuerySelectField(query_factory=lambda: Scout.query.all(), get_label='Name')
    rweight = IntegerField('Robot Weight', [validators.DataRequired('What is the robot\'s Weight?')], default=0)
    rheight = IntegerField('Robot Height', [validators.DataRequired('What is the robot\'s Height?')], default=0)
    auto = BooleanField('Autonomous?', default=False)
    beacon = BooleanField('Push Beacon?', default=False)
    aclimbers = BooleanField('Deliver Climbers?', default=False)
    lclimber = BooleanField('Rescue Low Climber?', default=False)
    mclimber = BooleanField('Rescue Mid Climber?', default=False)
    hclimber = BooleanField('Rescue High Climber?', default=False)
    fpark = BooleanField('Park on Floor?', default=False)
    lpark = BooleanField('Park on Low Zone?', default=False)
    mpark = BooleanField('Park on Mid Zone?', default=False)
    hpark = BooleanField('Park on High Zone?', default=False)
    climbheight = SelectField('Highest Zone Climbed', choices=[('Floor', 'Floor'),
                                                               ('Low Zone', 'Low Zone'),
                                                               ('Mid Zone', 'Mid Zone'),
                                                               ('High Zone', 'High Zone')])
    debris = BooleanField('Can Score Debris?', default=False)
    ldebrisscore = BooleanField('Can Score Debris in Low Zone?', default=False)
    mdebrisscore = BooleanField('Can Score Debris in Mid Zone?', default=False)
    hdebrisscore = BooleanField('Can Score Debris in High Zone?', default=False)
    avgdebris = IntegerField('Average Debris Score?', [validators.DataRequired('How much debris is scored on average?')], default=0)
    debrisscoringmethod = SelectField('How is Debris Handled?', choices=[('Climb', 'Climb'),
                                                                         ('Launch', 'Launch'),
                                                                         ('Extend', 'Extend'),
                                                                         ('Other', 'Other')])
    hang = BooleanField('Can the robot hang?', default=False)
    allclear = BooleanField('Trigger All Clear?', default=False)
    pof = TextAreaField('Points of Failure', [validators.DataRequired'Please enter possible points of failure:'], default='points of failure:')
    comments = TextAreaField('Comments', [validators.DataRequired('Please enter comments:')], default='general comments:')

    submit = SubmitField('Add Report')

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

        if self.username.data.lower() == 'admin' and self.password.data == 'roboraiders':
            return True
        else:
            self.username.errors.append('Invalid username or password')
            return False


class CompetitionForm(Form):
    name = StringField('Name', [validators.DataRequired('Please enter the competition name.')])
    date = DateField('Date', [validators.DataRequired('Please enter the competition date.')])
    location = StringField('Location', [validators.DataRequired('Please enter the competition location.')])
    submit = SubmitField('Add Competition')

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if not Form.validate(self):
            return False
        else:
            return True

class MatchForm(Form):
    competition = HiddenField ('Competition')
    match = HiddenField('Match')
    blueteam1 = QuerySelectField(query_factory=lambda: Team.query.all(), get_label='Number')
    blueteam2 = QuerySelectField(query_factory=lambda: Team.query.all(), get_label='Number')
    redteam1 = QuerySelectField(query_factory=lambda: Team.query.all(), get_label='Number')
    redteam2 = QuerySelectField(query_factory=lambda: Team.query.all(), get_label='Number')
    submit = SubmitField('Add Team')

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
        else:
            return True