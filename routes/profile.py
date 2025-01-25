from flask import Blueprint, render_template, session, redirect, url_for, g
from . import mysql
import MySQLdb.cursors

profile_bp = Blueprint('profile', __name__)

@profile_bp.route('/auth/profile')
def profile():
    if 'loggedin' in session:
        g.db.execute('SELECT * FROM accounts WHERE user_id = %s', (session['user_id'],))
        account = g.db.fetchone()
        return render_template('profile.html', account=account)
    return redirect(url_for('login.login'))