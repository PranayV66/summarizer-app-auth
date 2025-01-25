from flask import Blueprint, render_template, request, current_app, g
from . import mysql
import re, hashlib

register_bp = Blueprint('register', __name__)

@register_bp.route('/auth/register', methods=['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        
        g.db.execute('SELECT * FROM accounts WHERE username = %s', (username,))
        account = g.db.fetchone()
        
        if account:
            msg = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers!'
        elif not username or not password or not email:
            msg = 'Please fill out the form!'
        else:
            hash = password + current_app.secret_key
            hash = hashlib.sha1(hash.encode())
            password = hash.hexdigest()
            g.db.execute('INSERT INTO accounts VALUES (NULL, %s, %s, %s)', (username, password, email,))
            mysql.connection.commit()
            msg = 'You have successfully registered!'
    return render_template('register.html', msg=msg)