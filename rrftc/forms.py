from flask_wtf import Form
from wtforms import StringField, SubmitField, PasswordField, IntegerField, validators, DateField, HiddenField, TextAreaField
from wtforms_sqlalchemy.fields import QuerySelectField

from models import Team
'''
from models import Team, Scout, Competition

def active_competitions():
    return Competition.query.all()

def active_scouts():
    return Scout.query.all()

def active_teams():
    return Team.query.all()
'''

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
    website = StringField('Website', [validators.DataRequired('Please enter the team website')])
    submit = SubmitField('Add Team')

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if not Form.validate(self):
            return False
        else:
            return True