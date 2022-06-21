from app import forms, pwdApp, render_template, url_for, session, redirect, request, abort, flash

LOGIN = 'admin'
PASSWORD = '123'


# ============== routes ==========================
@pwdApp.route('/', methods=['GET'])
def index():
    return redirect(url_for('login'))


@pwdApp.route('/login', methods=['POST', 'GET'])
def login():
    form = forms.Logging()
    if 'userLogged' in session:
        return redirect(url_for('profile', username=session['userLogged']))

    elif request.method == 'POST' and request.form['username'] == LOGIN and request.form["psw"] == PASSWORD:
        session['userLogged'] = request.form['username']
        return redirect(url_for('profile', username=session['userLogged']))

    elif request.method == 'POST' and (request.form['username'] != LOGIN or request.form["psw"] != PASSWORD):
        return redirect(url_for('incorect_loginning_page'))

    return render_template('login.html', form=form)


@pwdApp.route('/incorect_loginning_page', methods=['GET'])
def incorect_loginning_page():
    if 'userLogged' in session:
        return redirect(url_for('profile', username=session['userLogged']))
    else:
        return render_template('incorect_loginning_page.html')


@pwdApp.route('/profile/<username>')
def profile(username):
    if 'userLogged' not in session or session['userLogged'] != username:
        abort(401)
    return render_template('profile.html', username=username)


@pwdApp.route('/logout')
def logout():
    if 'userLogged' in session:
        del session['userLogged']
    return redirect(url_for('index'))


# ============== errorhandlers ==========================
@pwdApp.errorhandler(404)
def pageNotFound(error):
    return render_template('page404.html'), 404


@pwdApp.errorhandler(401)
def pageNotFound(error):
    return render_template('page401.html'), 401
