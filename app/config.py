import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = 'dfkjfffnkfkfnkjfojijffjifknmvkjdjfoijfjlfdf'

    SESSION_PERMANENT = False
    SESSION_TYPE = 'filesystem'

    user = 'postgres'
    password = 'postgres'
    host = 'localhost'
    port = 5432
    db_name = 'flask_db'

    SQLALCHEMY_DATABASE_URI = f'postgresql://{user}:{password}@{host}:{port}/{db_name}'
    # SQLALCHEMY_DATABASE_URI ='sqlite:///' + os.path.join(basedir, 'database.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USERNAME = 'devtester619@gmail.com'
    MAIL_PASSWORD = 'rocffycohbymwzjw'
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True

