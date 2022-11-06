from sqlalchemy import ForeignKey
from app import db
from datetime import datetime



class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(100)  ,  nullable=False)
    last_name = db.Column(db.String(100) , nullable=False)
    password = db.Column(db.String(10000) , nullable=False)
    email = db.Column(db.String(100), unique = True , nullable=False)
    hashcode = db.Column(db.String(100) , nullable = True)
    public_id = db.Column(db.String(100) , unique = True , nullable = True)
    created_at = db.Column(db.String(100) , default = datetime.now() , nullable = True)

 
 
    def __init__(self, first_name, last_name ,  password , email):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.email = email
        

    def __repr__(self):
        return f'<{self.first_name} { self.last_name } {self.email} {self.password} >'


class Topics(db.Model):
    __tablename__ = "topics"
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100)  ,  nullable=False)
    details = db.Column(db.String(100) , nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    photo_file =db.Column(db.String(100) , nullable=True)
    attach_file=db.Column(db.String(100) , nullable=True)
    status = db.Column(db.Integer , default = 1 , nullable = False)
    created_by = db.Column(db.Integer , db.ForeignKey('user.id'))
    created_at = db.Column(db.String(100) , default = datetime.now() , nullable = True)
    updated_at = db.Column(db.String(100) , default = datetime.now() , nullable = True)

    def __init__(self , title , details , photo_file , attach_file , created_by):
        self.title = title
        self.details = details
        self.attach_file = attach_file
        self.photo_file = photo_file
        self.created_by = created_by

    def __repr__(self):
        return f'< {self.title} {self.details} {self.created_by} >'


    def to_dict(self):
        return {'id' : self.id , 'title' : self.title , 'details' : self.details , 'photo_file' : self.photo_file , 'attach_file' : self.attach_file , 'status' : self.status , 'created_by' : self.created_by , 'created_at':self.created_at , 'updated_at':self.updated_at}


class Section(db.Model):
    __tablename__="section"
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100)  ,  nullable=False)
    details = db.Column(db.String(100) , nullable=False)
    photo_file =db.Column(db.String(100) , nullable=True)
    status = db.Column(db.Integer , default = 1 , nullable = False)
    created_by = db.Column(db.Integer , db.ForeignKey('user.id'))
    created_at = db.Column(db.String(100) , default = datetime.now() , nullable = True)
    updated_at = db.Column(db.String(100) , default = datetime.now() , nullable = True)


    def __init__(self , title , details , photo_file  , created_by):
        self.title = title
        self.details = details
        self.photo_file = photo_file
        self.created_by = created_by


    def __str__(self):
        return f'< {self.title} {self.details} {self.created_by} >'

    def to_dict(self):
        return {'id' : self.id , 'title' : self.title , 'details' : self.details , 'photo_file' : self.photo_file , 'status' : self.status , 'created_by' : self.created_by , 'created_at':self.created_at , 'updated_at':self.updated_at}


class Categories(db.Model):
    __tablename__ = "categories"
    id = db.Column(db.Integer , primary_key = True)
    user_id = db.Column(db.Integer , db.ForeignKey('user.id'))
    topic_id = db.Column(db.Integer , db.ForeignKey('topics.id'))
    section_id = db.Column(db.Integer , db.ForeignKey('section.id'))
    created_at = db.Column(db.String(100) , default = datetime.now() , nullable = True)
    updated_at = db.Column(db.String(100) , default = datetime.now() , nullable = True)

    def __init__(self , user_id , topic_id , section_id):
        self.user_id = user_id
        self.topic_id = topic_id
        self.section_id = section_id

    def __repr__(self):
        return f"{self.user_id} {self.topic_id} {self.section_id}"


class Comments(db.Model):
    __tablename__="comments"
    id = db.Column(db.Integer , primary_key = True)
    topic_id = db.Column(db.Integer , db.ForeignKey('topics.id'))
    first_name = db.Column(db.String(100)  ,  nullable=False)
    last_name = db.Column(db.String(100) , nullable=False)
    email = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer , db.ForeignKey('user.id'))
    comment = db.Column(db.String(200) , nullable=True)
    ratings = db.Column(db.Integer , nullable=True)
    created_at = db.Column(db.String(100) , default = datetime.now() , nullable = True)
    updated_at = db.Column(db.String(100) , default = datetime.now() , nullable = True)

    def __init_(self , topic_id , first_name , last_name , email , comment , ratings):
        self.topic_id = topic_id
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.comment = comment
        self.ratings = ratings

    def __repr__(self):
        return f"{self.first_name} {self.last_name} commented on {self.topic_id} as {self.comment} {self.ratings}"

    def to_dict(self):
        return {'id' : self.id , 'first_name' : self.first_name , 'self.last_name' : self.last_name , 'comment' : self.comment , 'ratings' : self.ratings , 'email' : self.email , 'created_at':self.created_at , 'updated_at':self.updated_at}


class Photos(db.Model):
    __tablename__="photos"
    id = db.Column(db.Integer , primary_key = True)
    topic_id = db.Column(db.Integer , db.ForeignKey('topics.id'))
    file = db.Column(db.String(200) , nullable = False)
    title = db.Column(db.String(200) , nullable = True)
    user_id = db.Column(db.Integer , db.ForeignKey('user.id'))
    urllink = db.Column(db.String(200) , nullable = True)
    created_at = db.Column(db.String(100) , default = datetime.now() , nullable = True)
    updated_at = db.Column(db.String(100) , default = datetime.now() , nullable = True)


    def __init_(self , topic_id , file , title , user_id , urllink):
        self.topic_id = topic_id
        self.file = file
        self.title = title
        self.user_id = user_id
        self.urllink = urllink
       

    def to_dict(self):
        return {'id' : self.id , 'topic_id' : self.topic_id , 'title' : self.title , 'file' : self.file , 'user' : self.user_id}