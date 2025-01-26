from flask import Blueprint, redirect, url_for, session

logout_bp = Blueprint('logout', __name__, url_prefix='/auth')

@logout_bp.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('user_id', None)
    session.pop('username', None)
    return redirect(url_for('login.login'))