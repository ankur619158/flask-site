from app import app,db,mail
from app.helpers import api_response
from app.models import User
from flask import request , jsonify , session , render_template
from time import time
from re import match
from random import randint
from flask_mail import Message
import uuid
import jwt



EmailPattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
PasswordPattern = r'(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[@$!%*#?&])[^ \s]{8,}'

@app.route('/')
def hello():
    return render_template("main.html")


@app.route('/api/login' , methods = ["POST"])
def login():
    if request.method == "POST":
        email = request.form['email']
        if not match(EmailPattern , email):                   # Validate E-mail
            return api_response(error="invalid email")

        password = request.form['password']
        if not match(PasswordPattern, password):                  # Validate Password
            return api_response(error="invalid password")
        
        row = User.query.filter_by(email = email , password = password).first()
        
        if row == None:                                     # Check Credentials
            return api_response(error="invalid credentials")  
        else:
            payload = {'public_id' : row.public_id}
            token = jwt.encode(payload , app.config['secret_key'])
            data = {'first_name' : row.first_name ,'last_name' : row.last_name , 'email' : row.email , 'password' : row.password , 'token' : token}
            session['email'] = row.email                    # Create Session
            return api_response(data = data)   
       


@app.route('/api/signup', methods = ["POST"])
def signup():
    if request.method == "POST":
        first_name = request.form["first_name"]
        if not match(r'^[a-zA-Z0-9_ ]*$' , first_name):     # Validate name
            return api_response(error="invalid first name")

        last_name = request.form["last_name"]
        if not match(r'^[a-zA-Z0-9]*$' , last_name):        # Validate last_name
            return api_response(error="invalid last name")

        email = request.form["email"]
        if not match(EmailPattern , email):                   # Validate email
            return api_response(error="invalid email")

        email_row = User.query.filter_by(email = email).first()
        if email_row is not None:                           # Check if already a user
            return api_response(error="email id already been used")

        password = request.form["password"]
        password_confirmation = request.form["password_confirmation"]

        if not match(PasswordPattern, password):                  # Validate password
            return api_response(error="make strong password")

        if(password == password_confirmation):
            user = User(first_name = first_name , last_name= last_name , email = email , password = password)
            user.public_id = str(uuid.uuid4()),
            db.session.add(user)                            # Data inserted
            db.session.commit()

            row = User.query.filter_by(email = email , password = password).first()
            data = {'first_name' : row.first_name , 'last_name' : row.last_name , 'email' : row.email , 'password' : row.password}
            payload = {'public_id' : row.public_id}
            data['token'] = jwt.encode(payload , app.config['secret_key'])
            session['email'] = row.email                    # Create session
            return api_response(data=data)  
        else:
            return api_response(error="password did not matched")         
        


@app.route('/api/forgot' , methods = ["POST"])
def forgot():
    start = time()
    if(request.method == "POST"):
        email = request.form['email']
        if not match(EmailPattern , email):                   # Validate email.
            return api_response(error="invalid email")

        user = User.query.filter_by(email = email).first()  # Check for user.
        if user == None:
            return api_response(error="E-mail id not in use")
        else:
            pin = randint(100000, 999999)                   # Generate pin.
            msg = Message('Robots', sender = 'devtester619@gmail.com', recipients = [email])
            msg.body = f"Your one time password is {pin}, You can Reset your password at https://example.com/api/reset ."
            mail.send(msg)                                  # Send mail

            user.hashcode = pin                             # Store pin for verification
            db.session.commit()
            return api_response(data=["otp sent to your email"])



@app.route('/api/reset' , methods = ["POST"])
def reset():
    start = time()
    if(request.method == "POST"):
        email = request.form['email']
        if not match(EmailPattern , email):                    # Validate email
            api_response(error="invalid email")

        hashcode = request.form['pin']
        if not match(r'[0-9]{6}' , hashcode):                # Validate Pin
            return api_response(error="invalid pin")
        password = request.form['password']
        password_confirmation = request.form['password_confirmation']

        user = User.query.filter_by(email = email).first()
        if(user.hashcode == hashcode):
            if not match(PasswordPattern, password):               # Validate Password
                api_response(error="create strong password")
            if (password == password_confirmation):          
                user.password = password                     # Password Updated
                db.session.commit()
                return api_response(data="password updated")
            else:
                return api_response(error="password did not matched")
        else:
            return api_response(error="invalid pin")


