import sys
import logging

activate_this = '/var/www/html/flask-site/roboenv/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

sys.path.insert(0 ,'/var/www/html/flask-site' )
sys.path.insert(0 , '/var/www/html/flask-site/roboenv/lib/python3.10/site-packages')

from app import app as application