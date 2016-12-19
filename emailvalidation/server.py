from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
app = Flask(__name__)
mysql = MySQLConnector(app,'emaildb')
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    query = "SELECT * FROM users"
    emails =  mysql.query_db(query)
    return render_template("index.html", emails=emails)

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
@app.route('/users', methods=['POST'])
def users():
    email=request.form['email']

    if EMAIL_REGEX.match(request.form['email']):
        flash("The entered email is a valid email address")
        query = "INSERT INTO users (email) VALUES (:email)"
        data = {
                 'email': request.form['email']
               }
        mysql.query_db(query, data)
        return redirect('/')
    else:
       flash("Invalid Email")
       return redirect('/')

app.run(debug=True) # run our server
