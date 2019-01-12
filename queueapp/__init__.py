from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dab'

from queueapp import routes

