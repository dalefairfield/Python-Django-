from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
# imports the Bcrypt module
from flask.ext.bcrypt import Bcrypt
import re
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app, 'login_db')
# this will load a page that has 2 forms one for registration and login
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/', methods=['GET','POST'])
def index():
     return render_template('index.html')
    # we are going to add functions to create new users and login users

@app.route('/create_user', methods=['POST'])
def create_user():
     first_name = request.form['first_name']
     last_name = request.form['last_name']
     email = request.form['email']
     password = request.form['password']
     password_confirmation = request.form['password_confirmation']
     # run validations and if they are successful we can create the password hash with bcrypt
     pw_hash = bcrypt.generate_password_hash(password)
     # now we insert the new user into the database
     if len(first_name)>2:
         flash("First name successfully submitted")
        # print first_name

     else:
         flash("Please enter a valid first name")
         return redirect('/')

     if len(last_name)>2:
         flash("First name successfully submitted")
         # print last_name

     else:
         flash("Please enter a valid last name")
         return redirect('/')

     if EMAIL_REGEX.match(request.form['email']):
         flash("The entered email is a valid email address")
        #  print email

     else:
         flash("Invalid Email")
         return redirect('/')

     if len(password)>=8 and password == password_confirmation:
         flash("Password successfully submitted")
         # print password

     else:
         flash("Please enter a password containing at least 8 characters and/or make sure password matches the password confirmation.")
         return redirect('/')

     insert_query = "INSERT INTO users (first_name, last_name, email, pw_hash, created_at, updated_at) VALUES (:first_name, :last_name, :email, :pw_hash, NOW(), NOW())"
     query_data = {
                    'first_name':first_name,
                    'last_name':last_name,
                    'email': email,
                    'pw_hash': pw_hash
                }
     mysql.query_db(insert_query, query_data)
     return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email_login']
    password = request.form['password_login']
    user_query = "SELECT * FROM users WHERE email = :email LIMIT 1"
    query_data = { 'email': email, 'password' : password}
    user = mysql.query_db(user_query, query_data) # user will be returned in a list
    if len(request.form['email_login']) < 1:
        flash('fail')
        return redirect('/')
    else:
        flash('success')
        pw_hash = bcrypt.generate_password_hash(password)
        if bcrypt.check_password_hash(user[0]['pw_hash'], password):
            flash("Login Successful")
            return redirect('/')
        else:
            flash("Unsucccesful Login TRY AGAIN")
            return redirect('/')
    # return redirect('/')

@app.route('/logout', methods=['GET','POST'])
def index():
     return redirect('/')

app.run(debug=True) # run our server
