## LOGIN API
# URL : http://127.0.0.1:5000/api/login
# Request Method = "POST"
----------------------------------------------------------------------------------------
# Header : accept Application/json
----------------------------------------------------------------------------------------
# email : tyrell@gmail.com
# password : RASPbe@123
----------------------------------------------------------------------------------------
`{
    "Success": true,
    "User": {
        "email": "ankur.shukla@esteplogic.com",
        "first_name": "Ron",
        "last_name": "Viseley",
        "password": "Seabn@123"
    },
    "execution_time": 0.01998305320739746,
    "message": "Logged In",
    "status": 200
}`

*****************************************************************************************

## SIGNUP API
# URL : http://127.0.0.1:5000/api/signup
# Request Method = "POST"
------------------------------------------------------------------------------------------
# Header : Accept Application/Json
------------------------------------------------------------------------------------------
# name:Ron Visel
# email:tyrell@gmail.com
# password:RASPbe@123
# password_confirmation:RASPbe@123
------------------------------------------------------------------------------------------
`
{
    "Success": true,
    "User": {
        "email": "tyrell@gmail.com",
        "first_name": "Ron",
        "last_name": "Visley",
        "password": "Seabn@123"
    },
    "execution_time": 0.006399631500244141,
    "message": "User Registered",
    "status": 200
}
`
********************************************************************************************

## FORGOT PASSWORD API
# URL : http://127.0.0.1:5000/api/forgot
# Request Method = "POST"
--------------------------------------------------------------------------------------------
# Header : Accept Applicaiton/Json
--------------------------------------------------------------------------------------------
# email : tyrell@gmail.com
--------------------------------------------------------------------------------------------
`
{
    "Execution Time": 3.3516969680786133,
    "Message": "Check Your E-Mail",
    "Success": true,
    "status": 200
}
`
*********************************************************************************************

## Pin Validation & Password Updation API ...
# URL : http://127.0.0.1:5000/api/reset
# Request Method = "POST"
---------------------------------------------------------------------------------------------
# Header : Accept Applicaiton/Json
---------------------------------------------------------------------------------------------
# email : tyrell@gmail.com
# pin    : `get it from your mail` eg . 2524568
# password : Newpass@123
# password_confirmation : Newpass@123
----------------------------------------------------------------------------------------------
`{
    "Execution Time": 0.008447647094726562,
    "Success": true,
    "message": "password_updated",
    "status": 200
}
`
**********************************************************************************************
