from urllib import request
from xml.etree.ElementTree import Comment
from flask import jsonify
from app.models import Comments, User,Topics,Section
import jwt
from functools import wraps
from app import app


def token_required(f):
    @wraps(f)
    def decorated(*args , **kwargs):
        if "x-access-token" in request.headers:
            token = request.headers['x-access-token']
            if not token:
                return api_response(error = "token is missing")
            try:
                data = jwt.decode(token , app.config['secret_key'])
                current_user = User.query.filter_by(public_id = data['public_id']).first()
            except:
                return api_response(error = "invalid token")
        return f(current_user , *args , **kwargs)
    return decorated



def api_response(data = [] , error = "" ):
    if error != "":
        return jsonify({"sucess" : False , "error" : error , "data" : data})
    else:
        return jsonify({"sucess" : True , "error" : False , "data" : data})


def get_topic(id):
    topic = Topics.query.filter_by(id = id).first()
    return topic

def get_user(id):
    user = User.query.filter_by(id = id).first()
    return user

def get_section(id):
    section = Section.query.filter_by(id = id).first()
    return section

def get_comment(id):
    comment = Comments.query.filter_by(id = id).first()
    return comment


