from app.helpers import api_response,token_required,get_section
from app.models import Section
from app import app,db
from werkzeug.utils import secure_filename
from flask import request
import os
import json

@app.route('/section/create/<int:id>' , methods=["POST"])
def create():
    content = request.json
    if "title" not in content:
        return api_response(error="invalid title")
    title = content["title"]
    if "details" not in content:
        return api_response(error="Invalid details")
    details = content['details'] 
    if photo_file.filename != "":
        photo_file = request.files['photo_file']
        photo_file_name = secure_filename(photo_file.filename)
        photo_file.save(os.path.join(app.config['UPLOAD_FOLDER'], photo_file_name))      

    s = Section(title=title, 
    details=details, 
    photo_file=photo_file_name, 
    created_by=id
    )
    db.session.add(s)
    db.session.commit()
    section = get_section(s.id)
    section = section.to_dict()
    return api_response(data=section)


@app.route('/section/update/<int:id>' , methods =["POST"])
def update(id):
    content = request.json
    section = get_section(id)
    if section is not None:
        if 'title' in content:
            title = content['title']
            section.title = title
        if 'details' in content:
            details = content['details']
            section.details = details
        if photo_file.filename != "":
            photo_file = request.files['photo_file']
            photo_file_name = secure_filename(photo_file.filename)
            photo_file.save(os.path.join(app.config['UPLOAD_FOLDER'] , photo_file_name))
            section.photo_file = photo_file_name
        db.session.add(section)
        db.session.commit()
        section = get_section(id)
        section = section.to_dict()
        return api_response(data = section)
    else:
        return api_response(error="invalid id")


@app.route('/section/delete/<int:id>' , methods = ["POST"])
def delete(id):
    section = get_section(id)
    if section is not None:
        db.session.delete(section)
        db.session.commit()
        return api_response(data = "section deleted")
    else:
        return api_response(error = "Invalid id")

