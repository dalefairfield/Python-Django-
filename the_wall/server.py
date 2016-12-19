from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
# imports the Bcrypt module
from flask.ext.bcrypt import Bcrypt
import re
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app, 'wall_db')
# this will load a page that has 2 forms one for registration and login
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/', methods=['GET'])
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
         session['first_name']=request.form['first_name']
     else:
         flash("Please enter a valid first name")
         return redirect('/')

     if len(last_name)>2:
         flash("First name successfully submitted")
         session['last_name']=request.form['last_name']
     else:
         flash("Please enter a valid last name")
         return redirect('/')

     if EMAIL_REGEX.match(request.form['email']):
         flash("The entered email is a valid email address")
         session['email']=request.form['email']
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
     register_info = mysql.query_db(insert_query, query_data)
     session['id'] = register_info
     return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email_login']
    password = request.form['password_login']
    user_query = "SELECT * FROM users WHERE email = :email LIMIT 1"
    query_data = { 'email': email }
    user = mysql.query_db(user_query, query_data) # user will be returned in a list
    if len(request.form['email_login']) < 1:
        flash('fail')
        return redirect('/')
    else:
        flash('success')
        if bcrypt.check_password_hash(user[0]['pw_hash'], password):
            session['first']=user[0]['first_name']
            session['last']=user[0]['last_name']
            session['id']=user[0]['id']
            # isValid= True
            return redirect('/wall')
        else:
            flash("Unsucccesful Login TRY AGAIN")
            return redirect('/')

@app.route('/wall', methods=['GET'])
def wall():
    # if isValid==True:
        message_query = "SELECT users.first_name, users.last_name, messages.id, messages.created_at, messages.message FROM users JOIN messages ON messages.users_id = users.id"
        comment_query = "SELECT comments.comment, comments.created_at, users.first_name, users.last_name, comments.messages_id FROM users JOIN comments ON users.id=comments.users_id"
        message = mysql.query_db(message_query)
        comment = mysql.query_db(comment_query)
        print comment
        return render_template('wall.html', message=message, comment=comment)
    # else:
    #     return redirect('/')

@app.route('/post', methods=['POST'])
def post():
    #  message = request.form['message']
     insert_query = "INSERT INTO messages (message, created_at, updated_at, users_id) VALUES ( :message, now(), now(), :user_id);"
     query_data = {
                 'user_id':session['id'],
                 'message':request.form['message']
                 }
     print session['id']
     mysql.query_db(insert_query, query_data)
     return redirect('/wall')


@app.route('/comment', methods=['POST'])
def comment():
    #  comment = request.form['comment']
     insert_query = "INSERT INTO comments (comment, created_at, updated_at, users_id, messages_id) VALUES (:comment, NOW(), NOW(), :user_id, :messages_id)"
     query_data = {
                    'user_id':session['id'],
                    'messages_id':request.form['message_id'],
                    'comment':request.form['comment']
                    }
     mysql.query_db(insert_query, query_data)
     return redirect('/wall')

@app.route('/logout', methods=['GET','POST'])
def logout():
     session['first_name']=''
     session['last_name']=''
     session['id']=''
     session['email']=''
     session['pw_hash']=''
     return redirect('/')

app.run(debug=True) # run our server

                    # 'first_name':first_name,
                    # 'last_name':last_name,
                    # 'messages.created_at':messages.created_at,

                        # 'comments.created_at':comments.created_at,
                        # 'first_name':first_name,
                        # 'last_name':last_name
