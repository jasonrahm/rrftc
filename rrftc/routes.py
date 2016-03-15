from rrftc import app
from flask import render_template, request, flash, session, url_for, redirect
from forms import SigninForm, CompetitionForm, TeamForm, CompetitionTeamForm, \
    PitScoutingForm, PitReportingForm, MatchScoutingForm, MatchReportingForm, AddUserForm
from models import db, Competition, Team, CompetitionTeam, PitScouting, MatchScouting, Users
import datetime
import sqlite3


def rollup(a, b, c, d=None):
    if d is not None:
        c = True if d is True else c
        b = True if c is True else b
        a = True if b is True else a
        return a, b, c, d
    else:
        b = True if c is True else b
        a = True if b is True else a
        return a, b, c


@app.route('/')
def home():
    return render_template('home.html')


@app.errorhandler(500)
def internal_error(error):
    return render_template('servererror.html')


@app.errorhandler(404)
def missing_file(error):
    return render_template('servererror.html')


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    form = SigninForm()

    if 'username' in session:
        return redirect(url_for('home'))

    if request.method == 'POST':
        if not form.validate():
            return render_template('signin.html', form=form)
        else:
            session['username'] = form.username.data
            flash('Login Successful.')
            return redirect(url_for('home'))

    elif request.method == 'GET':
        return render_template('signin.html', form=form)


@app.route('/signout')
def signout():

    if 'username' not in session:
        redirect(url_for('signin'))

    session.pop('username', None)
    session.pop('pitreport', None)
    session.pop('matchreport', None)
    session.pop('matchrank', None)

    flash('You have been logged out.')
    return redirect(url_for('home'))


@app.route('/teams', methods=['GET', 'POST'])
def teams():

    form = TeamForm()

    if 'username' not in session:
        return redirect(url_for('signin'))

    user = session['username']

    teams = db.session.query(Team).order_by(Team.Number).all()

    if user is None:
        redirect(url_for('signin'))
    else:
        if request.method == 'POST':
            if not form.validate():
                return render_template('teams.html', teams=teams, form=form)
            else:
                newteam = Team(number=form.number.data, name=form.name.data, website=form.website.data, timestamp=datetime.datetime.now())
                db.session.add(newteam)
                db.session.commit()

                flash('Team successfully added.')
                return redirect(url_for('teams'))

        elif request.method == 'GET' :
            return render_template('teams.html', teams=teams, form=form)


@app.route('/teams/<int:id>', methods=['GET'])
def team(id):
    if 'username' not in session:
        return redirect(url_for('signin'))

    user = session['username']
    if user is None:
        redirect(url_for('signin'))
    else:
        team = db.session.query(Team).filter(Team.id == id).all()
        pitreports = db.session.query(PitScouting).filter(PitScouting.Team == id).all()
        matchreports = db.session.query(MatchScouting).filter(MatchScouting.Team == id).all()

        return render_template('team.html', id=id, pitreports=pitreports, team=team, matchreports=matchreports)


