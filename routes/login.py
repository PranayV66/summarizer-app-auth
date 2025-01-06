from flask import Blueprint, render_template, request, redirect, url_for, session, g, current_app, make_response
from . import mysql
import jwt
import datetime
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
            session['user_id'] = account['user_id']
            session['username'] = account['username']

            token = jwt.encode({
                'user_id': account['user_id'],
                'username': account['username'],
                'exp': datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=1)
                }, current_app.secret_key, algorithm='HS256')

            response = make_response(redirect(url_for('home.home')))
            response.set_cookie('token', token, httponly=True, secure=True, samesite='Strict')
            return response
            # return redirect(url_for('home.home'))
        else:
            msg = 'Incorrect username/password!'
    return render_template('index.html', msg=msg)