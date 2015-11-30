from rrftc import app
from flask import render_template, request, flash, session, url_for, redirect
from forms import SigninForm, CompetitionForm, ScoutForm
from models import db, Competition, Scout


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/adminPanel')
def adminPanel():

    if 'username' not in session:
        return redirect(url_for('signin'))

    user = session['username']
    print user

    if user is None:
        redirect(url_for('signin'))
    else:
        return render_template('adminPanel.html')


@app.route('/signin', methods = ['GET', 'POST'])
def signin():
    form = SigninForm()

    if 'username' in session:
        return redirect(url_for('adminPanel'))

    if request.method == 'POST':
        if form.validate() == False:
            return render_template('signin.html', form=form)
        else:
            session['username'] = form.username.data
            return redirect(url_for('adminPanel'))

    elif request.method == 'GET':
        return render_template('signin.html', form=form)

@app.route('/signout')
def signout():

    if 'username' not in session:
        redirect(url_for('signin'))

    session.pop('username', None)
    return redirect(url_for('home'))

'''
@app.route('/addTeam')
def addTeam():
    return render_template('addTeam.html')

@app.route('/teams')
def teams():
    return render_template('teams.html')

@app.route('/addCompetition')
def addCompetition():
    return render_template('addCompetition.html')
'''

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
def delete_entry(id):
    competition = Competition.query.get(id)
    db.session.delete(competition)
    db.session.commit()
    return redirect(url_for('competitions'))



'''
    form = SigninForm()

    if 'username' in session:
        return redirect(url_for('adminPanel'))

    if request.method == 'POST':
        if form.validate() == False:
            return render_template('signin.html', form=form)
        else:
            session['username'] = form.username.data
            return redirect(url_for('adminPanel'))

    elif request.method == 'GET':
        return render_template('signin.html', form=form)
'''



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
'''

@app.route('/addMatch')
def addMatch():
    return render_template('addMatch.html')

@app.route('matches')
def matches():
    return render_template('matches.html')

@app.route('/scouting')
def scouting():
    return render_template('scouting.html')
'''