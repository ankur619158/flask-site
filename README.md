# THIS IS THE PYTHON API BUILT IN FLASK

## STEPS TO EXECUTE THE CODE
Inside Flask-site Dir.

# 1. CREATE & ACTIVATE VIRTUAL ENV. 
       `virtualenv venv
        source ./venv/bin/activate`

# 2. RUN pip3 install r- requirements.txt 
        `at last run your flask app.

# 3. Run python3 run.py

******************************************************************************************************
To connect python to psql we need psycopg2 Driver
so `pip install psycopg2-binary`

## The Database Used In the app is "POSTGRESql" with "SQLAlchemy" To use ORM Queries
# configuration Postgres

=> app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@hostname:5432/database_name'
=> app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/flask_db'


## to run migration hit these commands / changes inside created Tables...
# 1. flask db init
# 2. flask db migrate -m "Initial migration"
# 3. flask db upgrade


*******************************************************************************************************

## To Check if login / sign up is working u can paste these code in routes Category
`
@app.route('/api/me')
def loggedUser():
    if session['email'] == None:
        return jsonify({"message" : "UnAuthenticated" , "status" : 404})
    else:
        user = User.query.filter_by(email = session['email']).first()
        data = {}
        data['name'] = user.name
        data['email'] = user.email
        return jsonify({"message" : "User Authenticated" , "User" : data , "status" : 200})
`

    Another way for Authenticating Rather than session is Json Web Token , which is passed inside
    headers bearer token every time to authenticate, It could possibly more secure...

**********************************************************************************************************
// optional 
## Token based Authentication...
       
# from flask_jwt_extended import *
        


**********************************************************************************************************

## Could be Possible way of sendign mail
            `server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.login('devtester619@gmail.com', 'rocffycohbymwzjw')

            server.sendmail('devtester619@gmail.com',email,
                            f'Your one time password is {pin}')`

    As per gmail guidelines from 30-May-22 the third party apps access is closed so to send mail u have to 
# go to your gmail security => on 2 factor authentication => again back to secrutiy => add app => generate password 

# Now use that password on python code to send mail to user. 

***********************************************************************************************************

##  For Validating User Input like email , password , name , pin etc we use Regular Expression in python 

    # from re module imported match function to match 2 global variables storing pattern for password & email


## Input Validation Criteria.

# Name
        should not contain special chracters
# Password
        * Atlease 1 capital & Lowercase letters & 1 number with atleast 1 special Chracters with the length of 8 digit.
# E-mail
        email should end with .3 letters & have @ 
# pin 
        should be 6 digit number

*************************************************************************************************************