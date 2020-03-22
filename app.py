import datetime
import os
from flask import Flask
from flask import request, render_template, redirect, url_for, session, make_response
import user_storage
import init_quest


app = Flask(__name__)
app.permanent_session_lifetime = datetime.timedelta(days=31)
app.secret_key = os.urandom(24)


@app.route('/',  methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/game', methods=['GET'])
def game():
    if 'username' not in session:
        return redirect(url_for('home'))

    if not (user_storage.FileStorage.findByEmail(session['username'])):
        user_storage.FileStorage.saveUserProgress(session['username'], init_quest.quest_begin.code)

    currentStage = user_storage.FileStorage.loadUserProgress(session['username'])
    nextStagesCodes = user_storage.FileStorage.listNextStagesCode(session['username'])
    nextStagesNames = user_storage.FileStorage.listNextStagesName(nextStagesCodes)
    return render_template('game.html', currentStage=currentStage, nextStagesCodes=nextStagesCodes,
                           nextStagesNames=nextStagesNames)


@app.route('/restart', methods=['GET', 'POST'])
def restart():
    if user_storage.FileStorage.findByEmail(session['username']):
        user_storage.FileStorage.saveUserProgress(session['username'], init_quest.quest_begin.code)
        return redirect(url_for('game'))


@app.route('/game/running', methods=['POST'])
def running():
    if 'username' in session:
        stageFormCode = request.form.get('way')
        currentStage = user_storage.FileStorage.loadUserProgress(session['username'])
        if not user_storage.FileStorage.checkMove(currentStage, stageFormCode):
            return make_response("<h2>Bad Request</h2>", 400)

        user_storage.FileStorage.saveUserProgress(session['username'], stageFormCode)
        currentStage = user_storage.FileStorage.loadUserProgress(session['username'])
        nextStagesCodes = user_storage.FileStorage.listNextStagesCode(session['username'])
        nextStagesNames = user_storage.FileStorage.listNextStagesName(nextStagesCodes)
        return render_template('game.html', currentStage=currentStage, nextStagesCodes=nextStagesCodes,
                               nextStagesNames=nextStagesNames)
    else:
        return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'username' in session:
        return redirect(url_for('home'))

    if request.method == 'POST':
        if request.form['submit_button'] == 'Login':
            return redirect(url_for('login'))
        else:
            session['username'] = request.form['email']
            return redirect(url_for('home'))
    else:
        return render_template('login.html')


@app.route('/logout', methods=['GET'])
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
