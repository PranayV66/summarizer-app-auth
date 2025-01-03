from flask import Flask, render_template, request, redirect, url_for, session
import os
from routes import init_app

app = Flask(__name__, template_folder='templates')

app.secret_key = os.environ.get('APP_SECRET_KEY')

app.config['MYSQL_HOST'] = os.environ.get('SQL_HOST')
app.config['MYSQL_USER'] = os.environ.get('SQL_USER')
app.config['MYSQL_PASSWORD'] = os.environ.get('SQL_PASSWORD')
app.config['MYSQL_DB'] = os.environ.get('SQL_DB')

# Initialize MySQL
init_app(app)

# Import blueprints
from routes.login import login_bp
from routes.logout import logout_bp
from routes.register import register_bp
from routes.home import home_bp
from routes.profile import profile_bp

# Register blueprints
app.register_blueprint(login_bp)
app.register_blueprint(logout_bp)
app.register_blueprint(register_bp)
app.register_blueprint(home_bp)
app.register_blueprint(profile_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)