import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = 'dfkjfffnkfkfnkjfojijffjifknmvkjdjfoijfjlfdf'

    SESSION_PERMANENT = False
    SESSION_TYPE = 'filesystem'

    user = 'mclbtgevgkmygr'
    password = '6ab1508f58bdcee3831f3c4b46163470fbfdafd31fa4934783231dd699bfafc3'
    host = 'ec2-44-193-178-122.compute-1.amazonaws.com'
    port = 5432
    db_name = 'd5l41ilkvbelb7'

    # SQLALCHEMY_DATABASE_URI = f'postgresql://{user}:{password}@{host}:{port}/{db_name}'
    # SQLALCHEMY_DATABASE_URI ='sqlite:///' + os.path.join(basedir, 'database.db')
    SQLALCHEMY_DATABASE_URI = 'postgres://mclbtgevgkmygr:6ab1508f58bdcee3831f3c4b46163470fbfdafd31fa4934783231dd699bfafc3@ec2-44-193-178-122.compute-1.amazonaws.com:5432/d5l41ilkvbelb7'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USERNAME = 'devtester619@gmail.com'
    MAIL_PASSWORD = 'rocffycohbymwzjw'
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True