@app.route('/pit-reporting', methods=['GET', 'POST'])
def pit_reporting():

    form = PitReportingForm(request.values)
    form.competition.choices = [(a.id, a.Name) for a in Competition.query.order_by('Name')]

    if 'username' not in session:
        return redirect(url_for('signin'))

    user = session['username']
    if user is None:
        redirect(url_for('signin'))
    else:
        if request.method == 'POST':
            if not form.validate():
                return render_template('pitreporting.html', form=form)
            else:
                postdata = request.values
                sql_text = '''select PitScouting.id, Teams.Name, Teams.Number, Users.username,
                              (CanDoAutonomous*%d) +
                              (DefensiveAutonomous*%d) +
                              (a_CanDeliverClimbers*%d) +
                              (a_CanDeliverClimbers_accuracy*%d) +
                              (CanPushBeacon*%d) +
                              (a_CanParkFloor*%d) +
                              (a_CanParkLow*%d) +
                              (a_CanParkMid*%d) +
                              (a_CanParkMid_accuracy*%d) +
                              (a_CanParkHigh*%d) +
                              (a_CanParkHigh_accuracy*%d) +
                              (DebrisScoringCycles*%d) +
                              (CanScoreLow*%d) +
                              (CanScoreMid*%d) +
                              (CanScoreHigh*%d) +
                              (t_CanDeliverClimbers*%d) +
                              (t_CanDeliverClimbers_accuracy*%d) +
                              (CanReleaseLowClimber*%d) +
                              (CanReleaseLowClimber_accuracy*%d) +
                              (CanReleaseMidClimber*%d) +
                              (CanReleaseMidClimber_accuracy*%d) +
                              (CanReleaseHighClimber*%d) +
                              (CanReleaseHighClimber_accuracy*%d) +
                              (t_CanParkFloor*%d) +
                              (t_CanParkLow*%d) +
                              (t_CanParkMid*%d) +
                              (t_CanParkMid_accuracy*%d) +
                              (t_CanParkHigh*%d) +
                              (t_CanParkHigh_accuracy*%d) +
                              (CanHang*%d) +
                              (CanTriggerAllClear*%d)
                              AS Score
                              FROM PitScouting
                              INNER JOIN Teams
                                On PitScouting.Team = Teams.id
                              INNER JOIN Users
                                On PitScouting.Scout = Users.id
                              WHERE Competition = %d
                              ORDER BY Score
                              DESC''' % (int(postdata['auto_offense']),
                                         int(postdata['auto_defense']),
                                         int(postdata['a_climbers']),
                                         int(postdata['a_climbers']),
                                         int(postdata['beacon']),
                                         int(postdata['a_floorpark']),
                                         int(postdata['a_lowpark']),
                                         int(postdata['a_midpark']),
                                         int(postdata['a_midpark']),
                                         int(postdata['a_highpark']),
                                         int(postdata['a_highpark']),
                                         int(postdata['cycles']),
                                         int(postdata['scorelow']),
                                         int(postdata['scoremid']),
                                         int(postdata['scorehigh']),
                                         int(postdata['t_climbers']),
                                         int(postdata['t_climbers']),
                                         int(postdata['lowclimber']),
                                         int(postdata['lowclimber']),
                                         int(postdata['midclimber']),
                                         int(postdata['midclimber']),
                                         int(postdata['highclimber']),
                                         int(postdata['highclimber']),
                                         int(postdata['t_floorpark']),
                                         int(postdata['t_lowpark']),
                                         int(postdata['t_midpark']),
                                         int(postdata['t_midpark']),
                                         int(postdata['t_highpark']),
                                         int(postdata['t_highpark']),
                                         int(postdata['hang']),
                                         int(postdata['allclear']),
                                         int(postdata['competition']))

                result =db.engine.execute(sql_text)
                teams = []
                for row in result:
                    teams.append([row[0], row[1], row[2], row[3], row[4]])


                session['pitreport'] = teams

                sql_text1 = '''select PitScouting.id, Teams.Name, Teams.Number, Users.username
                              FROM PitScouting
                              INNER JOIN Teams
                                  On PitScouting.Team = Teams.id
                              INNER JOIN Users
                                  On PitScouting.Scout = Users.id
                              WHERE (Competition = %d AND AddToWatchList = 1)''' % int(postdata['competition'])

                result1 = db.engine.execute(sql_text1)
                teams1 = []
                for row in result1:
                    teams1.append([row[0], row[1], row[2], row[3]])
                session['watchlist'] = teams1

                return redirect(url_for('pit_report'))

        elif request.method == 'GET':
            return render_template('pitreporting.html', form=form)


