from rrftc import app
from flask import render_template, request, flash, session, url_for, redirect
from forms import SigninForm, CompetitionForm, ScoutForm, TeamForm, CompetitionTeamForm, ScoutingForm
from models import db, Competition, Scout, Team, CompetitionTeam, Scouting

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/signin', methods = ['GET', 'POST'])
def signin():
    form = SigninForm()

    if 'username' in session:
        return redirect(url_for('adminPanel'))

    if request.method == 'POST':
        if not form.validate():
            return render_template('signin.html', form=form)
        else:
            session['username'] = form.username.data
            return redirect(url_for('home'))

    elif request.method == 'GET':
        return render_template('signin.html', form=form)

@app.route('/signout')
def signout():

    if 'username' not in session:
        redirect(url_for('signin'))

    session.pop('username', None)
    return redirect(url_for('home'))


@app.route('/teams', methods = ['GET', 'POST'])
def teams():

    form = TeamForm()

    if 'username' not in session:
        return redirect(url_for('signin'))

    user = session['username']

    if user is None:
        redirect(url_for('signin'))
    else:
        if request.method == 'POST':
            if not form.validate():
                return render_template('teams.html', form=form)
            else:
                newteam = Team(number=form.number.data, name=form.name.data, website=form.website.data)
                db.session.add(newteam)
                db.session.commit()
                return redirect(url_for('teams'))

        elif request.method == 'GET' :
            teams = db.session.query(Team).all()
            teams = db.session.query(Team).order_by(Team.Number).all()
            return render_template('teams.html', teams=teams, form=form)

@app.route('/teams/delete/<int:id>',)
def delete_team_entry(id):
    team = Team.query.get(id)
    db.session.delete(team)
    db.session.commit()
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
                newcomp = Competition(name=form.name.data, date=form.date.data, location=form.location.data)
                db.session.add(newcomp)
                db.session.commit()
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
        return redirect(url_for('competitions'))

@app.route('/competitions/<int:id>', methods=['GET', 'POST'])
def manage_competition(id):

    form = CompetitionTeamForm(request.values, competition=id)
    comp = Competition.query.get(id)
    form.competition = comp.Name
    form.team.choices = [(a.id, a.Number) for a in Team.query.order_by('Number')]

    user = session['username']

    if user is None:
        redirect(url_for('signin'))
    else:
        if request.method == 'POST':
            if form.validate() == False:
                return render_template('competition_details.html', form=form, id=id)
            else:
                postdata = request.values
                comp = int(postdata['competition'])
                team = int(postdata['team'])

                newteam = CompetitionTeam(competitions=comp, teams=team)
                db.session.add(newteam)
                db.session.commit()

                return redirect(url_for('manage_competition', id=id))

        elif request.method == 'GET':
            teams = db.session.query(CompetitionTeam).filter(CompetitionTeam.Competitions == id).all()
            team_list = []
            for team in teams:
                team_list.append(int(team.Teams))
            team_data = db.session.query(Team).filter(Team.id.in_(team_list)).all()

            return render_template('competition_details.html', form=form, id=id, team_data=team_data)



@app.route('/scouts', methods=['GET', 'POST'])
def scouts():

    form = ScoutForm()

    if 'username' not in session:
        return redirect(url_for('signin'))

    user = session['username']

    if user is None:
        redirect(url_for('signin'))
    else:
        if request.method == 'POST':
            if form.validate() == False:
                return render_template('scouts.html', form=form)
            else:
                newscout = Scout(name=form.name.data)
                db.session.add(newscout)
                db.session.commit()
                return redirect(url_for('scouts'))

        elif request.method == 'GET' :
            scouts = db.session.query(Scout).all()
            return render_template('scouts.html', scouts=scouts, form=form)


@app.route('/scouts/delete/<int:id>',)
def delete_scout_entry(id):
    scout = Scout.query.get(id)
    db.session.delete(scout)
    db.session.commit()
    return redirect(url_for('scouts'))
'''

@app.route('/addMatch')
def addMatch():
    return render_template('addMatch.html')

@app.route('matches')
def matches():
    return render_template('matches.html')
'''
@app.route('/scouting', methods=['GET', 'POST'])
def scouting():

    form = ScoutingForm(request.values)
    form.competition.choices = [(a.id, a.Name) for a in Competition.query.order_by('Name')]
    form.team.choices = [(a.id, a.Number) for a in Team.query.order_by('Number')]
    form.scout.choices = [(a.id, a.Name) for a in Scout.query.order_by('Name')]

    if 'username' not in session:
        return redirect(url_for('signin'))

    user = session['username']

    if user is None:
        redirect(url_for('signin'))
    else:
        if request.method == 'POST':
            if not form.validate():
                return render_template('scouting.html', form=form)
            else:

                postdata = request.values
                # general data
                competition = int(postdata['competition'])
                team = int(postdata['team'])
                scout = int(postdata['scout'])
                rweight = float(postdata['rweight'])
                rheight = float(postdata['rheight'])
                # autonomous data
                if 'auto' in request.form:
                    auto = True
                    #test other autonomous conditions for true/false
                    beacon = True if 'beacon' in request.form else False
                    aclimbers = True if 'aclimbers' in request.form else False
                    lclimber = True if 'lclimber' in request.form else False
                    mclimber = True if 'mclimber' in request.form else False
                    hclimber = True if 'hclimber' in request.form else False
                    fpark = True if 'fpark' in request.form else False
                    lpark = True if 'lpark' in request.form else False
                    mpark = True if 'mpark' in request.form else False
                    hpark = True if 'hpark' in request.form else False
                else:
                    # set all autonomous to false
                    auto = False
                    beacon = False
                    aclimbers = False
                    lclimber = False
                    mclimber = False
                    hclimber = False
                    fpark = False
                    lpark = False
                    mpark = False
                    hpark = False
                climbheight = postdata['climbheight']
                # teleop data
                debris = True if 'debris' in request.form else False
                ldebrisscore = True if 'ldebrisscore' in request.form else False
                mdebrisscore = True if 'mdebrisscore' in request.form else False
                hdebrisscore = True if 'hdebrisscore' in request.form else False
                avgdebris = int(postdata['avgdebris'])
                debrisscoringmethod = postdata['debrisscoringmethod']
                hang = True if 'hang' in request.form else False
                # more general data
                allclear = True if 'allclear' in request.form else False
                spof = postdata['spof']
                comments = postdata['comments']
                watchlist = True if 'watchlist' in request.form else False

                scoutingreport = Scouting(scout=scout,
                                          team=team,
                                          comp=competition,
                                          weight=rweight,
                                          height=rheight,
                                          autonomous=auto,
                                          pushbeacon=beacon,
                                          deliverclimbers=aclimbers,
                                          lclimber=lclimber,
                                          mclimber=mclimber,
                                          hclimber=hclimber,
                                          fpark=fpark,
                                          lpark=lpark,
                                          mpark=mpark,
                                          hpark=hpark,
                                          highestzone=climbheight,
                                          scoredebris=debris,
                                          ldebris=ldebrisscore,
                                          mdebris=mdebrisscore,
                                          hdebris=hdebrisscore,
                                          avgdebris=avgdebris,
                                          debrismethod=debrisscoringmethod,
                                          hang=hang,
                                          allclear=allclear,
                                          spof=spof,
                                          comments=comments,
                                          watchlist=watchlist)




                db.session.add(scoutingreport)
                db.session.commit()


                return redirect(url_for('scouting'))



        elif request.method == 'GET' :
            reports = db.session.query(Scouting).all()
            return render_template('scouting.html', reports=reports, form=form)
