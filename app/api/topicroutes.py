from app import app,db
from app.models import  Topics , Comments
from app.helpers import api_response, get_comment,get_topic,get_user,get_comment
from flask import request  
from re import match
from werkzeug.utils import secure_filename
import os



@app.route('/api/topic/create', methods = ["POST"])
def topic_create():
    content = request.form
    title = content['title']
    details = content['details']
    description = content['description']
    photo_file = request.files['photo_file']
    if photo_file.filename != "":
        photo_file_name = secure_filename(photo_file.filename)
        photo_file.save(os.path.join(app.config['UPLOAD_FOLDER'], photo_file_name))
    attach_file = request.files['attach_file']
    if attach_file.filename != "":
        attach_file_name = secure_filename(attach_file.filename)
        attach_file.save(os.path.join(app.config['UPLOAD_FOLDER'], attach_file_name))

    topic = Topics(title=title , details=details ,description=description, photo_file=photo_file.filename , attach_file=attach_file.filename , created_by=1)
    db.session.add(topic)                            # Data inserted
    db.session.commit()
    data = get_topic(topic.id)
    data = data.to_dict()
    return api_response(data = data)


@app.route('/api/topic/update/<int:id>' , methods=["POST"])
def topic_update(id):
    topic = get_topic(id)
    if topic is not None:
        content = request.form
        if 'title' in content:
            title = content['title']
            topic.title = title
        if "details" in content:
            details = content['details']
            topic.details =details

        if 'description' in content:
            description = content['description']
            topic.description = description
            
        if "photo_file" in content:
            photo_file = request.files['filename']
            if photo_file.filename != "":
                photo_file_name = secure_filename(photo_file.filename)
                photo_file.save(os.path.join(app.config['UPLOAD_FOLDER'], photo_file_name))
                topic.photo_file =photo_file_name
        if "attach_file" in content:
            attach_file = request.files['attach_file']
            if attach_file.filename != "":
                attach_file_name = secure_filename(attach_file.filename)
                attach_file.save(os.path.join(app.config['UPLOAD_FOLDER'], attach_file_name))
                topic.attach_file =attach_file_name
        if "status" in content:
            status = content['status']
            topic.status = status
        db.session.commit()
        data = get_topic(id)
        data = data.to_dict()
        return api_response(data=data)
    else:
        return api_response(error="invalid id")


@app.route('/api/topic/delete/<int:id>' , methods=["POST"])
def topic_delete(id):
    topic = get_topic(id)
    if topic is not None:
        db.session.delete(topic)
        db.session.commit()
        return api_response(data = "topic_deleted")
    else:
        return api_response(error="Invalid id")


@app.route('/api/topic/comment/<int:topic_id>/<int:user_id>' , methods = ["POST"])
def create_comment(topic_id , user_id):
    content = request.json
    comment = content['comment']
    rating = content['ratings']
    user = get_user(user_id)
    c = Comments(topic_id , user.first_name , user.last_name , user.email , comment , rating)
    db.session.add(c)
    db.session.commit()
    comment = get_comment(c.id)
    comment = comment.to_dict()
    return api_response(data = comment)
        
        
        
        