@app.route('/pit-report')
def pit_report():
    if 'username' not in session:
        return redirect(url_for('signin'))

    user = session['username']

    if user is None:
        redirect(url_for('signin'))
    else:
        data = session['pitreport']
        if data == '':
            redirect(url_for('pit_reporting'))
        else:
            watchlist = session['watchlist']
            return render_template('pitreport.html', data=data, watchlist=watchlist)


@app.route('/pit-report/<int:id>',)
def get_individual_pitreport(id):
    data = PitScouting.query.get(id)
    return render_template('pitreport_details.html', data=data)


@app.route('/teams/delete/<int:id>',)
def delete_team_entry(id):
    team = Team.query.get(id)
    db.session.delete(team)
    db.session.commit()

    flash('Team deleted.')
    return redirect(url_for('teams'))


@app.route('/competitions', methods=['GET', 'POST'])
def competitions():

    form = CompetitionForm()

    if 'username' not in session:
        return redirect(url_for('signin'))

    user = session['username']

    if user is None:
        redirect(url_for('signin'))
    else:
        if request.method == 'POST':
            if form.validate() == False:
                return render_template('competitions.html', form=form)
            else:
                newcomp = Competition(name=form.name.data, date=form.date.data, location=form.location.data, timestamp=datetime.datetime.now())
                db.session.add(newcomp)
                db.session.commit()

                flash('Competition successfully added.')
                return redirect(url_for('competitions'))

        elif request.method == 'GET' :
            competitions = db.session.query(Competition).all()
            return render_template('competitions.html', competitions=competitions, form=form)


@app.route('/competitions/delete/<int:id>',)
def delete_competition_entry(id):

    user = session['username']
    if user is None:
        redirect(url_for('signin'))
    else:
        competition = Competition.query.get(id)
        db.session.delete(competition)
        db.session.commit()

        flash('Competition deleted.')
        return redirect(url_for('competitions'))


@app.route('/competitions/<int:id>', methods=['GET', 'POST'])
def manage_competition(id):

    form = CompetitionTeamForm(request.values, competition=id)
    comp = Competition.query.get(id)
    form.competition = comp.Name
    form.team.choices = [(a.id, a.Number) for a in Team.query.all()]

    user = session['username']

    teams = db.session.query(CompetitionTeam).filter(CompetitionTeam.Competitions == id).all()
    team_list = []
    for team in teams:
        team_list.append(int(team.Teams))
    team_data = db.session.query(Team).filter(Team.id.in_(team_list)).order_by(Team.Number).all()

    if user is None:
        redirect(url_for('signin'))
    else:
        if request.method == 'POST':
            if not form.validate():
                return render_template('competition_details.html', form=form, id=id, team_data=team_data)
            else:
                postdata = request.values
                comp = int(postdata['competition'])
                team = int(postdata['team'])

                newteam = CompetitionTeam(competitions=comp, teams=team, timestamp=datetime.datetime.now())
                db.session.add(newteam)
                db.session.commit()

                flash('Team successfully added to the competition.')
                return redirect(url_for('manage_competition', id=id))

        elif request.method == 'GET':
            return render_template('competition_details.html', form=form, id=id, team_data=team_data)


@app.route('/add-user', methods=['GET', 'POST'])
def add_user():
    form = AddUserForm()

    if 'username' not in session:
        return redirect(url_for('signin'))

    user = session['username']

    if user is None:
        redirect(url_for('signin'))
    else:
        if request.method == 'POST':
            if not form.validate():
                return render_template('adduser.html', form=form)
            else:
                newuser = Users(username=form.username.data.lower(),
                                password_hash=form.password.data,
                                role=form.role.data,
                                timestamp=datetime.datetime.now())
                db.session.add(newuser)
                db.session.commit()

                flash('User added.')
                return redirect(url_for('add_user'))

        elif request.method == 'GET':
            users = db.session.query(Users).filter(Users.role != 'admin').all()
            return render_template('adduser.html', form=form, users=users)


