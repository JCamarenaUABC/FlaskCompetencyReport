from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

app.config["SECRET_KEY"] = "Algo"
#app.config['SECRET_KEY'] = 'any secret string'

from app import routes
