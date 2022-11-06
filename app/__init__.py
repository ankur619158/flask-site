from flask import Flask

from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail
from flask_session import Session

# Configure Flask app
app = Flask(__name__)

app.secret_key = "dkjfjrehfjrkfnfiofjfjfirejr9refkfdnoijfjkd frenf21334dfkri23j42heewu54"

app.config['UPLOAD_FOLDER'] = '/var/www/html/flask-site/resources/topics'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

# Config.py file
app.config.from_object(Config)


# Configure Database Engine
db = SQLAlchemy(app)
migrate = Migrate(app,db)


# Configure Mail Engine
mail = Mail(app)


from app.api import routes,topicroutes,sectionroutes
from app.models import *