@app.route('/pit-scouting', methods=['GET', 'POST'])
def pit_scouting():

    form = PitScoutingForm(request.values)
    form.competition.choices = [(a.id, a.Name) for a in Competition.query.order_by('Name')]
    form.team.choices = [(a.id, a.Number) for a in Team.query.order_by('Number')]
    form.scout.choices = [(a.id, a.username) for a in Users.query.order_by('username')]

    if 'username' not in session:
        return redirect(url_for('signin'))

    user = session['username']

    # For role and form pre-select #
    match = db.session.query(Users).filter(Users.username == user).first()
    print match.username, match.id, match.role

    if user is None:
        redirect(url_for('signin'))
    else:
        if request.method == 'POST':
            if not form.validate():
                return render_template('pitscouting.html', form=form)
            else:
                postdata = request.values
                # general data
                competition = int(postdata['competition'])
                team = int(postdata['team'])
                scout = int(postdata['scout'])
                # autonomous data
                auto_offense = True if 'auto_offense' in request.form else False
                auto_defense = True if 'auto_defense' in request.form else False
                a_climbers = True if 'a_climbers' in request.form else False
                a_climbers_acc = postdata['a_climbers_acc']
                beacon = True if 'beacon' in request.form else False
                a_floorpark = True if 'a_floorpark' in request.form else False
                a_lowpark = True if 'a_lowpark' in request.form else False
                a_midpark = True if 'a_midpark' in request.form else False
                a_midpark_acc = postdata['a_midpark_acc']
                a_highpark = True if 'a_highpark' in request.form else False
                a_highpark_acc = postdata['a_highpark_acc']
                a_comments = postdata['a_comments']
                cycles = postdata['cycles']
                scorelow = True if 'scorelow' in request.form else False
                scoremid = True if 'scoremid' in request.form else False
                scorehigh = True if 'scorehigh' in request.form else False
                t_climbers = True if 't_climbers' in request.form else False
                t_climbers_acc = postdata['t_climbers_acc']
                lowclimber = True if 'lowclimber' in request.form else False
                lowclimber_acc = postdata['lowclimber_acc']
                midclimber = True if 'midclimber' in request.form else False
                midclimber_acc = postdata['midclimber_acc']
                highclimber = True if 'highclimber' in request.form else False
                highclimber_acc = postdata['highclimber_acc']
                t_floorpark = True if 't_floorpark' in request.form else False
                t_lowpark = True if 't_lowpark' in request.form else False
                t_midpark = True if 't_midpark' in request.form else False
                t_midpark_acc = postdata['t_midpark_acc']
                t_highpark = True if 't_highpark' in request.form else False
                t_highpark_acc = postdata['t_highpark_acc']
                hang = True if 'hang' in request.form else False
                allclear = True if 'allclear' in request.form else False
                comments = postdata['comments']
                watchlist = True if 'watchlist' in request.form else False

                # Roll up scoring data to highest level
                scorelow, scoremid, scorehigh = rollup(scorelow, scoremid, scorehigh)
                # Roll up parking data to highest level (auto & teleop)
                a_floorpark, a_lowpark, a_midpark, a_highpark = rollup(a_floorpark, a_lowpark, a_midpark, a_highpark)
                t_floorpark, t_lowpark, t_midpark, t_highpark = rollup(t_floorpark, t_lowpark, t_midpark, t_highpark)

                pitscoutingreport = PitScouting(comp=competition,
                                                team=team,
                                                scout=scout,
                                                auto_offense=auto_offense,
                                                auto_defense=auto_defense,
                                                a_climbers=a_climbers,
                                                a_climbers_acc=a_climbers_acc,
                                                beacon=beacon,
                                                a_floorpark=a_floorpark,
                                                a_lowpark=a_lowpark,
                                                a_midpark=a_midpark,
                                                a_midpark_acc=a_midpark_acc,
                                                a_highpark=a_highpark,
                                                a_highpark_acc=a_highpark_acc,
                                                a_comments=a_comments,
                                                cycles=cycles,
                                                scorelow=scorelow,
                                                scoremid=scoremid,
                                                scorehigh=scorehigh,
                                                t_climbers=t_climbers,
                                                t_climbers_acc=t_climbers_acc,
                                                lowclimber=lowclimber,
                                                lowclimber_acc=lowclimber_acc,
                                                midclimber=midclimber,
                                                midclimber_acc=midclimber_acc,
                                                highclimber=highclimber,
                                                highclimber_acc=highclimber_acc,
                                                t_floorpark=t_floorpark,
                                                t_lowpark=t_lowpark,
                                                t_midpark=t_midpark,
                                                t_midpark_acc=t_midpark_acc,
                                                t_highpark=t_highpark,
                                                t_highpark_acc=t_highpark_acc,
                                                hang=hang,
                                                allclear=allclear,
                                                comments=comments,
                                                watchlist=watchlist,
                                                timestamp=datetime.datetime.now())

                db.session.add(pitscoutingreport)
                db.session.commit()

                flash('Pit Scouting report successfully added.')
                return redirect(url_for('pit_scouting'))

        elif request.method == 'GET' :
            return render_template('pitscouting.html', form=form)


