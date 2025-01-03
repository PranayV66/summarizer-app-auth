from flask_mysqldb import MySQL
from flask import g
import MySQLdb

mysql = MySQL()

def init_app(app):
    mysql.init_app(app)

    @app.before_request
    def before_request():
        g.db = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

    @app.teardown_request
    def teardown_request(exception):
        if hasattr(g, 'db'):
            g.db.close()