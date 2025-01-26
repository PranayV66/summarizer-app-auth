from flask import Blueprint, render_template, session, redirect, url_for

home_bp = Blueprint('home', __name__, url_prefix='/auth')

@home_bp.route('/home')
def home():
    if 'loggedin' in session:
        return render_template('home.html', username=session['username'])
    return redirect(url_for('login.login'))