@app.route('/match-scouting', methods=['GET', 'POST'])
def match_scouting():

    form = MatchScoutingForm(request.values)
    form.competition.choices = [(a.id, a.Name) for a in Competition.query.order_by('Name')]
    form.team.choices = [(a.id, a.Number) for a in Team.query.order_by('Number')]
    form.scout.choices = [(a.id, a.username) for a in Users.query.order_by('username')]

    if 'username' not in session:
        return redirect(url_for('signin'))

    user = session['username']

    if user is None:
        redirect(url_for('signin'))
    else:
        if request.method == 'POST':
            if not form.validate():
                return render_template('matchscouting.html', form=form)
            else:
                postdata = request.values
                competition = int(postdata['competition'])
                team = int(postdata['team'])
                scout = int(postdata['scout'])
                match = int(postdata['match'])

                move = True if 'move' in request.form else False
                a_climbers = True if 'a_climbers' in request.form else False
                beacon = True if 'beacon' in request.form else False
                a_park = postdata['a_park']
                t_climbers = True if 't_climbers' in request.form else False
                score = True if 'score' in request.form else False
                cycles = postdata['cycles']
                scorelow = True if 'scorelow' in request.form else False
                scoremid = True if 'scoremid' in request.form else False
                scorehigh = True if 'scorehigh' in request.form else False
                lowclimber = True if 'lowclimber' in request.form else False
                midclimber = True if 'midclimber' in request.form else False
                highclimber = True if 'highclimber' in request.form else False
                t_park = postdata['t_park']
                hang = True if 'hang' in request.form else False
                allclear = True if 'allclear' in request.form else False
                comments = postdata['comments']

                #rollup scoring levels to highest level
                scorelow, scoremid, scorehigh = rollup(scorelow, scoremid, scorehigh)

                matchscoutingreport = MatchScouting(scout=scout,
                                                    team=team,
                                                    comp=competition,
                                                    match=match,
                                                    move=move,
                                                    a_climbers=a_climbers,
                                                    beacon=beacon,
                                                    a_park=a_park,
                                                    t_climbers=t_climbers,
                                                    score=score,
                                                    cycles=cycles,
                                                    scorelow=scorelow,
                                                    scoremid=scoremid,
                                                    scorehigh=scorehigh,
                                                    lowclimber=lowclimber,
                                                    midclimber=midclimber,
                                                    highclimber=highclimber,
                                                    t_park=t_park,
                                                    hang=hang,
                                                    allclear=allclear,
                                                    comments=comments,
                                                    timestamp=datetime.datetime.now())
                db.session.add(matchscoutingreport)
                db.session.commit()

                flash('Match scouting report successfully added.')
                return redirect(url_for('match_scouting'))

        elif request.method == 'GET':
            return render_template('matchscouting.html', form=form)


