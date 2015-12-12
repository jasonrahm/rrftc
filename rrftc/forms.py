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
    rweight = IntegerField('Robot\'s Weight?', [validators.DataRequired('What is the robot\'s Weight?')], default=0)
    rheight = IntegerField('Robot\'s Height?', [validators.DataRequired('What is the robot\'s Height?')], default=0)
    auto = BooleanField('Is autonomous working?', default=False)
    beacon = BooleanField('Can it push the beacon?', default=False)
    aclimbers = BooleanField('Can it deliver climbers?', default=False)
    lclimber = BooleanField('Can it release the low climber?', default=False)
    mclimber = BooleanField('Can it release the mid climber?', default=False)
    hclimber = BooleanField('Can it release the high climber?', default=False)
    fpark = BooleanField('Can it park on the floor?', default=False)
    lpark = BooleanField('Can it park on the low zone?', default=False)
    mpark = BooleanField('Can it park on the mid zone?', default=False)
    hpark = BooleanField('Can it park on the high zone?', default=False)
    climbheight = SelectField('Highest zone climbed?', choices=[('Floor', 'Floor'),
                                                               ('Low Zone', 'Low Zone'),
                                                               ('Mid Zone', 'Mid Zone'),
                                                               ('High Zone', 'High Zone')])
    debris = BooleanField('Can it score debris?', default=False)
    ldebrisscore = BooleanField('Can it score debris in low zone?', default=False)
    mdebrisscore = BooleanField('Can it score debris in mid zone?', default=False)
    hdebrisscore = BooleanField('Can it score debris in high zone?', default=False)
    avgdebris = IntegerField('What is the average debris scored?', [validators.DataRequired('How much debris is scored on average?')], default=0)
    debrisscoringmethod = SelectField('How is debris handled?', choices=[('Climb', 'Climb'),
                                                                         ('Launch', 'Launch'),
                                                                         ('Extend', 'Extend'),
                                                                         ('Other', 'Other (add details in comments)')])
    hang = BooleanField('Can it hang?', default=False)
    allclear = BooleanField('Can it trigger the all clear?', default=False)
    spof = TextAreaField('What are the perceived points of failure?', [validators.DataRequired('Please enter possible points of failure:')], default='points of failure:')
    comments = TextAreaField('General Comments', [validators.DataRequired('Please enter comments:')], default='general comments:')
    watchlist = BooleanField('Add this team to the watch list?', default=False)

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