from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy




app = Flask(__name__)
app.config.from_object(Config)
app.config['JSON_AS_ASCII'] = False
db = SQLAlchemy(app)


from app import routes