@app.route('/match-reporting', methods=['GET', 'POST'])
def match_reporting():

    form = MatchReportingForm(request.values)
    form.competition.choices = [(a.id, a.Name) for a in Competition.query.order_by('Name')]

    if 'username' not in session:
        return redirect(url_for('signin'))

    user = session['username']
    if user is None:
        redirect(url_for('signin'))
    else:
        if request.method == 'POST':
            if not form.validate():
                return render_template('matchreporting.html', form=form)
            else:
                postdata = request.values
                sql_text = '''select MatchScouting.id, Teams.Name, Teams.Number, Users.username,
                              (DidRobotMove*%d) +
                              (a_DeliverClimbers*%d) +
                              (PushBeacon*%d) +
                              (a_ParkingLevel*%d) +
                              (t_DeliverClimbers*%d) +
                              (DidRobotScoreCycles*%d) +
                              (HowManyCycles*%d) +
                              (ScoreLowZone*%d) +
                              (ScoreMidZone*%d) +
                              (ScoreHighZone*%d) +
                              (ReleaseLowClimber*%d) +
                              (ReleaseMidClimber*%d) +
                              (ReleaseHighClimber*%d) +
                              (t_DeliverClimbers*%d) +
                              (DidRobotHang*%d) +
                              (DidRobotTriggerAllClear*%d)
                              AS Score
                              FROM MatchScouting
                              INNER JOIN Teams
                                On MatchScouting.Team = Teams.id
                              INNER JOIN Users
                                On MatchScouting.Scout = Users.id
                              WHERE Competition = %d
                              ORDER BY Score
                              DESC''' % (int(postdata['move']),
                                         int(postdata['a_climbers']),
                                         int(postdata['score']),
                                         int(postdata['beacon']),
                                         int(postdata['a_park']),
                                         int(postdata['t_climbers']),
                                         int(postdata['cycles']),
                                         int(postdata['scorelow']),
                                         int(postdata['scoremid']),
                                         int(postdata['scorehigh']),
                                         int(postdata['lowclimber']),
                                         int(postdata['midclimber']),
                                         int(postdata['highclimber']),
                                         int(postdata['t_park']),
                                         int(postdata['hang']),
                                         int(postdata['allclear']),
                                         int(postdata['competition']))

                result = db.engine.execute(sql_text)
                teams = []
                for row in result:
                    teams.append([row[0], row[1], row[2], row[3], row[4]])
                session['matchreport'] = teams

                con = sqlite3.connect(":memory:")
                cur = con.cursor()
                cur.execute("create table t (id int, team_name text, team_number int, scout text, team_score int)");
                cur.executemany("insert into t values(?, ?, ?, ?, ?)", teams)
                con.commit()

                res = cur.execute("""
                  SELECT team_number, team_name, min(team_score), max(team_score), round(avg(team_score)) as average, count(team_score)
                    FROM t
                GROUP BY team_number
                ORDER BY average DESC""")

                rank = []
                for row in res:
                    rank.append(row)

                session['matchrank'] = rank

                return redirect(url_for('match_report'))

        elif request.method == 'GET':
            return render_template('matchreporting.html', form=form)


@app.route('/match-report')
def match_report():
    if 'username' not in session:
        return redirect(url_for('signin'))

    user = session['username']

    if user is None:
        redirect(url_for('signin'))
    else:
        matchdata = session['matchreport']
        matchrank = session['matchrank']
        if matchdata == '' or matchrank == '':
            redirect(url_for('match_reporting'))
        else:
            return render_template('matchreport.html', matchdata=matchdata, matchrank=matchrank)


@app.route('/match-report/<int:id>',)
def get_individual_matchreport(id):
    data = MatchScouting.query.get(id)
    return render_template('matchreport_details.html', data=data)