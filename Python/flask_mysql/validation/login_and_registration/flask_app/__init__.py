# __init__.py
from flask import Flask
from flask import session, flash
app = Flask(__name__)
app.secret_key = "shhhhhh"
DATABASE = 'login_db'