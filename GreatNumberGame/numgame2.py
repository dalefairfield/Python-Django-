from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

# our index route will handle rendering our form
@app.route('/')
def index():
    if not 'x' in session.keys():
        session['x']=random.randrange(0, 101)
    if not 'answer' in session.keys():
        session['answer']=''
    return render_template('index.html', answer=session['answer'])
# notice how we defined which HTTP methods are allowed by this route

@app.route('/users', methods=['POST'])
def create_user():
    guess = int(request.form['guess'])
    if session['x']>guess:
        session['answer'] = "Your guess was too low"
    elif session['x']<guess:
        session['answer'] = "Your guess was too high"
    else:
        session['answer'] = "You guessed correctly"
    return redirect('/')

# @app.route('/answers', methods=['POST'])
# def create_user():
#     guess = int(request.form['guess'])
#     if session['x']=guess:
#         session['x'].pop()
#         session['answers'].pop()
#     return redirect('/')

app.run(debug=True) # run our server
