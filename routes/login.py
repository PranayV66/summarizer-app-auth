from flask import Blueprint, render_template, request, redirect, url_for, session, g, current_app
from . import mysql
import MySQLdb.cursors
import hashlib

login_bp = Blueprint('login', __name__)

@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        hash_str = password + current_app.secret_key
        hash_str = hashlib.sha1(hash_str.encode())
        password_hashed = hash_str.hexdigest()
        
        g.db.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password_hashed,))
        account = g.db.fetchone()
        
        if account:
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            return redirect(url_for('home.home'))
        else:
            msg = 'Incorrect username/password!'
    return render_template('index.html', msg=msg)