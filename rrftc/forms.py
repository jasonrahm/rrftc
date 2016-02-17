from flask_wtf import Form
from wtforms import StringField, SubmitField, PasswordField, IntegerField, validators, DateField, HiddenField, \
    TextAreaField, SelectField, BooleanField
from wtforms_sqlalchemy.fields import QuerySelectField

from models import Team, Scout, Competition


class MatchScoutingForm(Form):
    competition = QuerySelectField(query_factory=lambda: Competition.query.all(), get_label='Name')
    team = QuerySelectField(query_factory=lambda: Team.query.all(), get_label='Number')
    scout = QuerySelectField(query_factory=lambda: Scout.query.all(), get_label='Name')
    move = BooleanField('Did the robot move?', default=False)
    win = BooleanField('Did the robot win?', default=False)
    score = BooleanField('Did the robot score?', default=False)
    cycles = SelectField('How many scoring cycles?', choices=[(-1, '0'),
                                                               (1, '1'),
                                                               (2, '2'),
                                                               (3, '3'),
                                                               (4, '4'),
                                                               (5, '5')
                                                               (6, '6')], coerce=int)
    hang = BooleanField('Did the robot hang?', default=False)
    trigger = BooleanField('Did the robot trigger the climbers?', default=False)

    submit = SubmitField('Add Report')

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if not Form.validate(self):
            return False
        else:
            return True


class ScoutingForm(Form):
    competition = QuerySelectField(query_factory=lambda: Competition.query.all(), get_label='Name')
    team = QuerySelectField(query_factory=lambda: Team.query.all(), get_label='Number')
    scout = QuerySelectField(query_factory=lambda: Scout.query.all(), get_label='Name')
    auto = BooleanField('Can it do autonomous?', default=False)
    beacon = BooleanField('Can it push the beacon?', default=False)
    aclimbers = BooleanField('Can it deliver climbers?', default=False)
    lclimber = BooleanField('Can it release the low climber?', default=False)
    mclimber = BooleanField('Can it release the middle climber?', default=False)
    hclimber = BooleanField('Can it release the high climber?', default=False)
    fpark = BooleanField('Can it park on the floor?', default=False)
    lpark = BooleanField('Can it park on the low zone?', default=False)
    mpark = BooleanField('Can it park on the middle zone?', default=False)
    hpark = BooleanField('Can it park on the high zone?', default=False)
    climbheight = SelectField('What is the highest zone climbed?', choices=[('Floor', 'Floor'),
                                                               ('Low Zone', 'Low Zone'),
                                                               ('Mid Zone', 'Mid Zone'),
                                                               ('High Zone', 'High Zone')])
    debris = BooleanField('Can it score debris?', default=False)
    ldebrisscore = BooleanField('Can it score debris in low zone?', default=False)
    mdebrisscore = BooleanField('Can it score debris in middle zone?', default=False)
    hdebrisscore = BooleanField('Can it score debris in high zone?', default=False)
    avgdebris = SelectField('How many scoring cycles can it do?', choices=[(1,'1'),
                                                                            (2,'2'),
                                                                            (3,'3'),
                                                                            (4,'4'),
                                                                            (5,'5')], coerce=int)
    debrisscoringmethod = SelectField('How is debris handled?', choices=[('None', 'None'),
                                                                         ('Push', 'Push'),
                                                                         ('Climb', 'Climb'),
                                                                         ('Launch', 'Launch'),
                                                                         ('Extend', 'Extend'),
                                                                         ('Other', 'Other (add details in comments)')])
    hang = BooleanField('Can it hang?', default=False)
    allclear = BooleanField('Can it trigger the all clear?', default=False)
    spof = TextAreaField('What are the perceived points of failure?', [validators.DataRequired('Please enter possible points of failure:')], default='points of failure:')
    comments = TextAreaField('General Comments', [validators.DataRequired('Please enter comments:')], default='Parking Accuracy:\nBeacon Accuracy:\nDelivery Accuracy:\nZipline Accuracy:\nHang Accuracy:\nAll Clear Accuracy:\n\nGeneral Comments:')
    watchlist = BooleanField('Add this team to the watch list?', default=False)

    submit = SubmitField('Add Report')

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if not Form.validate(self):
            return False
        else:
            return True


class MatchReportingForm(Form):
    competition = QuerySelectField(query_factory=lambda: Competition.query.all(), get_label='Name')
    move = SelectField('Did the robot move?', choices=[(1,'1'),(3,'3'),(9,'9')], coerce=int)
    win = SelectField('Did the robot win?', choices=[(1,'1'),(3,'3'),(9,'9')], coerce=int)
    score = SelectField('Did the robot score?', choices=[(1,'1'),(3,'3'),(9,'9')], coerce=int)
    cycles = SelectField('How many scoring cycles?', choices=[(1,'1'),(3,'3'),(9,'9')], coerce=int)
    hang = SelectField('Did the robot hang?', choices=[(1,'1'),(3,'3'),(9,'9')], coerce=int)
    trigger = SelectField('Did the robot trigger the climbers?', choices=[(1,'1'),(3,'3'),(9,'9')], coerce=int)

    submit = SubmitField('Get Report')

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if not Form.validate(self):
            return False
        else:
            return True


class ReportingForm(Form):
    competition = QuerySelectField(query_factory=lambda: Competition.query.all(), get_label='Name')
    auto = SelectField('Can it do autonomous?', choices=[(1,'1'),(3,'3'),(9,'9')], coerce=int)
    beacon = SelectField('Can it push the beacon?', choices=[(1,'1'),(3,'3'),(9,'9')], coerce=int)
    aclimbers = SelectField('Can it deliver climbers?', choices=[(1,'1'),(3,'3'),(9,'9')], coerce=int)
    lclimber = SelectField('Can it release the low climber?', choices=[(1,'1'),(3,'3'),(9,'9')], coerce=int)
    mclimber = SelectField('Can it release the middle climber?', choices=[(1,'1'),(3,'3'),(9,'9')], coerce=int)
    hclimber = SelectField('Can it release the high climber?', choices=[(1,'1'),(3,'3'),(9,'9')], coerce=int)
    fpark = SelectField('Can it park on the floor?', choices=[(1,'1'),(3,'3'),(9,'9')], coerce=int)
    lpark = SelectField('Can it park on the low zone?', choices=[(1,'1'),(3,'3'),(9,'9')], coerce=int)
    mpark = SelectField('Can it park on the middle zone?', choices=[(1,'1'),(3,'3'),(9,'9')], coerce=int)
    hpark = SelectField('Can it park on the high zone?', choices=[(1,'1'),(3,'3'),(9,'9')], coerce=int)
    debris = SelectField('Can it score debris?', choices=[(1,'1'),(3,'3'),(9,'9')], coerce=int)
    ldebrisscore = SelectField('Can it score in the low zone?', choices=[(1,'1'),(3,'3'),(9,'9')], coerce=int)
    mdebrisscore = SelectField('Can it score in the middle zone?', choices=[(1,'1'),(3,'3'),(9,'9')], coerce=int)
    hdebrisscore = SelectField('Can it score in the high zone?', choices=[(1,'1'),(3,'3'),(9,'9')], coerce=int)
    avgdebris = SelectField('What is the average debris score?', choices=[(1,'1'),(3,'3'),(9,'9')], coerce=int)
    hang = SelectField('Can it hang?', choices=[(1,'1'),(3,'3'),(9,'9')], coerce=int)
    allclear = SelectField('Can it trigger the all clear?', choices=[(1,'1'),(3,'3'),(9,'9')], coerce=int)

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
        else:
            return True