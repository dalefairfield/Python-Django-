from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    session['count']=0
    return redirect('/show')

@app.route('/show')
def showcount():
    session['count'] = session['count'] + 1
    return render_template('index.html', count=session['count'])

# @app.route('/')
# def index():
#     if session['count']<1:
#         session['count']=0
#         session['count'] = session['count'] + 1
#         return render_template('index.html', count=session['count'])
#     else:
#         session['count'] = session['count'] + 1
#         return render_template('index.html', count=session['count'])
app.run(debug=True)
